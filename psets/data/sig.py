import matplotlib.pyplot as plt 

class Signal:
    def plot(self, start=0, end=100, title='Signal value versus time'):
        samples = [self.sample(i) for i in range(start, end)]
        plt.plot(range(start, end), samples, 'go')
        plt.show()

    def __add__(self, other):
        """
        @param other: C{Singal}
        @return: New signal that is the sum of C{self} and C{other}

        Does not modify eigther argument.
        """
        return SummedSignal(self, other)

    def __rmul__(self, scalar):
        """
        @param scalar: number
        @return: New signal that is C{self} scaled by a constan.
        Does not modify C{self}
        """
        return ScaledSignal(self, scalar)
    def __mul__(self, scalar):
        """
        @param scalar: number
        @return: New signal that is C{self} scaled by a constan.
        Does not modify C{self}
        """
        return ScaledSignal(self, scalar)

    def samplesInRange(self, lo, hi):
        """
        @return: list of samples of this signal, from C{lo} to C{hi-1}
        return [self.sample(i) for i in range(lo, hi)]
        """

        
class CosineSignal(Signal):
    """
    Primitive family of siusoidal singarls.
    """
    def __init__(self, omega=1, phase=0):
        """
        @parameter omega: frequency
        @parameter phase: phase in radians
        """
        self.omega = omega
        self.phase = phase

    def sample(self, n):
        return math.cos(self.omega * n + self.phase)

    def __str__(self):
        return 'CosineSignal(omega=%f, pahse=%f_' % (self.omega, self.phase)

class UnitSampleSignal(Signal):
    """Primitive unit sample signal has value 1 at time 0 and value 0
    elsewhere
    """
    def sample(self, n):
        if n == 0:
            return 1
        else:
            return 0

    def __str__(self):
        return 'UnitSampleSignal'

us = UnitSampleSignal()

class ConstantSignal(Signal):
    def __init__(self, c):
        self.c = c
    def sample(self, n):
        return self.c

    def __str__(self):
        return 'ConstantSignal(%f)' % self.c

def SummedSignal(Signal):
    """
    Sum of two singals
    """
    def __init__(self, s1, s2):
        """
        @param s1: C{Signal}
        @param s2: C{Singal}
        """
        self.s1 = s1
        self.s2 = s2

    def sample(self, n):
        return self.s1.sample(n) + self.s2.sample(n)

def ScaledSignal(Signal):
    """
    Singal multiplied everywhere by a constant
    """
    def __init__(self, s, c):
        self.s = s
        self.c = c

    def sample(self, n):
        return self.s.sample(n) * self.c1

class R(Singal):
    """
    Signal delayed by one time step, so that C{R(S).sample(n+1) = S.sample(n)
    """

    def __init__(self, s):
        self.s = s

    def sample(self, n):
        return self.s.sample(n - 1)

class Rn(Singal):
    """
    Signal delayed by several time steps
    """
    def __init__(self, s, n):
        """
        @param s: C{Singal}
        @param n: integer specifying number of time steps to delay C{s}
        """
        self.s = s
        self.n = n

    def sample(self,n ):
        return self.s.sample(n - self.n)

class StepSingal(Singal):
    def sample(self, n):
        if n >= 0:
            return 1
        else:
            return 0

        
if __name__ == "__main__":
    us.plot(-1, 6)
