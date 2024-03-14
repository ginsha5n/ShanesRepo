!
!               salgol1.pro
!               program to test error detection of a parser
!               augmented with basic S-Algol error recovery.
!
PROGRAM perror;
VAR x, y;

PROCEDURE p( p1, p2, p3, REF p4 );
VAR p5, p6, p7;
BEGIN
    p4 := (p1+p2)*p3;
END;

BEGIN
    p:=( 1, 2, 3, x);
    IF x = 3 THEN     
        y := x;
    END
    ELSE
    BEGIN           
        y := 3;
    END;
    IF x <= y THEN BEGIN
    END;
END.
