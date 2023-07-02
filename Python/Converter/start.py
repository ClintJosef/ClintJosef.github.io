from _time import *


def main():
    while True:
        try:
            input_unit = int(input("Input unit: \n1. Second \n2. NanoSecond \n3. MicroSecond \n>>> "))
        except ValueError:
            print("Not a number")
            continue

        try:
            value = float(input("Please enter the value: "))
        except ValueError:
            print("Not a number")
            continue

        try:
            output_unit = int(input("Output unit: \n1. Second \n2. Nanosecond \n3. MicroSecond \n>>> "))
        except ValueError:
            print("Not a number")
            continue
        while True:
            match input_unit:
                case 1:
                    distance = Second(value)
                case 2:
                    distance = NanoSecond(value)
                case 3:
                    distance = MicroSecond(value)
                case 4:
                    distance = Second(value)
                case 5:
                    distance = Minute(value)
                case _:
                    print("Unknown input unit type")
                    continue

            if output_unit == 1:
                print(distance.as_seconds())
            elif output_unit == 2:
                print(distance.as_nanoseconds())
            elif output_unit == 3:
                print(distance.as_microseconds())
            else:
                print("Unknown output unit type")
                continue
            break
        break


if __name__ == '__main__':
    main()
