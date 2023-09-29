class SM:
    startState = None

    def start(self):
        self.state = self.startState

    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def done(self, state):
        return False

    def transduce(self, inputs, verbose = False):
        self.start()
        if verbose:
            print(f"Start state: {self.state}")
        outputs = []
        for inp in inputs:
            if self.done(self.state):
                break
            o = self.step(inp)
            outputs.append(o)
            if verbose:
                print(f"In: {inp} Out: {o} NextState: {self.state}")
        if verbose:
            print(outputs)
        return outputs

    def run(self, n = 10, verbose = False):
        self.start()
        if verbose:
            print(f"Start state: {self.state}")
        outputs = []
        for l in range(n):
            o = self.step('undefined')
            outputs.append(o)
        return outputs

class Cascade(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, o1)
        return ((newS1, newS2), o2)



class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))

class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValue(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))

class ParallelAdd(Parallel):
    def getNextState(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1 + o2)


class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState

    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS, ignore) = self.m.getNextValues(state, o)
        return (newS, o)

class Feedback2(Feedback):
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS, ignore) = self.m.getNextValues(state, (inp, o))
        return (newS, o)


class Delay(SM):
    def __init__(self, v0):
        self.startState = v0

    def getNextValues(self, state, inp):
        return (inp, state)

class Increment(SM):
    def __init__(self, incr):
        self.incr = incr

    def getNextState(self, state, inp):
        return safeAdd(inp, self.incr)


class Adder(SM):
    def getNextState(self, state, inp):
        (i1, i2) = splitValue(inp)
        return safeAdd(i1, i2)

class Multiplier(SM):
    def getNextState(self, state, inp):
        (i1, i2) = splitValue(inp)
        return safeMul(i1, i2)

class Switch(SM):
    def __init__(self, condition, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.condition = condition
        self.startState = (self.m1.startState, 
                           self.m2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        if self.condition(inp):
            (ns1, o) = self.m1.getNextValues(s1, inp)
            return ((ns1, s2), o)
        else:
            (ns2, o) = self.m2.getNextValues(s2, inp)
            return ((s1, ns2), o)

class Mux(Switch):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ns1, o1) = self.m1.getNextValues(s1, inp)
        (ns2, o2) = self.m2.getNextValues(s2, inp)
        if self.condition(inp):
            return ((ns1, ns2), o1)
        else:
            return ((ns1, ns2), o2)

class If(SM):
    startState = ('start', None)
    def __init__(self, condition, sm1, sm2):
        self.sm1 = sm1
        self.sm2 = sm2
        self.condition = condition

    def getFirstRealState(self, inp):
        if self.condition(inp):
            return ('runningM1', self.sm1.startState)
        else:
            return ('runningM2', self.sm2.startState)

    def getNextValues(self, state, inp):
        (ifState, smState) = state
        if ifState == 'start':
            (ifState, smState) = self.getFirstRealState(inp)
        if ifState == 'runningM1':
            (newS, o) = self.sm1.getNextValues(smState, inp)
            return (('runningM1', newS), o)
        else:
            (newS, o) = self.sm2.getNextValues(smState, inp)
            return (('runningM2', newS), o)

        
class Accumulator(SM):
    def __init__(self, initialValue):
        self.startState = initialValue 

    def getNextState(self, state, inp):
        return state + inp


def splitValue(v):
    if v == 'undefined':
        return ('undefined', 'undefined')
    else:
        return v

def safeAdd(a, b):
    if a == 'undefined' or b == 'undefined':
        return 'undefined'
    else:
        return a + b

def safeMul(a, b):
    if a == 'undefined' or b == 'undefined':
        return 'undefined'
    else:
        return a * b
