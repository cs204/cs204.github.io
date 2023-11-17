"""
Реализация сигналов, графический вывод и комбинирование.
"""

import matplotlib.pyplot as plt 
import utils

class Signal:
    """
    Реализация бесконечных сигналов. Это базовый класс он
    представляет некоторые общие операции. Каждый подкласс должен
    задавать C{sample} метод.
    """
 
    def plot(self, start=0, end=100, title='Signal value versus time'):
        samples = [self.sample(i) for i in range(start, end)]
        plt.plot(range(start, end), samples, 'go')
        plt.show()

    def __add__(self, other):
        """
        @param other: C{Singal}
        @return: новый сигнал сумма C{self} и C{other}
        Не изменяет аргументы.
        """
        return SummedSignal(self, other)

    def __rmul__(self, scalar):
        """
        @param scalar: number
        @return: Новый сигнал, который  C{self} умноженный на константу.
        Не изменяет C{self}
        """
        return ScaledSignal(self, scalar)

    def __mul__(self, scalar):
        """
        @param scalar: number
        @return: Новый сигнал, который  C{self} умноженный на константу.
        Не изменяет C{self}
        """
        return ScaledSignal(self, scalar)

    def samplesInRange(self, lo, hi):
        """
        @return: list значений сигнала, от C{lo} до C{hi-1}
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
    Семейство синусоидальных сигналов.
    """
    def __init__(self, omega = 1, phase = 0):
        """
        @parameter omega: частота
        @parameter phase: фаза в радианах 
        """
        self.omega = omega
        self.phase = phase
    def sample(self, n):
        return math.cos(self.omega * n + self.phase)
    def __str__(self):
        return 'CosineSignal(omega=%f,phase=%f)'%(self.omega, self.phase)


class UnitSampleSignal(Signal):
    """
    Единичный импульс сигнал имеет значение 1 в момент 0 и 0  для других значений аргумента.
    """
    def sample(self, n):
        if n == 0:
            return 1
        else:
            return 0

    def __str__(self):
        return 'UnitSampleSignal'

us = UnitSampleSignal()
"""Экземпляр единичного импульса """

class ConstantSignal(Signal):
    """
    Постоянный сигнал.
    """
    def __init__(self, c):
        """
        param c: значение сигнала для всех значений аргумента
        """
        self.c = c

    def sample(self, n):
        return self.c

    def __str__(self):
        return 'ConstantSignal(%f)' % self.c

def SummedSignal(Signal):
    """ 
    Принимает два сигнала, s1 и s2, во время инициализации и создаёт новый сигнал, 
    который представляет собой сумму этих сигналов.  
    Обратите внимание, что этот класс должен быть ленивым: 
    при создании сигнала не должно происходить никаких сложений;
    сложение должно выполняться только когда вызывается sample SummedSignal.
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
    принимает сигнал s и константу c во 
    время инициализации и создает новый сигнал, значения 
    sample которого представляют собой значения sample 
    исходного сигнала, умноженные на c. 
    """
    def __init__(self, s, c):
        self.s = s
        self.c = c

    def sample(self, n):
        return self.s.sample(n) * self.c

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
    """
    имеет значение 0 для аргумента меньшего 0 иначе 1.
    """
    def sample(self, n):
        if n >= 0:
            return 1
        else:
            return 0

def polyR(s, p):
    """
    @param s: C{Signal}
    @param p: C{poly.Polynomial}
    @return: New signal that is C{s} transformed by C{p} interpreted
    as a polynomial in I{R}.
    """
    return util.sum([ c * Rn(s, k) for c, k in zip(p.coeffs, range(p.order, -1, -1))
                    ])


