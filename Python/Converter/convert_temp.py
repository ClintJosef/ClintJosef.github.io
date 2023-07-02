class Temp_Unit:
    # default measurement being celsius
    def __init__(self, value):
        self._value = value

    def as_celsius(self):
        return str(self._value) + " degrees celsius"

    def as_fahrenheit(self):
        return str(round(self._value * 1.8 + 32, 2)) + " degrees fahrenheit"

    def as_kelvin(self):
        return str(round(self._value + 273.15, 2)) + " degrees kelvin"


class Celsius(Temp_Unit):
    pass


class Fahrenheit(Temp_Unit):
    def __init__(self, value):
        super().__init__((value-32) / 1.8)


class Kelvin(Temp_Unit):
    def __init__(self, value):
        super().__init__(value - 273.15)
