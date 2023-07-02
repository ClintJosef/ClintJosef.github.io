import PySimpleGUI as sg
import time


def window_start():
    sg.set_options(font='ComicSansMS')
    layout = [
        [sg.VPush()],
        [sg.Text(0, font='ComicSansMS 20', key='-TIME-')],
        [sg.Button('Start', key='-START-'), sg.Button('Lap', key='-LAP-', visible=False)],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]]
    return sg.Window(
        '',
        layout,
        element_justification='center')


def stoopwatch():
    window = window_start()
    start_time = 0
    active = False
    lap_times = 1

    while True:
        event, values = window.read(timeout=1)

        match event:
            case sg.WIN_CLOSED:
                break

            case '-START-':
                if active:
                    active = False
                    window['-START-'].update('Reset')
                    window['-LAP-'].update(visible=False)
                else:
                    if start_time > 0:
                        start_time = 0
                        active = False
                        lap_times = 1
                        window.close()
                        window = window_start()
                    else:
                        active = True
                        start_time = time.time()
                        window['-START-'].update('Stop')
                        window['-LAP-'].update(visible=True)

        if active:
            stopwatch = round(time.time() - start_time, 1)
            window['-TIME-'].update(stopwatch)
            if event == '-LAP-':
                window.extend_layout(
                    window['-LAPS-'],
                    [[sg.Text(f'{lap_times} - {stopwatch}', font='ComicSansMS 13')]])
                lap_times += 1

    window.close()


if __name__ == '__main__':
    stoopwatch()
