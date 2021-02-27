#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: Feb 2021
# Description:
#   Command line script to find integer roots of polynomials with
#   integer coefficients.


#-------------------------------------------------------------------#
#                                                                   #
#                   Command-line interface                          #
#                                                                   #
#-------------------------------------------------------------------#

PROGRAM_EXPLANATION = """
Usage:
$ python roots.py COEFF1 COEFF2 ...

Find integer roots of a polynomial with integer coefficients.

Example:

Find the roots of x^4 - 3x^3 - 75x^2 + 475x - 750.

$ python roots.py 1 -3 -75 475 -750
-10
3
5
"""


def main(*arguments):
    """Main entry point for the program"""
    if not arguments:
        print(PROGRAM_EXPLANATION)
        return

    poly = parse_coefficients(arguments)
    roots = integer_roots(poly)
    print_roots(roots)


def parse_coefficients(arguments):
    """Convert string arguments to integer

    >>> parse_coefficients(["2", "3"])
    [2, 3]
    """
    return [int(arg) for arg in arguments]


def print_roots(roots):
    """Print the roots one per line if there are any

    >>> print_roots([2, 3])
    2
    3
    """
    if roots:
        roots_str = [str(r) for r in roots]
        print('\n'.join(roots_str))


#-------------------------------------------------------------------#
#                                                                   #
#                      Polynomial functions                         #
#                                                                   #
#-------------------------------------------------------------------#


class BadPolynomialError(Exception):
    """Raised by polynomial routines when the polynomial is invalid.

    A valid polynomial is a list of coefficients like [1, 2, 1]

    The first (leading) coefficient must *not* be zero in a valid polynomial.
    """
    pass


def integer_roots(poly):
    # add code here!
    N=len(poly)
    if N==0:
        return []
    elif N==1:
        return []
    elif N==2:
        [a,b]=poly
        answer=[(0-b)/a]
        estimate=isinstance(answer,int)
        if estimate is True:
            return answer
        else:
            return []
    elif N==3:
        [a,b,c]=poly
        delta=b**2 - 4*a*c
        answer=[(-b+delta**0.5)/(2*a)] and answer=[(-b - delta**0.5)/(2*a)]
        estimate =isinstance(answer,int)
        if estimate is True:
            return answer
        else:
            return []
    
    elif N==4:
        [a,b,c,d]=poly
        u=[(9*a*b*c - 27*(a**2)*d - 2*b**3)/(52*a**3)]
        v=[((3*(4*a*c**3 - (b**2)*(c**2) - 18*a*b*c*d + 27*(a**2)*(d**2) + 4*(b**3)*d))**0.5)/(18*a**2)]
        if abs(u+v)>=abs(u-v):
            m=(u+v)**(1/3)
            if abs(m) !=0:
                n=((b**2)-3*a*c)/(9*a*m)
                answer=n + m - (b/(3*a))
                estimate = isinstance(answer,int)
                if estimate is True:
                    return answer
                else:
                    return[]
            else:
                n=0
                answer=n + m - (b/(3*a))
                estimate = isinstance(answer,int)
                if estimate is True:
                    return answer
                else:
                    return[]
                
        else:
            m=(u-v)**(1/3)
            if abs(m) !=0:
                n=((b**2)-3*a*c)/(9*a*m)
                answer=n + m - (b/(3*a))
                estimate = isinstance(answer,int)
                if estimate is True:
                    return answer
                else:
                    return[]
            else:
                n=0
                answer=n + m - (b/(3*a))
                estimate = isinstance(answer,int)
                if estimate is True:
                    return answer
                else:
                    return[]
        
    


def evaluate_polynomial(poly, xval):
    N=len(poly)
    """
    For example evaluate_polynomial([1, 2, 1], 3) 
    calculates p(3) where p(x) = x^2 + 2x + 1 
    return is 16

 """
     if N==0:
         return 0
     elif N==1:
         [a]=poly
         return a
     elif N==2:
         [a,b]=poly
         return a*xval + b
     elif N==3:
         [a,b,c]=poly
         return a*xval**2 + b*xval +c
         
    # add code here!


def is_root(poly, xval):
    """
   The is_root(p, x) function returns 
   True if x is a root of p(x)
   eg.
   >>> is_root([1, 2, 1], 3)
   False
   
   >>> is_root([1, 2, 1], -1)
   True
   
   This is because 33 is not a root of x^2 + 2x + 1
 It's easy to check if x is a root of p:
     we just calculate p(x) and see if it gives zero.
   
    """
    N=len(poly)
    if N==0:
        return True
    elif N==1:
        return False
    elif N==2:
        [a,b]=poly
        if xval*a + b==0:
            return True
        else:
            return False
    
    elif N==3:
        [a,b,c]=poly
        if a*xval**2 + b*xval + c ==0:
            return True
        else:
            return False
    
        
    
    
    # add code here!


#-------------------------------------------------------------------#
#                                                                   #
#                           Unit tests                              #
#                                                                   #
#-------------------------------------------------------------------#

#
# Run these tests with pytest:
#
#    $ pytest roots.py
#

def test_evaluate_polynomial():
    assert evaluate_polynomial([], 1) == 0
    assert evaluate_polynomial([1], 2) == 1
    assert evaluate_polynomial([1, 2], 3) == 5
    assert evaluate_polynomial([1, 2, 1], 4) == 25

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: evaluate_polynomial([0], 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial({}, 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial([[1]], 1))


def test_is_root():
    assert is_root([], 1) is True
    assert is_root([1], 1) is False
    assert is_root([1, 1], 1) is False
    assert is_root([1, 1], -1) is True
    assert is_root([1, -1], 1) is True
    assert is_root([1, -1], -1) is False
    assert is_root([1, -5, 6], 2) is True
    assert is_root([1, -5, 6], 3) is True
    assert is_root([1, -5, 6], 4) is False

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: is_root([0], 1))
    raises(BadPolynomialError, lambda: is_root({}, 1))
    raises(BadPolynomialError, lambda: is_root([[1]], 1))


def test_integer_roots():
    # In the case of the zero polynomial every value is a root but we return
    # the empty list because we can't list every possible value!
    assert integer_roots([]) == []
    assert integer_roots([1]) == []
    assert integer_roots([1, 1]) == [-1]
    assert integer_roots([2, 1]) == []
    assert integer_roots([1, -5, 6]) == [2, 3]
    assert integer_roots([1, 5, 6]) == [-3, -2]
    assert integer_roots([1, 2, 1]) == [-1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -3, -75, 475, -750]) == [-10, 3, 5]

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: integer_roots([0]))
    raises(BadPolynomialError, lambda: integer_roots({}))
    raises(BadPolynomialError, lambda: integer_roots([[1]]))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
    main(*arguments)
