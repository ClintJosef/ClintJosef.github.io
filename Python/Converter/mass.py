

class MassUnit:
    def __init__(self, value):
        self._value = value

    def as_centigram(self):
        return str(round(self._value * 100, 2)) + ' centigram'

    def as_gram(self):
        return str(self._value) + ' grams'

    def as_kilogram(self):
        return str(round(self._value / 1000, 2)) + ' kilogram'


class Gram(MassUnit):
    pass


class KiloGram(MassUnit):
    def __init__(self, value):
        super().__init__(value * 1000)



