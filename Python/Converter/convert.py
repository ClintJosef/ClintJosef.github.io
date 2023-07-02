class converter:
    def __init__(self, num):
        self.num = float(num)


# class temp:
#     class temp_fahrenheit(converter):
#         def fahrenheit_celsius(self):
#             return (self.num - 32) / 1.8
#
#         def fahrenheit_kelvin(self):
#             return (self.num - 32) * 5 / 9 + 273.15
#
#     class temp_celsius(converter):
#         def celsius_fahrenheit(self):
#             return self.num * 1.8 + 32
#
#         def celsius_kelvin(self):
#             return self.num + 273.15
#
#     class temp_kelvin(converter):
#         def kelvin_fahrenheit(self):
#             return (self.num - 273.15) * 1.8 + 32
#
#         def kelvin_celsius(self):
#             return self.num - 273.15
#
#
# class metric_metric:
#     class metric_centi(converter):
#         def centi_meter(self):
#             return self.num / 100
#
#         def centi_kilo(self):
#             return self.num / 100000
#
#         def centi_mili(self):
#             return self.num * 10
#
#         def centi_micro(self):
#             return self.num * 10000
#
#         def centi_nano(self):
#             return self.num * 10000000
#
#     class metric_meter(converter):
#         def meter_centi(self):
#             return self.num * 100
#
#         def meter_kilo(self):
#             return self.num / 1000
#
#         def meter_mili(self):
#             return self.num * 1000
#
#         def meter_micro(self):
#             return self.num * 1000000
#
#         def meter_nano(self):
#             return self.num * 1000000000
#
#     class metric_kilo(converter):
#         def kilo_centi(self):
#             return self.num * 1000000
#
#         def kilo_meter(self):
#             return self.num * 1000
#
#         def kilo_mili(self):
#             return self.num * 1000000
#
#         def kilo_micro(self):
#             return self.num * 1000000000
#
#         def kilo_nano(self):
#             return self.num * 1000000000000
#
#     class metric_mili(converter):
#         def mili_centi(self):
#             return self.num / 10
#
#         def mili_meter(self):
#             return self.num / 1000
#
#         def mili_kilo(self):
#             return self.num / 1000000
#
#         def mili_micro(self):
#             return self.num * 1000
#
#         def mili_nano(self):
#             return self.num * 1000000
#
#     class metric_micro(converter):
#         def micro_centi(self):
#             return self.num / 10000
#
#         def micro_meter(self):
#             return self.num / 1000000
#
#         def micro_kilo(self):
#             return self.num / 1000000000
#
#         def micro_mili(self):
#             return self.num / 1000
#
#         def micro_nano(self):
#             return self.num * 1000
#
#     class metric_nano(converter):
#         def nano_centi(self):
#             return self.num / 10000000
#
#         def nano_meter(self):
#             return self.num / 1000000000
#
#         def nano_kilo(self):
#             return self.num / 1000000000000
#
#         def nano_mili(self):
#             return self.num / 1000000
#
#         def nano_micro(self):
#             return self.num / 1000
#
#
# class metric_imperial:
#     class mi_centi(converter):
#         def centi_inch(self):
#             return self.num / 2.54
#
#         def centi_foot(self):
#             return self.num / 30.48
#
#         def centi_yard(self):
#             return self.num / 91.44
#
#         def centi_mile(self):
#             return self.num / 160934
#
#         def centi_nmile(self):
#             return self.num / 185200
#
#     class mi_meter(converter):
#         def meter_inch(self):
#             return self.num * 39.37
#
#         def meter_foot(self):
#             return self.num * 3.281
#
#         def meter_yard(self):
#             return self.num * 1.094
#
#         def meter_mile(self):
#             return self.num / 1609
#
#         def meter_nmile(self):
#             return self.num / 1852
#
#     class mi_kilo(converter):
#         def kilo_inch(self):
#             return self.num * 39370
#
#         def kilo_foot(self):
#             return self.num * 3281
#
#         def kilo_yard(self):
#             return self.num * 1094
#
#         def kilo_mile(self):
#             return self.num / 1.609
#
#         def kilo_nmile(self):
#             return self.num / 1.852
#
#     class mi_mili(converter):
#         def mili_inch(self):
#             return self.num / 25.4
#
#         def mili_foot(self):
#             return self.num / 305
#
#         def mili_yard(self):
#             return self.num / 914
#
#         def mili_mile(self):
#             return self.num / 1609344
#
#         def mili_nmile(self):
#             return self.num / 1852000
#
#     class mi_micro(converter):
#         def micro_inch(self):
#             return self.num / 25400
#
#         def micro_foot(self):
#             return self.num / 304800
#
#         def micro_yard(self):
#             return self.num / 914400
#
#         def micro_mile(self):
#             return self.num / 1609344000
#
#         def micro_nmile(self):
#             return self.num / 1852000000
#
#     class mi_nano(converter):
#         def nano_inch(self):
#             return self.num / 25400000
#
#         def nano_foot(self):
#             return self.num / 304800000
#
#         def nano_yard(self):
#             return self.num / 914400000
#
#         def nano_mile(self):
#             return self.num / 1609344000000
#
#         def nano_nmile(self):
#             return self.num / 1852000000000
#
#
# class imperial_imperial:
#     class imperial_inch(converter):
#         def inch_foot(self):
#             return self.num / 12
#
#         def inch_yard(self):
#             return self.num / 36
#
#         def inch_mile(self):
#             return self.num / 63360
#
#         def inch_nmile(self):
#             return self.num / 72913
#
#     class imperial_foot(converter):
#         def foot_inch(self):
#             return self.num * 12
#
#         def foot_yard(self):
#             return self.num / 3
#
#         def foot_mile(self):
#             return self.num / 5280
#
#         def foot_nmile(self):
#             return self.num / 6076
#
#     class imperial_yard(converter):
#         def yard_inch(self):
#             return self.num * 36
#
#         def yard_foot(self):
#             return self.num * 3
#
#         def yard_mile(self):
#             return self.num / 1760
#
#         def yard_nmile(self):
#             return self.num / 2025
#
#     class imperial_mile(converter):
#         def mile_inch(self):
#             return self.num * 63360
#
#         def mile_foot(self):
#             return self.num * 5280
#
#         def mile_yard(self):
#             return self.num * 1760
#
#         def mile_nmile(self):
#             return self.num / 1.151
#
#     class imperial_nmile(converter):
#         def nmile_inch(self):
#             return self.num * 72913
#
#         def nmile_foot(self):
#             return self.num * 6076
#
#         def nmile_yard(self):
#             return self.num * 2025
#
#         def nmile_mile(self):
#             return self.num * 1.151
#
#
# class imperial_metric:
#     class im_inch(converter):
#         def inch_centi(self):
#             return self.num * 2.54
#
#         def inch_meter(self):
#             return self.num / 39.37
#
#         def inch_kilo(self):
#             return self.num / 39370
#
#         def inch_mili(self):
#             return self.num * 25.4
#
#         def inch_micro(self):
#             return self.num * 25400
#
#         def inch_nano(self):
#             return self.num * 25400000
#
#     class im_foot(converter):
#         def foot_centi(self):
#             return self.num * 30.48
#
#         def foot_meter(self):
#             return self.num / 3.281
#
#         def foot_kilo(self):
#             return self.num / 3281
#
#         def foot_mili(self):
#             return self.num * 305
#
#         def foot_micro(self):
#             return self.num * 304800
#
#         def foot_nano(self):
#             return self.num * 304800000
#
#     class im_yard(converter):
#         def yard_centi(self):
#             return self.num * 91.44
#
#         def yard_meter(self):
#             return self.num / 1.094
#
#         def yard_kilo(self):
#             return self.num / 1094
#
#         def yard_mili(self):
#             return self.num * 914
#
#         def yard_micro(self):
#             return self.num * 914400
#
#         def yard_nano(self):
#             return self.num * 914400000
#
#     class im_mile(converter):
#         def mile_centi(self):
#             return self.num * 160934
#
#         def mile_meter(self):
#             return self.num * 1609.34
#
#         def mile_kilo(self):
#             return self.num * 1.60934
#
#         def mile_mili(self):
#             return self.num * 1609344
#
#         def mile_micro(self):
#             return self.num * 1609344000
#
#         def mile_nano(self):
#             return self.num * 1609344000000
#
#     class im_nmile(converter):
#         def nmile_centi(self):
#             return self.num * 185200
#
#         def nmile_meter(self):
#             return self.num * 1852
#
#         def nmile_kilo(self):
#             return self.num * 1.852
#
#         def nmile_mili(self):
#             return self.num * 1852000
#
#         def nmile_micro(self):
#             return self.num * 1852000000
#
#         def nmile_nano(self):
#             return self.num * 1852000000000
#
