class SM:
    """
    Класс реализует абстрактный автомат. 
    Для создания подкласса автомата, надо задать
    методы:
    getNextValues: (state_t, inp_t) -> (state_t+1, out_t), 
    getNextState: (state_t, inp_t) -> state_t+1,
    done: state -> bool, значение по умолчанию False
    """
    startState = None

    def getNextValues(self, state, inp):
        """
        Версия метода по умолчанию, если
        подклсс задает только getNextState,
        то предполагаем, что вывод в момент t,
        такой же как состояние в момент t+1.
        """
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    def done(self, state):
        """
        По умолчанию, машина
        не останавливается
        """
        return False

    def isDone(self):
        return self.done(self.state)

    def start(self, verbose=False, printInput=True):
        """
        Вызываем перед отправкой ввода в автомате
        или для перезапуска.
        Устанавливает состояние автомата в начальное.
        Если verbose = True, то печатает описание 
        каждого шага.
        """
        self.__debugParams = DebugParams(verbose, printInput)
        self.state = self.startState

    def step(self, inp):
        """
        Выполняет один шаг автомата, 
        принимет inp, изменяет состояние, 
        выводит результат, ошибка, если done True
        """
        (s, o) = self.getNextValues(self.state, inp)
        if self.__debugParams.verbose:
            print(f"Step: {self.__debugParams.k}")
            self.printDebugInfo(0, self.state, s, inp, o, self.__debugParams)
            self.__debugParams.k += 1
        self.state = s
        return o

    def transduce(self, inps, verbose=False, printInput=True):
        """
        Переводит машину в начальное состояние.
        Берет список ввода, возвращает список выводов.
        """
        i = 0
        n = len(inps)
        result = []
        self.start(verbose=verbose, printInput=printInput)
        if verbose:
            print(f"Start state: {self.state}")
        while i < n and not self.isDone():
            result.append(self.step(inps[i]))
            i += 1
        return result

    def run(self, n = 10, verbose=False, printInput=True):
        """
        Для автоматов без входа, образованных с feedback.
        @params n: число шагов
        @result: список выводов
        """
        return self.transduce([None] * n, verbose=verbose, printInput=printInput)

    def guaranteeName(self):
        """
        Для уникальности имени
        """
        try: 
            self.name
        except AttributeError:
            self.name = gensym(self.__class__.__name__)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        """
        По умолчанию метод печати для премитивных машин
        """
        self.guaranteeName()
        if debugParams.verbose:
            if debugParams.printInput:
                print(' ' * depth, self.name, 'In:', inp, end=" ")
                print('Out:', out, end=" ")
                print('Next State:', nextState)
            else:
                print(' ' * depth, self.name, end=" ")
                print('Out:', out, end= " ")
                print('Next State:', nextState)



class Cascade(SM): 
    """ 
    Соединенеи двух машин. Выводи из первой - 
    ввод во вторую.  
    """
    def __init__(self, m1, m2, name=None):
        self.m1 = m1
        self.m2 = m2
        self.startState = (m1.startState, m2.startState)
        if not ((name is None or isinstance(name, str)) 
                and
                isinstance(m1, SM) and isinstance(m2, SM)):
            print(m1, m2, name)
            raise Exception("Cascade берет две машины как аргументы и опционоально имя новой машины.")
        self.name = name

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, o1)
        return ((newS1, newS2), o2)

    def done(self, state):
        (s1, s2) = state
        return self.m1.done(s1) or self.m2.done(s2)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            if debugParams.verbose:
                print(' ' * depth, self.name)
                (s1, s2) = state
                (ns1, ns2) = nextState
                (ns1, o1) = self.m1.getNextValues(s1, inp)
                self.m1.printDebugInfo(depth + 4, s1, ns1, inp, o1, debugParams)
                self.m2.printDebugInfo(depth + 4, s2, ns2, o1, out, debugParams)
                



class Parallel(SM):
    def __init__(self, m1, m2, name = None):
        self.m1 = m1
        self.m2 = m2
        self.name = name
        self.startState = (m1.startState, m2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))

    def done(self, state):
        (s1, s2) = state
        return self.m1.done(s1) or self.m2.done(s2)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            (s1, s2) = state
            (ns1, ns2) = nextState
            (o1, o2) = out
            if debugParams.verbose:
                print(' ' * depth, self.name)
                self.m1.printDebugInfo(depth + 4, s1, ns1, inp, o1, debugParams)
                self.m2.printDebugInfo(depth + 4, s2, ns2, inp, o2, debugParams)



class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValue(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            (s1, s2) = state
            (ns1, ns2) = nextState
            (i1, i2) = splitValue(inp)
            (o1, o2) = out
            if debugParams.verbose:
                print(' ' * depth, self.name)
                self.m1.printDebugInfo(depth + 4, s1, ns1, i1, o1, debugParams)
                self.m2.printDebugInfo(depth + 4, s2, ns2, i2, o2, debugParams)


class Feedback(SM):
    def __init__(self, m, name = None):
        self.m = m
        self.name = name
        self.startState = self.m.startState

    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS, ignore) = self.m.getNextValues(state, o)
        return (newS, o)

    def done(self, state):
        return self.m.done(state)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        (machineState, lastOutput) = self.getNextValues(state, inp)
        self.guaranteeName()
        if debugParams.verbose:
            print(' ' * depth, self.name)
            self.m.printDebugInfo(depth + 4, state, nextState, lastOutput, out, debugParams)
    

