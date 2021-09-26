 
class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def get_float(self):
        return self.num/self.den
    
    def __truediv__(self, other):
        return Rational(self.num, self.div)