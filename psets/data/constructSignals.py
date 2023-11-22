import signalDefinitions as sign
import poly

#Вам может понадобится следующая функция суммирования
def sum(l):
    """
    @param l: список 
    @return: сумма элементов списка
    """
    if len(l) == 0:
        return 0
    res = l[0]
    for elem in l[1:]:
        res += elem
    return res


def polyR(s, p):
    """
    @param s:  экземпляр класса Signal, 
    @param p:  экземпляр класса Polynomial, 
    @return: новый экземпляр класса Singal, который получен из сигнала  s, преобразованного  полиномом по R 
    """
    #ваш код
    pass

#step1: сигнал равен 3.0 для и 0 для других 
step1 =  None #Ваш код

#step2: сигнал равен -3.0 для t > 7 и 0 для других t.
step2 =  None #Ваш код

#stepUpDown: сигнал равен 3.0 для 3 <= t <= 6 и 0 для других t 
stepUpDown = None #Ваш код

#stepUpDownPoly: используйте polyR, чтобы построить сигнал, который имеет 
#значение 1.0 в t = 1, значение 3 в t = 3, 5 для t = 5 и 0 для остальных.
stepUpDownPoly = None #Ваш код

def test():
    print("step1:")
    print(list(range(0, 5)))
    print(step1.samplesInRange(0, 5))

    print("step2:")
    print(list(range(0, 9)))
    print(step2.samplesInRange(0, 9))

    print("stepUpDown:")
    print(list(range(0, 9)))
    print(stepUpDown.samplesInRange(0, 9))

    print("stepUpDownPoly:")
    print(list(range(0, 9)))
    print(stepUpDownPoly.samplesInRange(0, 9))




if __name__ == "__main__":
    #Для проверки раскомментируйте строку ниже 
    pass
    #test()
