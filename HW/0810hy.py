import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add_(self, other):
        return complex(self.real + other.real,
                       self.imaginary + other.imaginary)
    def __sub__(self, other):
        return complex(self.real - other.real,
                       self.imaginary - other.imaginary)
    def __mul__(self, other):
        return complex(self.real*other.real - self.imaginary*other.imaginary,
                       self.imaginary*other.real + self.real*other.imaginary)
    def __div__(self, other):
        return complex ((self.real*other.real + self.imaginary*other.imaginary)/(other.real**2 - other.imaginary**2),
                        (self.imaginary*other.real - self.real*other.imaginary)/(other.real**2 - other.imaginary**2))        
    def mod(self, other):
        value = complex(self.real**2-self.imaginary**2, 0)
        return math.sqrt(value)

    def __str__(self):
        if self.imaginary == 0:
            result =  "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "%.2f+%.2fi" %self.real, abs(self.imaginary)
         return result