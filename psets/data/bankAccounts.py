import sm
class PureFunction(sm.SM):
    def __init__(self, f):
        pass

    def getNextValues(self, state, inp):
        pass

class BA1(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        if inp != 0:
            newState = state * 1.02 + inp - 100
        else:
            newState = state * 1.02
        return (newState, newState)


class BA2(sm.SM):
    startState = 0 
    def getNextValues(self, state, inp):
        newState = state * 1.01 + inp
        return (newState, newState)

ba1 = BA1()
ba2 = BA2()
maxAccount = None # здесь вам надо задать комбинацию машин 
print(maxAccount.transduce([300, 200, 3000]))
