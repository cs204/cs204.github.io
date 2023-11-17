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


def sum(items):
    """
    Define to work on items other than numbers, which is not true for
    the built-in sum.
    """
    if len(items) == 0:
        return 0
    else:
        result = items[0]
        for item in items[1:]:
            result += item
    return result
