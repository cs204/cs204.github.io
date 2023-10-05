import sm
class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = '' # исправьте это
        pass
    def getNextValues(self, state, inp):
        pass


if __name__ == "__mina__":
    sm = Delay2Machine(100, 10)
    print(sm.transduce([1, 2, 10, 20, 30, 35]))
