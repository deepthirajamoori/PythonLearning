import math
class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real+other.real,self.imag+other.imag)
    def __sub__(self, other):
        return Complex(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z)
    def dot(self,other):
        return Complex(self.x*other.x,self.y*other.y,self.z*other)
    def cross(self,other):
        return Points((self.y * no.z - self.z * no.y), (self.z * no.x - self.x * no.z), (self.x * no.y - self.y * no.x))
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__'
    complex = list()
    for i in range(4):
        a = list(map(float,input().split()))
        complex.append(a)
    a,b,c,d = Complex(*points)