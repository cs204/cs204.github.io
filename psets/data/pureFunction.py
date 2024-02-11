import sm

class PureFunction(sm.SM): 
    def __init__(self, f): 
        pass

    def getNextValues(self, state, inp): 
        pass 


if __name__ == "__main__": 
    pf = PureFunction(lambda x: 2 * x) 
    print(pf.transduce([2, 3, 4, 5]))


