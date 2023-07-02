from convert_length import *
from convert_mass import *
from convert_pressure import *
from convert_temp import *
from convert_speed import *
from convert_area import *
from convert_time import *
from convert_index import *


def main():
    print("Welcome to converter 2.0!")
    while True:
        try:
            input_unit = main_list[int(input("0 - Length \n1 - Mass \n2 - Pressure \n3 - Temperature \n4 - Speed \n5 - Area \n6 - Time \n>>> "))]
        except (ValueError, IndexError):
            print("Not a number/ not in selection")
            continue
        convert = 0
        while True:
            match input_unit:
                case 1:
                    while True:
                        try:
                            input_unit1 = length_list[int(input("Input: \nMetric: \n0 - Cm \n1 - Meter \n2 - Km \n3 - Mm \n4 - Mcm \n5 - Nm \nImperial: \n6 - Foot \n7 - Yard \n8 - Inch \n9 - Mile \n10 - Nautical mile \n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Value: "))
                            output_unit1 = length_list[int(input("Output: \nMetric: \n0 - Cm \n1 - Meter \n2 - Km \n3 - Mm \n4 - Mcm \n5 - Nm \nImperial: \n6 - Foot \n7 - Yard \n8 - Inch \n9 - Mile \n10 - Nautical mile \n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in selection")
                            continue
                        match input_unit1:
                            case 'Centimeters':
                                convert = Centimeter(num)
                            case 'Meters':
                                convert = Meter(num)
                            case 'Kilometers':
                                convert = Kilometer(num)
                            case 'Millimeters':
                                convert = Millimeter(num)
                            case 'Micrometers':
                                convert = Micrometer(num)
                            case 'Nanometers':
                                convert = Nanometer(num)
                            case 'Feet':
                                convert = Foot(num)
                            case 'Yards':
                                convert = Yard(num)
                            case 'Inches':
                                convert = Inch(num)
                            case 'Miles':
                                convert = Mile(num)
                            case 'Nautical Miles':
                                convert = Nmile(num)
                        match output_unit1:
                            case 'Centimeters':
                                print(convert.as_centimeter())
                            case 'Meters':
                                print(convert.as_meter())
                            case 'Kilometers':
                                print(convert.as_kilometer())
                            case 'Millimeters':
                                print(convert.as_millimeter())
                            case 'Micrometers':
                                print(convert.as_micrometer())
                            case 'Nanometers':
                                print(convert.as_nanometer())
                            case 'Feet':
                                print(convert.as_foot())
                            case 'Yards':
                                print(convert.as_yard())
                            case 'Inches':
                                print(convert.as_inch())
                            case 'Miles':
                                print(convert.as_mile())
                            case 'Nautical Miles':
                                print(convert.as_nmile())
                        break
                case 2:
                    while True:
                        try:
                            input_unit1 = mass_list[int(input(
                                "Input: \nMetric: \n0 - Kg \n1 - Ton \n2 - Gram \n3 - Mg \n4 - Mcg \nImperial: \n5 - Imperial ton \n6 - US ton \n7 - Pound \n8 - Ounce \n9 - Stone \n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Enter your value: "))
                            output_unit1 = mass_list[int(input(
                                "Output \nMetric: \n0 - Kg \n1 - Ton \n2 - Gram \n3 - Mg \n 4 - Mcg \nImperial: \n5 - Imperial ton \n6 - US ton \n7 - Pound \n8 - Ounce \n9 - Stone \n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in this selection")
                            continue
                        match input_unit1:
                            case 'Kilograms':
                                convert = Kilogram(num)
                            case 'Tons':
                                convert = Ton(num)
                            case 'Grams':
                                convert = Gram(num)
                            case 'Milligrams':
                                convert = Milligram(num)
                            case 'Micrograms':
                                convert = Microgram(num)
                            case 'Imperial Tons':
                                convert = Im_Ton(num)
                            case 'US Tons':
                                convert = Us_Ton(num)
                            case 'Pounds':
                                convert = Pound(num)
                            case 'Ounces':
                                convert = Ounce(num)
                            case 'Stones':
                                convert = Stone(num)
                        match output_unit1:
                            case 'Kilograms':
                                print(convert.as_kg())
                            case 'Tons':
                                print(convert.as_ton())
                            case 'Grams':
                                print(convert.as_gram())
                            case 'Milligrams':
                                print(convert.as_milligram())
                            case 'Micrograms':
                                print(convert.as_microgram())
                            case 'Imperial Tons':
                                print(convert.as_im_ton())
                            case 'US Tons':
                                print(convert.as_us_ton())
                            case 'Pounds':
                                print(convert.as_pound())
                            case 'Ounces':
                                print(convert.as_ounce())
                            case 'Stones':
                                print(convert.as_stone())
                        break
                case 3:
                    while True:
                        try:
                            input_unit1 = pressure_list[int(input("Input: \n0 - Bar \n1 - Psi \n2 - Pascal \n3 - Atmospheres \n4 - Torr \n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Enter your value: "))
                            output_unit1 = pressure_list[int(input("Output: \n0 - Bar \n1 - Psi \n2 - Pascal \n3 - Atmospheres \n4 - Torr \n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in this selection")
                            continue
                        match input_unit1:
                            case 'Bars':
                                convert = Bar(num)
                            case 'Psi':
                                convert = Psi(num)
                            case 'Pascals':
                                convert = Pascal(num)
                            case 'Atmospheres':
                                convert = Atmosphere(num)
                            case 'Torrs':
                                convert = Torr(num)
                        match output_unit1:
                            case 'Bars':
                                print(convert.as_bar())
                            case 'Psi':
                                print(convert.as_psi())
                            case 'Pascals':
                                print(convert.as_pascal())
                            case 'Atmospheres':
                                print(convert.as_atmosphere())
                            case 'Torrs':
                                print(convert.as_torr())
                        break

                case 4:
                    while True:
                        try:
                            input_unit1 = temp_list[
                                int(input("Input: \n0 - Celsius \n1 - Fahrenheit \n2 - Kelvin \n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Enter your value: "))
                            output_unit1 = temp_list[
                                int(input("Input: \n0 - Celsius \n1 - Fahrenheit \n2 - Kelvin \n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in this selection")
                            continue
                        match input_unit1:
                            case 'Celsius':
                                convert = Celsius(num)
                            case 'Fahrenheit':
                                convert = Fahrenheit(num)
                            case 'Kelvin':
                                convert = Kelvin(num)
                        match output_unit1:
                            case 'Celsius':
                                print(convert.as_celsius())
                            case 'Fahrenheit':
                                print(convert.as_fahrenheit())
                            case 'Kelvin':
                                print(convert.as_kelvin())
                        break
                case 5:
                    while True:
                        try:
                            input_unit1 = speed_list[int(input("Input: \n0 - Miles per Hour \n1 - Meters per Second \n2 - Feet per Second \n3 - Kilometers per Hour \n4 - Knots \n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = int(input("Enter your value: "))
                            output_unit1 = speed_list[int(input("Output: \n0 - Miles per Hour \n1 - Meters per Second \n2 - Feet per Second \n3 - Kilometers per Hour \n4 - Knots \n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in this selection")
                            continue
                        match input_unit1:
                            case 'Mph':
                                convert = Mph(num)
                            case 'Mps':
                                convert = Mps(num)
                            case 'Fps':
                                convert = Fps(num)
                            case 'Kph':
                                convert = Kph(num)
                            case 'Knots':
                                convert = Knot(num)
                        match output_unit1:
                            case 'Mph':
                                print(convert.as_mph())
                            case 'Mps':
                                print(convert.as_mps())
                            case 'Fps':
                                print(convert.as_fps())
                            case 'Kph':
                                print(convert.as_kph())
                            case 'Knots':
                                print(convert.as_knot())
                        break
                case 6:
                    while True:
                        try:
                            input_unit1 = area_list[int(input("Input: \n0 - Sq. Meter \n1 - Sq. Km \n2 - Sq. Mile \n3 - Sq. Yard, \n4 - Sq. Foot \n5 - Sq. Inch \n6 - Hectare \n7 - Acre\n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Enter your value:"))
                            output_unit1 = area_list[int(input("Output: \n0 - Sq. Meter \n1 - Sq. Km \n2 - Sq. Mile \n3 - Sq. Yard, \n4 - Sq. Foot \n5 - Sq. Inch \n6 - Hectare \n7 - Acre\n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in selection")
                            continue
                        match input_unit1:
                            case 'Sq. Meters':
                                convert = Sq_meter(num)
                            case 'Sq. Kilometers':
                                convert = Sq_kilometer(num)
                            case 'Sq. Miles':
                                convert = Sq_mile(num)
                            case 'Sq. Yards':
                                convert = Sq_yard(num)
                            case 'Sq. Feet':
                                convert = Sq_foot(num)
                            case 'Sq. Inches':
                                convert = Sq_inch(num)
                            case 'Hectares':
                                convert = Hectare(num)
                            case 'Acres':
                                convert = Acre(num)
                        match output_unit1:
                            case 'Sq. Meters':
                                print(convert.as_sq_meter())
                            case 'Sq. Kilometers':
                                print(convert.as_sq_kilometer())
                            case 'Sq. Miles':
                                print(convert.as_sq_mile())
                            case 'Sq. Yards':
                                print(convert.as_sq_yard())
                            case 'Sq. Feet':
                                print(convert.as_sq_foot())
                            case 'Sq. Inches':
                                print(convert.as_sq_inch())
                            case 'Hectares':
                                print(convert.as_hectare())
                            case 'Acres':
                                print(convert.as_acre())
                        break
                case 7:
                    while True:
                        try:
                            input_unit1 = time_list[int(input("Input:\n0 - Nanosecond\n1 - Microsecond\n2 - Millisecond\n3 - Second\n4 - Minute\n5 - Hour\n6 - Day\n7 - Week\n8 - Month\n9 - Year\n10 - Decade\n11 - Century\n12 - Millennium\n>>> "))]
                            print(f"Selected Measurement: {input_unit1}")
                            num = float(input("Enter your value: "))
                            output_unit1 = time_list[int(input("Output:\n0 - Nanosecond\n1 - Microsecond\n2 - Millisecond\n3 - Second\n4 - Minute\n5 - Hour\n6 - Day\n7 - Week\n8 - Month\n9 - Year\n10 - Decade\n11 - Century\n12 - Millennium\n>>> "))]
                            print(f"Selected Measurement: {output_unit1}")
                        except (ValueError, IndexError):
                            print("Not a number/ not in selection")
                            continue
                        match input_unit1:
                            case 'Nanoseconds':
                                convert = Nanosecond(num)
                            case 'Microseconds':
                                convert = Microsecond(num)
                            case 'Milliseconds':
                                convert = Millisecond(num)
                            case 'Seconds':
                                convert = Second(num)
                            case 'Minutes':
                                convert = Minute(num)
                            case 'Hours':
                                convert = Hour(num)
                            case 'Days':
                                convert = Day(num)
                            case 'Weeks':
                                convert = Week(num)
                            case 'Months':
                                convert = Month(num)
                            case 'Years':
                                convert = Year(num)
                            case 'Decades':
                                convert = Decade(num)
                            case 'Centuries':
                                convert = Century(num)
                            case 'Millennia':
                                convert = Millennium(num)
                        match output_unit1:
                            case 'Nanoseconds':
                                print(convert.as_nanosecond())
                            case 'Microseconds':
                                print(convert.as_microsecond())
                            case 'Milliseconds':
                                print(convert.as_millisecond())
                            case 'Seconds':
                                print(convert.as_second())
                            case 'Minutes':
                                print(convert.as_minute())
                            case 'Hours':
                                print(convert.as_hour())
                            case 'Days':
                                print(convert.as_day())
                            case 'Weeks':
                                print(convert.as_week)
                            case 'Months':
                                print(convert.as_month())
                            case 'Years':
                                print(convert.as_year())
                            case 'Decades':
                                print(convert.as_decade())
                            case 'Centuries':
                                print(convert.as_century())
                            case 'Millennia':
                                print(convert.as_millennium())
                        break
                    break
            break
        break


if __name__ == '__main__':
    while True:
        main()
        again = input("Do you want to use it again? ").lower()
        if again in ['yes', 'ok', 'sure', 'yeah']:
            print("Okay!")
            continue
        else:
            print("Alright")
            break
