class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor called: Complex Number ({self.real} + {self.imag}i) created")

    def __del__(self):
        print(f"Destructor called: Complex Number ({self.real} + {self.imag}i) destroyed")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


# ---- Demo ----
c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 4)

print("C1 =", c1)
print("C2 =", c2)

c3 = c1 + c2
print("C1 + C2 =", c3)

c4 = c1 - c2
print("C1 - C2 =", c4)