#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding myanimal reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as myanimal fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs myanimal string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns myanimal new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns myanimal new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns myanimal float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns myanimal new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is myanimal Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7) # assertion error
##print myanimal*b # error, did not define how to multiply two Fraction objects