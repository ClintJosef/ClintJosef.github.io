class Length:
    # default being meters
    def __init__(self, value):
        self.value = value

    def as_centimeter(self):
        return str(self.value * 100) + ' centimeters'

    def as_meter(self):
        return str(self.value) + ' meters'

    def as_kilometer(self):
        return str(self.value / 1000) + ' kilometers'

    def as_millimeter(self):
        return str(self.value * 1000) + ' millimeters'

    def as_micrometer(self):
        return str(self.value * 10 ** 6) + ' micrometers'

    def as_nanometer(self):
        return str(self.value * 10 ** 9) + ' nanometers'

    def as_foot(self):
        return str(self.value * 3.28084) + ' feet'

    def as_yard(self):
        return str(self.value * 1.094) + ' yards'

    def as_inch(self):
        return str(self.value * 39.37) + 'inches'

    def as_mile(self):
        return str(self.value / 1609) + ' miles'

    def as_nmile(self):
        return str(self.value / 1852) + ' nautical miles'


class Centimeter(Length):
    def __init__(self, value):
        super().__init__(value / 100)


class Meter(Length):
    pass


class Kilometer(Length):
    def __init__(self, value):
        super().__init__(value * 1000)


class Millimeter(Length):
    def __init__(self, value):
        super().__init__(value / 1000)


class Micrometer(Length):
    def __init__(self, value):
        super().__init__(value / 10 ** 6)


class Nanometer(Length):
    def __init__(self, value):
        super().__init__(value / 10 ** 9)


class Foot(Length):
    def __init__(self, value):
        super().__init__(value / 3.281)


class Yard(Length):
    def __init__(self, value):
        super().__init__(value / 1.094)


class Inch(Length):
    def __init__(self, value):
        super().__init__(value / 39.37)


class Mile(Length):
    def __init__(self, value):
        super().__init__(value * 1609.344)


class Nmile(Length):
    def __init__(self, value):
        super().__init__(value * 1852)
