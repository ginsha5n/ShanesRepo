/*--------------------------------------------------------------------------*/
/*                                                                          */
/*       comp1                                                              */
/*                                                                          */
/*                                                                          */
/*       Group Members:          ID numbers                                 */
/*                                                                          */
/*           John Doe            12345678                                   */
/*           Jane Murphy         23456789                                   */
/*           Anthony N. Other    12345679                                   */
/*                                                                          */
/*                                                                          */
/*       Currently this file is just a placeholder (actually a copy of      */
/*       "smallparser.c", which is just a simple parser, not a compiler at  */
/*       all).                                                              */
/*       When you have completed the second part of the project (i.e.,      */
/*       "parser2.c") copy it over this file.  In this way, "comp1.c"       */
/*       builds upon your earlier parser work.                              */
/*                                                                          */
/*--------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/
/*                                                                          */
/*       parser1                                                            */
/*                                                                          */
/*                                                                          */
/*       Group Members:          ID numbers                                 */
/*                                                                          */
/*           Shane Ginty            12345678                                */
/*           James Martin           23456789                                */
/*           James Mcgrath          123456                                  */
/*           Emma Madden                                                    */
/*                                                                          */
/*                                                                          */
/*       Currently just a copy of "smallparser.c".  To create "parser1.c",  */
/*       modify this source to reflect the CPL grammar.                     */
/*                                                                          */
/*--------------------------------------------------------------------------*/
/*                                                                          */
/*       parser1.c      Intial stab at a version of parser1.c using a       */
/*                      very small (& modified) subset of the CPL grammar   */
/*                                                                          */
/*       An illustration of the use of the character handler and scanner    */
/*       in a parser for the language                                       */
/*                                                                          */
/*       <Program>       :==  "PROGRAM" <Identifier> ";"                    */
/*                            [ <Declarations> ] <Block> "."           (1)  */
/*       <Declarations>  :==  "VAR" <Variable> { "," <Variable> } ";"  (2)  */
/*       <Block>         :==  "BEGIN" { <Statement> ";" } "END"        (3)  */
/*       <Statement>     :==  <Identifier> ":=" <Expression>           (4)  */
/*       <Expression>    :==  <Term> { ("+"|"-") <Term> }              (5)  */
/*       <Term>          :==  <Variable> | <IntConst>                  (6)  */
/*       <Variable>      :==  <Identifier>                             (7)  */
/*                                                                          */
/*                                                                          */
/*       Note - <Identifier> and <IntConst> are provided by the scanner     */
/*       as tokens IDENTIFIER and INTCONST respectively.                    */
/*                                                                          */
/*       As <Variable> is just a renaming of <Identifier>, we will omit     */
/*       any explicit implementation of <Variable>, and just use            */
/*       "Accept( IDENTIFIER );"  wherever a <Variable> is needed.          */
/*                                                                          */
/*       Although the listing file generator has to be initialised in       */
/*       this program, full listing files cannot be generated in the        */
/*       presence of errors because of the "crash and burn" error-          */
/*       handling policy adopted. Only the first error is reported, the     */
/*       remainder of the input is simply copied to the output (using       */
/*       the routine "ReadToEndOfFile") without further comment.            */
/*                                                                          */
/*--------------------------------------------------------------------------*/

/* Old */ 
/*       <Program>     :== "BEGIN" { <Statement> ";" } "END" "."            */
/*       <Statement>   :== <Identifier> ":=" <Expression>                   */
/*       <Expression>  :== <Identifier> | <IntConst>                        */
/*                                                                          */
/* New*/
/*       <Program>     :== PROGRAM" <identifier> ";"            */
/*                         [<declaration>] <block> "."          */
/*       <Declaration> :== "VAR" <variable> {"," <variable> } ";"*/
/*       <Block> :==  "BEGIN" {<statement> ";"} "END"*/
/*       <Statement>   :== <Identifier> ":=" <Expression>                   */
/*       <Expression>  :== <Identifier> | <IntConst>                        */
/*          <term>*/
/*                                                                          */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "global.h"
#include "scanner.h"
#include "line.h"





/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  Global variables used by this parser.                                   */
/*                                                                          */
/*--------------------------------------------------------------------------*/

