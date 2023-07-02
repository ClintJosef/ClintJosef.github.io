import PySimpleGUI as sg


def convert_window():
    layout = [
        [sg.Input(key='-INPUT-'),
         sg.Spin(['Ft to Meters', 'Km to Miles', 'Inches to Cm'], key='-UNIT-'),
         sg.Button('Convert', key='-BUTTON-')],
        [sg.Text('Output', key='-RESULT-')]
    ]
    return sg.Window('Converter 3.0', layout, )


def convert():
    converter = convert_window()
    output = 0

    while True:
        event, values = converter.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-BUTTON-':
            num = values['-INPUT-']
            if num.isnumeric():
                match values['-UNIT-']:
                    case 'Ft to Meters':
                        result = round(float(num) / 3.28084, 4)
                        output = f'{num} feet would be {result} meters. '
                    case 'Km to Miles':
                        result = round(float(num) / 1.609, 4)
                        output = f'{num} km would be {result} miles. '
                    case 'Inches to Cm':
                        result = round(float(num) * 2.54, 4)
                        output = f'{num} inches would be {result} cm. '
            else:
                converter['-RESULT-'].update("Not a number.")
            converter['-RESULT-'].update(output)
    converter.close()


if __name__ == '__main__':
    convert()
