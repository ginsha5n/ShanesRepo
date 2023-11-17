# import pytest

def one():
    return 1

def testOne():

    x = one()
    assert x ==1

def oddOrEven(x):

    if (x%2) == 0:
        return "Even"
    else:
        return "Odd"
    
def testTwo():
    
    ans = oddOrEven(6)
    assert ans =="Even"

    ans = oddOrEven(7)
    assert ans !="Even"