PRIVATE FILE *InputFile;           /*  CPL source comes from here.          */
PRIVATE FILE *ListFile;            /*  For nicely-formatted syntax errors.  */

PRIVATE TOKEN  CurrentToken;       /*  Parser lookahead token.  Updated by  */
                                   /*  routine Accept (below).  Must be     */
                                   /*  initialised before parser starts.    */


/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  Function prototypes                                                     */
/*                                                                          */
/*--------------------------------------------------------------------------*/

PRIVATE void ParseProgram( void );
PRIVATE void ParseDeclarations( void );

PRIVATE void ParseProcDeclaration(void);
PRIVATE void ParseParameterList(void);

PRIVATE void ParseBlock(void);
PRIVATE void ParseStatement(void);
PRIVATE void ParseExpression(void);
PRIVATE void ParseTerm(void);
PRIVATE void ParseCondition(void);
PRIVATE void ParseAssignment(void);
PRIVATE void ParseWhileLoop(void);
PRIVATE void ParseWriteStatement(void);



PRIVATE void Accept( int code );
PRIVATE int  OpenFiles( int argc, char *argv[] );
PRIVATE void Synchronise(SET *F, SET *FB);
PRIVATE void SetupSets(void);



SET StatementFs_aug;
SET StatementB;
SET StatementFBS;
SET StatementFs;
SET StatementSec;
SET StatementFolB;
SET StatementB_aug;

