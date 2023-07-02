

class Second:
    def __init__(self, value):
        self._value = value

    def as_nanoseconds(self):
        return str(self._value * 10**9) + " nanoseconds"

    def as_microseconds(self):
        return str(self._value * 10**6) + " microsecond"

    def as_milliseconds(self):
        return str(self._value * 10**3) + " millisecond"

    def as_seconds(self):
        return str(self._value) + " seconds"

    def as_minutes(self):
        return str(round(self._value / 60, 2)) + " minutes"

    def as_hours(self):
        return str(round(self._value / 3600, 2)) + " hours"

    def as_days(self):
        return str(round(self._value / (3600 * 24), 2)) + " days"

    def as_week(self):
        return str(round(self._value / (3600 * 24 * 7), 2)) + " days"

    def as_month(self):
        return str(round(self._value / (3600 * 24 * 7 * 30), 2)) + " months"

    def as_year(self):
        pass

    def as_decade(self):
        pass

    def as_century(self):
        pass

    def as_millennium(self):
        pass


class NanoSecond(Second):
    def __init__(self, value):
        value = value * 10**-9
        super().__init__(value)


class MicroSecond(Second):
    def __init__(self, value):
        super().__init__(value*(10**-6))


class MilliSecond(Second):
    def __init__(self, value):
        super().__init__(value*(10**-3))


class Minute(Second):
    def __init__(self, value):
        super().__init__(value*60)


class Hour(Second):
    def __init__(self, value):
        super().__init__(value*3600*24)


class Day(Second):
    def __init__(self, value):
        super().__init__(value*3600*24*7)


class Month(Second):
    def __init__(self, value):
        super().__init__(value*3600*24*7*30)
