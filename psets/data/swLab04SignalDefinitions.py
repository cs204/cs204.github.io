"""
Signals, represented implicitly, with plotting and combinations.
"""

import matplotlib.pyplot as plt 
import math



class Signal:
    """
    Represent infinite signals.  This is a generic superclass that
    provides some basic operations.  Every subclass must provide a
    C{sample} method.
    """
 

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
        """
        return [self.sample(i) for i in range(lo, hi)]

   
        

    def period(self, n = None, z = None):
        """
        @param n: number of samples to use to estimate the period;  if
        not provided, it will look for a C{length} attribute of C{self}
        @param z: zero value to use when looking for zero-crossings of
        the signal;  will use the mean by default.
        @return: an estimate of the period of the signal, or
        'aperiodic' if it can't get a good estimate
        """
        if n == None:
            n = self.length
        crossingsD = self.crossings(n, z)
        if len(crossingsD) < 2:
            return 'aperiodic'
        else:
            return listMean(gaps(crossingsD))*2

    def crossings(self, n = None, z = None):
        """
        @param n: number of samples to use;  if
        not provided, it will look for a C{length} attribute of C{self}
        @param z: zero value to use when looking for zero-crossings of
        the signal;  will use the mean by default.
        @return: a list of indices into the data where the signal crosses the
        z value, up through time n
        """
        if n == None: n = self.length
        if z == None: z = self.mean(n)
        samples = self.samplesInRange(0, n)
        return [i for i in range(n-1) if \
                   samples[i] > z and samples[i+1] < z or\
                   samples[i] < z and samples[i+1] > z]

    def mean(self, n = None):
        """
        @param n: number of samples to use to estimate the mean;  if
        not provided, it will look for a C{length} attribute of C{self}
        @return: sample mean of the values of the signal from 0 to n
        """
        if n == None: n = self.length
        return listMean(self.samplesInRange(0, n))

    

class CosineSignal(Signal):
    """
    Primitive family of sinusoidal signals.
    """
    def __init__(self, omega = 1, phase = 0):
        """
        @parameter omega: frequency
        @parameter phase: phase in radians
        """
        self.omega = omega
        self.phase = phase
    def sample(self, n):
        return math.cos(self.omega * n + self.phase)
    def __str__(self):
        return 'CosineSignal(omega=%f,phase=%f)'%(self.omega, self.phase)

class UnitSampleSignal(Signal):
    """
    Primitive unit sample signal has value 1 at time 0 and value 0
    elsewhere.
    """
    def sample(self, n):
        if n == 0:
            return 1
        else:
            return 0
    def __str__(self):
        return 'UnitSampleSignal'

us = UnitSampleSignal()
"""Unit sample signal instance"""

class ConstantSignal(Signal):
    """
    Primitive constant sample signal.
    """
    def __init__(self, c):
        """
        param c: value of signal at all times
        """
        self.c = c
    def sample(self, n):
        return self.c
    def __str__(self):
        return 'ConstantSignal(%f)'%(self.c)

################
# Your code here
################