/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  Main: Smallparser entry point.  Sets up parser globals (opens input and */
/*        output files, initialises current lookahead), then calls          */
/*        "ParseProgram" to start the parse.                                */
/*                                                                          */
/*--------------------------------------------------------------------------*/

PUBLIC int main ( int argc, char *argv[] )
{

    
    if ( OpenFiles( argc, argv ) )  {
        
        InitCharProcessor( InputFile, ListFile );
        CurrentToken = GetToken();
        SetupSets();
        ParseProgram();
        
        fclose( InputFile );
        fclose( ListFile );
        printf("\nValid\n");
        return  EXIT_SUCCESS;
    }
    else {
        return EXIT_FAILURE;
    }
}


/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  Parser routines: Recursive-descent implementaion of the grammar's       */
/*                   productions.                                           */
/*                   Accept a program and accept an identifier*/
/*                                                                          */
/*                                                                          */
/*  ParseProgram implements:                                                */
/*                                                                          */
/*       <Program>     :== "BEGIN" { <Statement> ";" } "END" "."            */
/*                                                                          */
/*                                                                          */
/*    Inputs:       None                                                    */
/*                                                                          */
/*    Outputs:      None                                                    */
/*                                                                          */
/*    Returns:      Nothing                                                 */
/*                                                                          */
/*                             */
/*                                                                          */
/*--------------------------------------------------------------------------*/

PRIVATE void ParseProgram(void)
{
    Accept( PROGRAM );
    Accept( IDENTIFIER );
    Accept( SEMICOLON );

    Synchronise(&StatementFs, &StatementFolB);

    if ( CurrentToken.code == VAR ) ParseDeclarations();

    Synchronise(&StatementSec, &StatementFolB);

    while (CurrentToken.code == PROCEDURE){
        ParseProcDeclaration();
        Synchronise(&StatementSec, &StatementFolB);
    }

    ParseBlock();
    
    Accept( ENDOFPROGRAM );     /* Token "." has name ENDOFPROGRAM          */
    Accept( ENDOFINPUT );
}

PRIVATE void ParseDeclarations( void )
{
    Accept( VAR );
    Accept( IDENTIFIER );   /* <Variable> is just a remaning of IDENTIFIER. */
    
    /* EBNF repetition operator {...} implemented as a while-loop.          */
    /* Repetition triggered by "," (i.e, COMMA) in lookahead.               */

    while ( CurrentToken.code == COMMA ) {
        Accept( COMMA );
        Accept( IDENTIFIER );
    }
    Accept( SEMICOLON );
}

PRIVATE void ParseProcDeclaration(void) {
    Accept(PROCEDURE);
    Accept(IDENTIFIER); 


    Synchronise(&StatementFs, &StatementFolB);
    
    if (CurrentToken.code == LEFTPARENTHESIS) {
        ParseParameterList();
        Accept(SEMICOLON);
        Synchronise(&StatementSec, &StatementFolB);
    }

    if (CurrentToken.code == VAR) {
        ParseDeclarations();
        Synchronise(&StatementSec, &StatementFolB);
    }

    while (CurrentToken.code == PROCEDURE) {
        ParseDeclarations();
        Synchronise(&StatementSec, &StatementFolB);
    }


    ParseBlock(); 
    Accept(SEMICOLON); 
}

PRIVATE void ParseParameterList(void) {
    Accept(LEFTPARENTHESIS);

    if (CurrentToken.code != RIGHTPARENTHESIS) {
        ParseDeclarations();

        while (CurrentToken.code == COMMA) {
            Accept(COMMA);
            ParseDeclarations();
        }
    }
    Accept(RIGHTPARENTHESIS);
}

PRIVATE void ParseBlock(void)
{
    Accept(BEGIN);
    Synchronise(&StatementFs_aug, &StatementFBS);
    
    while (CurrentToken.code != END)
    {
        ParseStatement();
        Accept(SEMICOLON); 
        Synchronise(&StatementFs_aug, &StatementFBS);
    }

    Accept(END);
}



/*PRIVATE void ParseStatement( void )
{
    Accept( IDENTIFIER );        <Variable> is just token IDENTIFIER.     
    Accept( ASSIGNMENT );        ":=" has token name ASSIGNMENT.          
    ParseExpression();
}*/ 


PRIVATE void ParseStatement( void )
{
    if (CurrentToken.code == IDENTIFIER) {
        ParseAssignment();
    } else if (CurrentToken.code == WHILE) {
        ParseWhileLoop();
    } else if (CurrentToken.code == WRITE) {
        ParseWriteStatement();
    } else {
        SyntaxError(IDENTIFIER, CurrentToken);
        CurrentToken = GetToken();
    }
}














PRIVATE void ParseExpression( void )
{
    int token;

    ParseTerm();

    /* EBNF repetition operator {...} handled by while-loop.  Note that the */
    /* presence of either token "+" or token "-" in the lookahead triggers  */
    /* the repetition.                                                      */

    while ( (token = CurrentToken.code) == ADD ||    /* ADD: name for "+".  */
            token == SUBTRACT ) {                    /* SUBTRACT: "-".      */
        Accept(token);
        ParseExpression();
    }
}

PRIVATE void ParseTerm( void )
{
    /* EBNF "or" operator: "|" implemented as an if-else block. If-path     */
    /* triggered by a <Variable> in the input stream, which is just an      */
    /* <Identifier>, i.e., token IDENTIFIER.  Else-path is taken otherwise. */
    /* N.B., in the case of a syntax-error, this error will be reported as  */
    /* "INTCONST expected" because of this behaviour.                       */

    if ( CurrentToken.code == IDENTIFIER )  Accept( IDENTIFIER );
    else  Accept( INTCONST );
}

PRIVATE void ParseCondition(void) {
    ParseExpression();
    if (CurrentToken.code == LESS || CurrentToken.code == GREATER || CurrentToken.code == EQUALITY ) {
        Accept(CurrentToken.code);
        ParseExpression();
    }
}

PRIVATE void ParseAssignment(void) {
    Accept(IDENTIFIER);
    Accept(ASSIGNMENT);
    ParseExpression();
}

PRIVATE void ParseWhileLoop(void) {
    Accept(WHILE);
    ParseCondition();
    Accept(DO);
    ParseBlock();
}

PRIVATE void ParseWriteStatement(void) {
    Accept(WRITE);
    Accept(LEFTPARENTHESIS);
    ParseExpression();
    while (CurrentToken.code == COMMA) {
        Accept(COMMA);
        ParseExpression();
    }
    Accept(RIGHTPARENTHESIS);
}





/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  End of parser.  Support routines follow.                                */
/*                                                                          */
/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  Accept:  Takes an expected token name as argument, and if the current   */
/*           lookahead matches this, advances the lookahead and returns.    */
/*                                                                          */
/*           If the expected token fails to match the current lookahead,    */
/*           this routine reports a syntax error and exits ("crash & burn"  */
/*           parsing).  Note the use of routine "SyntaxError"               */
/*           (from "scanner.h") which puts the error message on the         */
/*           standard output and on the listing file, and the helper        */
/*           "ReadToEndOfFile" which just ensures that the listing file is  */
/*           completely generated.                                          */
/*                                                                          */
/*                                                                          */
/*    Inputs:       Integer code of expected token                          */
/*                                                                          */
/*    Outputs:      None                                                    */
/*                                                                          */
/*    Returns:      Nothing                                                 */
/*                                                                          */
/*    Side Effects: If successful, advances the current lookahead token     */
/*                  "CurrentToken".                                         */
/*                                                                          */
/*--------------------------------------------------------------------------*/

/* S-algol error recovery,  check out Lecture 14 for pros and cons etc.*/
/* Report the error, let the parser keep parsing*/
/* look ahead (get token) is not advanced*/

PRIVATE void Accept( int ExpectedToken )
{
    /*"mode flag"*/
    static int recovering = 0; 

    /*Error resync*/
    if (recovering){ 
        while( CurrentToken.code != ExpectedToken && CurrentToken.code != ENDOFINPUT)
        CurrentToken = GetToken();
        recovering = 0;
    }

    /*Normal accept*/ 
    if ( CurrentToken.code != ExpectedToken )  {
        SyntaxError( ExpectedToken, CurrentToken );
        recovering = 1;
    }

    else CurrentToken = GetToken();
}


/*--------------------------------------------------------------------------*/
/*                                                                          */
/*  OpenFiles:  Reads strings from the command-line and opens the           */
/*              associated input and listing files.                         */
/*                                                                          */
/*    Note that this routine mmodifies the globals "InputFile" and          */
/*    "ListingFile".  It returns 1 ("true" in C-speak) if the input and     */
/*    listing files are successfully opened, 0 if not, allowing the caller  */
/*    to make a graceful exit if the opening process failed.                */
/*                                                                          */
/*                                                                          */
/*    Inputs:       1) Integer argument count (standard C "argc").          */
/*                  2) Array of pointers to C-strings containing arguments  */
/*                  (standard C "argv").                                    */
/*                                                                          */
/*    Outputs:      No direct outputs, but note side effects.               */
/*                                                                          */
/*    Returns:      Boolean success flag (i.e., an "int":  1 or 0)          */
/*                                                                          */
/*    Side Effects: If successful, modifies globals "InputFile" and         */
/*                  "ListingFile".                                          */
/*                                                                          */
/*--------------------------------------------------------------------------*/

PRIVATE int  OpenFiles( int argc, char *argv[] )
{
    if ( argc != 3 )  {
        fprintf( stderr, "%s <inputfile> <listfile>\n", argv[0] );
        return 0;
    }

    if ( NULL == ( InputFile = fopen( argv[1], "r" ) ) )  {
        fprintf( stderr, "cannot open \"%s\" for input\n", argv[1] );
        return 0;
    }

    if ( NULL == ( ListFile = fopen( argv[2], "w" ) ) )  {
        fprintf( stderr, "cannot open \"%s\" for output\n", argv[2] );
        fclose( InputFile );
        return 0;
    }

    return 1;
}

/* Check out lecture 15 for some info on this function*/
PRIVATE void Synchronise(SET *F, SET *FB)
{
    SET S;
    S = Union(2, F, FB);

    if(!InSet(F, CurrentToken.code))
    {
        SyntaxError2(*F, CurrentToken);
        while(!InSet(&S, CurrentToken.code))
            CurrentToken = GetToken();

    }
}

    

/* Check out lecture 15 for some info on this function*/
PRIVATE void SetupSets(void)
{
    InitSet(&StatementFs_aug , 6, IDENTIFIER, WHILE, IF, READ, WRITE, END);
    InitSet(&StatementFBS , 4, SEMICOLON, ELSE, ENDOFPROGRAM, ENDOFINPUT);

    InitSet(&StatementFs , 3, VAR, PROCEDURE, BEGIN);
    InitSet(&StatementSec , 2, PROCEDURE, BEGIN);
    InitSet(&StatementFolB , 3, ENDOFPROGRAM, ENDOFINPUT, END);
    
    InitSet(&StatementB , 2, ENDOFINPUT, END);
    InitSet(&StatementB_aug , 3, ENDOFINPUT, ENDOFPROGRAM, END);
}
 