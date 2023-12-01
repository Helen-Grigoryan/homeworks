def gcd(a,b):
    while a % b != 0:
        c = a
        a = b
        b = c % b
    return b

class Rational:
    def __init__(self,nominator, denominator):
        self.__nominator = nominator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise Exception("Denominator should not be 0")
        
    def __add__(self, rhs):
        denominator = self.__denominator * rhs.__denominator
        nominator = self.__nominator + rhs.__nominator
        g = gcd(nominator, denominator)
        nominator = nominator // g
        denominator = denominator // g
        result = Rational(nominator,denominator)
        return result
    
    def __sub__(self, rhs):
        denominator = self.__denominator * rhs.__denominator
        nominator = self.__nominator - rhs.__nominator
        g = gcd(nominator, denominator)
        nominator = nominator // g
        denominator = denominator // g
        result = Rational(nominator,denominator)
        return result

    def __mul__(self, rhs):
        denominator = self.__denominator * rhs.__denominator
        nominator = self.__nominator * rhs.__nominator
        g = gcd(nominator,denominator)
        denominator = denominator // g
        nominator = nominator // g
        result = Rational(nominator,denominator)
        return result
    
    def __div__(self, rhs):
        nominator = self.__nominator * rhs.__denominator
        denominator = self.__denominator * rhs.__nominator
        g = gcd(nominator,denominator)
        denominator = denominator // g
        nominator = nominator // g
        result = Rational(nominator,denominator)
        return result

    def __str__(self):
        str = f"{self.__nominator} / {self.__denominator}"
        return str




    
