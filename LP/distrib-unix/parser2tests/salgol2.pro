!
!               salgol2.pro
!               program to test error detection of parser 
!               augmented with S-Algol error recovery.
!
PROGRAM perror;
VAR x, y;

BEGIN
    IF x = 3 THEN BEGIN  
        y = x;		! Got an equality where an assignment expected
    END
    ELSE                ! BEGIN expected
        y = 3;          ! Got an equality where an assignment expected
    END;
END.
