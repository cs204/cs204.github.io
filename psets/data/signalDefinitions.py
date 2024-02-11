"""
Реализация сигналов, графический вывод и комбинирование.
"""

import matplotlib.pyplot as plt 
import math



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
    Единичный импульс сигнал имеет значение 1 в момент 0 и 0  для других значений агруметна.
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
        return 'ConstantSignal(%f)'%(self.c)

###########################
# Здесь должен быть ваш код
###########################  

class StepSignal(Signal):
    """
    имеет значение 0 для аргумента меньшего 0 иначе 1.
    """
    pass

class SummedSignal(Signal):
    """ 
    Принимает два сигнала, s1 и s2, во время инициализации и создаёт новый сигнал, 
    который представляет собой сумму этих сигналов.  
    Обратите внимание, что этот класс должен быть ленивым: 
    при создании сигнала не должно происходить никаких сложений;
    сложение должно выполняться только когда вызывается sample SummedSignal.
    """
    pass

class ScaledSignal(Signal): 
    """
    принимает сигнал s и константу c во 
    время инициализации и создает новый сигнал, значения 
    sample которого представляют собой значения sample 
    исходного сигнала, умноженные на c. 
    """
    pass


class R(Signal): 
    """
    Принимает сигнал s во время инициализации и создаёт 
    новый сигнал, sample которого задерживаются на один 
    временной шаг; то есть значение нового сигнала в момент 
    времени n должно быть значением старого сигнала в 
    момент времени n - 1.
    """
    pass

class Rn(Signal):  
    """ 
    Принимает сигнал s во время инициализации и 
    создаёт новый сигнал, sample которого задерживаются 
    на n шагов.
    """
    pass

###########
# Проверка
###########
def test():
    print("[-1, 3]")
    s1 = StepSignal()

    print(f"StepSignal: {s1.samplesInRange(-1, 4)}")

    s2 = ScaledSignal(us, 2)
    print(f"ScaledSginal(StepSignal, 2): {s2.samplesInRange(-1, 4)}")

    s3 = R(us)
    print(f"R(us)): {s3.samplesInRange(-1, 4)}")

    s4 = SummedSignal(us, s3)
    print(f"SummedSignal(us, R(us)): {s4.samplesInRange(-1, 4)}")

    s5 = Rn(us, 2)
    print(f"Rn(us, 2): {s5.samplesInRange(-1, 4)}")

if __name__ == "__main__":
# Для проверки раскомментируйте строку ниже
    #test()
    pass
