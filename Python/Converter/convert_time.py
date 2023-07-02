class Time:
    # default being seconds (obviously)
    def __init__(self, value):
        self.value = value

    def as_nanosecond(self):
        return str(self.value * 10 ** 9) + ' nanoseconds'

    def as_microsecond(self):
        return str(self.value * 10 ** 6) + ' microseconds'

    def as_millisecond(self):
        return str(self.value * 1000) + ' milliseconds'

    def as_second(self):
        return str(self.value) + ' seconds'

    def as_minute(self):
        return str(self.value / 60) + ' minutes'

    def as_hour(self):
        return str(self.value / (60*60)) + ' hours'

    def as_day(self):
        return str(self.value / 86400) + ' days'

    def as_week(self):
        return str(self.value / 604800) + ' weeks'

    def as_month(self):
        return str(self.value / (2.628 * 10 ** 6)) + ' months'

    def as_year(self):
        return str(self.value / (3.154 * 10 ** 7)) + ' years'

    def as_decade(self):
        return str(self.value / (3.154 * 10 ** 8)) + ' decades'

    def as_century(self):
        return str(self.value / (3.154 * 10 ** 9)) + ' centuries'

    def as_millennium(self):
        return str(self.value / (3.154 * 10 ** 10)) + ' millennia'


class Nanosecond(Time):
    def __init__(self, value):
        super().__init__(value / 10 ** 9)


class Microsecond(Time):
    def __init__(self, value):
        super().__init__(value / 10 ** 6)


class Millisecond(Time):
    def __init__(self, value):
        super().__init__(value / 1000)


class Second(Time):
    pass


class Minute(Time):
    def __init__(self, value):
        super().__init__(value * 60)


class Hour(Time):
    def __init__(self, value):
        super().__init__(value * 60 ** 2)


class Day(Time):
    def __init__(self, value):
        super().__init__(value * 3600 * 24)


class Week(Time):
    def __init__(self, value):
        super().__init__(value * 86400)


class Month(Time):
    def __init__(self, value):
        super().__init__(value * 604800)


class Year(Time):
    def __init__(self, value):
        super().__init__(value * 2.628 * 10 ** 6)


class Decade(Time):
    def __init__(self, value):
        super().__init__(value * 3.154 * 10 ** 8)


class Century(Time):
    def __init__(self, value):
        super().__init__(value * 3.154 * 10 ** 9)


class Millennium(Time):
    def __init__(self, value):
        super().__init__(value * 3.154 * 10 ** 10)
