!		
!		augsalgol.pro
!		program to test simple Augmented S-Algol
!		recovery. (N.B., don't need to report
!		restart point if you don;t want.)
!
PROGRAM augsalgol;
VAR x;
BEGIN
    WHILE x > 0 BEGIN DO   ! reversed
        WRITE(x);
        x := x - 1;
    END;
END.
