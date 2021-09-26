class Foo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(self.real)+"+"+str(self.imag)+"i"
    
    def __mul__(self, other):
        if type(other) == int:
            newreal = self.real * other
            newimag = self.imag * other

        elif type(other) == Foo:
            newreal =self.real * other.real - other.imag * self. imag
            newimag = self.real * other.imag + self.imag * other.real

        elif type(other) == float:
            newreal = self.real * other
            newimag = self.imag * other
        
        elif type(other)== complex:
            newreal =self.real * other.real - other.imag * self. imag
            newimag = self.real * other.imag + self.imag * other.real

        
        else:
            newreal = self.real
            newimag = self.imag

        return Foo(newreal, newimag)

    def __add__(self, other):
        if type(other) == int:
            newreal = self.real + other

        elif type(other) == Foo:
            newreal = self.real +other.real
            newimag = self.imag + other. imag

        elif type(other) == complex:
            newreal = self.real +other.real
            newimag = self.imag + other. imag
            
        elif type(other) == float:
            newreal = self.real + other
        
        else:
            newreal = self.real
            newimag = self.imag
        
        return Foo(newreal, newimag)

    def __sub__(self, other):
        if type(other) == int:
            newreal = self.real - other

        elif type(other) == Foo:
            newreal = self.real - other.real
            newimag = self.imag - other. imag
            
        elif type(other) == float:
            newreal = self.real - other
        
        else:
            newreal = self.real
            newimag = self.imag

        return Foo(newreal, newimag)
    
    def __div__(self, other):
        return Foo(self.real, self.imag)



a = Foo(1,2)
print()
b = complex(2,3)
print(b)
print(a*b)