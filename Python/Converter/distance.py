class Distance:
    def __init__(self, value):
        self._value = value

    def as_centimeter(self):
        return str(round(self._value * 100, 2)) + ' centimeters'

    def as_meter(self):
        return str(round(self._value, 2)) + ' meters'

    def as_kilometer(self):
        return str(round(self._value / 1000, 2)) + ' kilometers'

    def as_nanometer(self):
        return str(round(self._value * 10**9, 2)) + ' nanometers'

    def as_feet(self):
        return str(round(self._value * 3.28084, 2)) + ' feet'


class Meter(Distance):
    pass


class Mile(Distance):
    def __init__(self, value):
        super().__init__(value * 1609.344)


class CentiMeter(Distance):
    def __init__(self, value):
        super().__init__(value / 100)



