class Speed:
    # default being mph
    def __init__(self, value):
        self._value = value

    def as_mph(self):
        return str(self._value) + ' miles per hour'

    def as_mps(self):
        return str(self._value / 2.237) + ' meters per second'

    def as_fps(self):
        return str(self._value * 14.67) + ' feet per second'

    def as_kph(self):
        return str(self._value * 1.609) + ' kilometers per hour'

    def as_knot(self):
        return str(self._value / 1.151) + ' knots'


class Mph(Speed):
    pass


class Mps(Speed):
    def __init__(self, value):
        super().__init__(value * 2.237)


class Fps(Speed):
    def __init__(self, value):
        super().__init__(value / 1.467)


class Kph(Speed):
    def __init__(self, value):
        super().__init__(value / 1.609)


class Knot(Speed):
    def __init__(self, value):
        super().__init__(value * 1.151)
