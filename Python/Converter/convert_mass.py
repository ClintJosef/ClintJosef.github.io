class Mass:
    # default being grams
    def __init__(self, value):
        self.value = value

    def as_kg(self):
        return str(self.value / 1000) + ' kilograms'

    def as_ton(self):
        return str(self.value / 10 ** 6) + ' kilograms'

    def as_gram(self):
        return str(self.value) + ' grams'

    def as_milligram(self):
        return str(self.value * 1000) + ' milligrams'

    def as_microgram(self):
        return str(self.value * 10 ** 6) + ' micrograms'

    def as_im_ton(self):
        return str(self.value / 1.016 * 10 ** 6) + ' imperial tons'

    def as_us_ton(self):
        return str(self.value / 907185) + ' US tons'

    def as_pound(self):
        return str(self.value / 454) + ' pounds'

    def as_ounce(self):
        return str(self.value / 28.35) + ' ounces'

    def as_stone(self):
        return str(self.value / 6350) + ' stones'


class Kilogram(Mass):
    def __init__(self, value):
        super().__init__(value * 1000)


class Ton(Mass):
    def __int__(self, value):
        super().__init__(value * 10 ** 6)


class Gram(Mass):
    pass


class Milligram(Mass):
    def __int__(self, value):
        super().__init__(value / 1000)


class Microgram(Mass):
    def __init__(self, value):
        super().__init__(value / 10 ** 6)


class Im_Ton(Mass):
    def __init__(self, value):
        super().__init__(value * 1.016 * 10 ** 6)


class Us_Ton(Mass):
    def __init__(self, value):
        super().__init__(value * 907185)


class Pound(Mass):
    def __init__(self, value):
        super().__init__(value * 454)


class Ounce(Mass):
    def __init__(self, value):
        super().__init__(value * 28.35)


class Stone(Mass):
    def __init__(self, value):
        super().__init__(value * 6350)
