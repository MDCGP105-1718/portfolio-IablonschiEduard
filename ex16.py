class Fraction(object):
    def __init__(self,num,denom):
        self.num=num;
        self.denom=denom;

    def __add__(self):
        return Fraction(self.num + self.denom)
    def __sub__(self):
        return Fraction(self.num - self.denom)
    def multiplication(self):
        return Fraction(self.num * self.denom)
    def division(self):
        return Fraction(self.num / self.denom)
    def inverse(self, x):
        x = self.num
        self.num = self.denom
        self.denom = x
        return Fraction(self.num, self.denom)
    