class Feedback2(Feedback):
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, (inp, 'undefined'))
        (newS, ignore) = self.m.getNextValues(state, (inp, o))
        return (newS, o)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        (machineState, lastOutput) = self.getNextValues(state, (inp, 'undefined'))
        self.guaranteeName()
        if debugParams.verbose:
            print(' ' * depth, self.name)
            self.m.printDebugInfo(depth + 4, state, nextState, (inp, lastOutput) , out, debugParams)


class Switch(SM):
    """
    заданной condition (для ввода вычисляет логическое значение),
    и пары автоматов создаём новую машину. 
    condition вычисляется на каждом шагу и выбранная машина используется для
    вывода и её состояние меняется.
    """
    def __init__(self, condition, m1, m2, name = None):
        self.m1 = m1
        self.m2 = m2
        self.condition = condition
        self.name = name
        self.startState = (self.m1.startState, self.m2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        if self.condition(inp):
            (ns1, o) = self.m1.getNextValues(s1, inp)
            return ((ns1, s2), o)
        else:
            (ns2, o) = self.m2.getNextValues(s2, inp)
            return ((s1, ns2), o)

    def done(self, state):
        (s1, s2) = state
        return self.m1.done(s1) or self.m2.done(s2)


    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            (s1, s2) = state
            (ns1, ns2) = nextState
            if self.condition(inp):
                machineRunning = 'M1'
            else:
                machineRunning = 'M2'
            if debugParams.verbose:
                print(' ' * depth, self.name, 'Running', machineRunning)
            if machineRunning == 'M1':
                self.m1.printDebugInfo(depth + 4, s1, ns1, inp, out, debugParams)
            else:
                self.m2.printDebugInfo(depth + 4, s2, ns2, inp, out, debugParams)


class Mux(Switch):
    """
    Как Switch, но изменяются состояния обоих машин
    """
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ns1, o1) = self.m1.getNextValues(s1, inp)
        (ns2, o2) = self.m2.getNextValues(s2, inp)
        if self.condition(inp):
            return ((ns1, ns2), o1)
        else:
            return ((ns1, ns2), o2)


class Repeat(SM):
    """
    Дан автомат, создает новый автомат,
    который будет выполнять его n раз. Если n
    не заданно, то будет выполнять вечно.
    """
    def __init__(self, m, n = None, name = None):
        self.m = m
        self.startState = (0, self.m.startState)
        self.n = n
        self.name = name

    def advanceIfDone(self, counter, mState):
        while self.m.done(mState) and not self.done((counter, mState)):
            counter += 1
            mState = self.m.startState
        return (counter, mState)

    def getNextValues(self, state, inp):
        (counter, mState) = state
        (mState, o) = self.m.getNextValues(mState, inp)
        (counter, mState) = self.advanceIfDone(counter, mState)
        return ((counter, mState), o)

    def done(self, state):
        (counter, mState) = state
        return not self.n == None and counter == self.n

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            (counter, mState) = state
            (ncounter, nmState) = nextState
            if debugParams.verbose:
                print(' ' * depth, self.name, 'Counter =', counter) 
            self.m.printDebugInfo(depth + 4, mState, nmState, inp, out, debugParams)



class Sequence(SM):
    def __init__(self, smList, name = None):
        self.smList = smList
        self.name = name
        self.startState = (0, self.smList[0].startState)
        self.n = len(smList)

    def advanceIfDone(self, counter, smState):
        while self.smList[counter].done(smState) and counter + 1 < self.n:
            counter = counter + 1 
            smState = self.smList[counter].startState
        return (counter, smState)

    def getNextValues(self, state, inp):
        (counter, smState) = state
        (smState, o) = self.smList[counter].getNextValues(smState, inp)
        (counter, smState) = self.advanceIfDone(counter, smState)
        return ((counter, smState), o)

    def done(self, state):
        (counter, smState) = state
        return self.smList[counter].done(smState)

    def printDebugInfo(self, depth, state, nextState, inp, out, debugParams):
        if nextState and len(nextState) == 2:
            self.guaranteeName()
            (counter, smState) = state
            (ncounter, nsmState) = nextState
            if debugParams.verbose:
                print(" " * depth, self.name, 'Counter =', counter)
            self.smList[counter].printDebugInfo(depth + 4, smState, nsmState, inp, out, debugParams)
    

class R(SM):
    """
    Вывод в момент t равен вводу в момент t-1.
    """

    def __init__(self, v0=0, name = None):
        """
        @param v0: initial output value
        """
        self.startState = v0
        self.name = name

    def getNextValues(self, state, inp):
        return (inp, state)


Delay = R


class Wire(SM):
    """
    Автомат, его вывод равен вводу без задрежки.
    """
    def getNextState(self, state, inp):
        return inp

class Const(SM):
    """
    Автомат, вывод из которого постоянный
    """
    def __init__(self, c):
        self.c = c
    def getNextState(self, state, inp):
        return self.c





class DebugParams:
    def __init__(self, verbose, printInput):
        self.verbose = verbose
        self.printInput = printInput
        self.k = 0




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

def splitValue(v, n = 2):
    if v == 'undefined':
        return ['undefined'] * n 
    else:
        return v


class SymbolGenerator:
    """
    Генерирует символы отличные от других
    """

    def __init__(self):
        self.count = 0


    def gensym(self, prefix="i"):
        self.count += 1
        return prefix + "_" + str(self.count)


gensym = SymbolGenerator().gensym


