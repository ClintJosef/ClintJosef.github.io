class Pressure:
    # default being bar
    def __init__(self, value):
        self.value = value

    def as_bar(self):
        return str(self.value) + ' bars'

    def as_psi(self):
        return str(self.value * 14.504) + ' psi'

    def as_pascal(self):
        return str(self.value * 10 ** 5) + ' pascals'

    def as_atmosphere(self):
        return str(self.value / 1.013) + ' atmospheres'

    def as_torr(self):
        return str(self.value * 750) + ' torrs'


class Bar(Pressure):
    pass


class Psi(Pressure):
    def __init__(self, value):
        super().__init__(value / 14.5038)


class Pascal(Pressure):
    def __init__(self, value):
        super().__init__(value / 10 ** 5)


class Atmosphere(Pressure):
    def __init__(self, value):
        super().__init__(value * 1.01325)


class Torr(Pressure):
    def __init__(self, value):
        super().__init__(value / 750.062)
