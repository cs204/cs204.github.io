"""
Polynomials with addition, subtraction, multiplication, and roots.
"""
import numpy

class Polynomial:
    """
    Represent polynomials, and supports addition, substraction, multiplitcation 
    root finding
    """
    def __init__(self, c):
        """
        @param c: a list of numbers, starting with highest
        order coefficient.
        """
        self.coeffs = tuple(float(i) if not isinstance(i, complex) else i for i in c)
        while len(self.coeffs) > 0 and self.coeffs[0] == 0:
            self.coeffs = self.coeffs[1:]
        self.order = len(self.coeffs) - 1

    def coeff(self, i):
        """
        @return: the coefficient associated with the C{x**i} term
        """
        if 0 <= i <= self.order:
            return self.coeffs[self.order - i]
        else:
            return 0.0

    def val(self, v):
        """
        @param v: number
        @return: the value of the polynomial with the variable assigned to x.
        """
        return sum([ self.coeff(i) * v**i for i in range(self.order + 1)])

    def add(self, other):
        """
        @param other: the instance of L{Polynomial} which we want to add to C{self}
        @return: a new isntance of L{Polynomial}, wich is the sum of C{self} and C{other}.
        Does not affect either input.
        """
        c1 = [self.coeff(i) for i in range(self.order + 1)]
        c2 = [other.coeff(i) for i in range(other.order + 1)]
        while len(c1) < len(c2):
            c1.append(0)
        while len(c2) < len(c1):
            c2.append(0)
        return Polynomial([c1[i] + c2[i] for i in range(len(c1) - 1, -1, -1)])

    def mul(self, other):
        """
        @param other: the instance of L{Polynomial} by which we want to multiply
        @return: a new instance of L{Polynomial}, which is the product of C{slef} and C{other}
        Does not affect either input.
        """
        out = Polynomial([])
        c1 = [self.coeff(i) for i in range(self.order + 1)]
        for i in range(other.order + 1):
            m = other.coeff(i)
            coeffs = [m * j for j in [0] * i + c1]
            p = Polynomial(coeffs[::-1])
            out = out + p
        return out

    def sub(self, other):
        return self + Polynomail([-1.0 * other.coeff(i) for i in range(other.order - 1, -1, -1)])

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)

    def __repr__(self):
        coeffs = [self.coeff(i) for i in range(self.order, -1, -1)]
        return 'Polynomail([%s])'%(', ').join(repr(i) for i in coeffs)

    def __str__(self):
        out = ''
        for i in range(self.order, -1, -1):
            c = self.coeff(i)
            if c == 0:
                continue
            if c.real >= 0 and len(out) != 0:
                out += ' + '
            elif len(out) != 0:
                out += ' - '
                c = -c
            if c != 1:
                out += '(%r)' % c
            elif c == 1 and i == 0:
                out += repr(c)
            if i == 1:
                out += 'x'
            elif i != 0:
                out += '(x^%d)' % i

        return out

    def roots(self):
        """
        @return list of the roots of the polynonial
        """
        return numpy.roots(self.coeffs).tolist()


        
p1 = Polynomial([1, 0, -4])
print(p1.roots())
