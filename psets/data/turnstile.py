import sm
class Turnstile(sm.SM):
    startState = 'locked'
    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return (Q1, Q2)
            else:
                return (Q3, Q4)
        else:
            if inp == 'turn':
                return (Q5, Q6)
            else:
                return (Q7, Q8)

if __name__ == "__main__":
    t = Turnstile()
    print(t.transduce(['coin', 'turn', 'coin']))


