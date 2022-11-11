import PySimpleGUI as sg

# The graphic user interface of the program.
def interface():
    
    font = ("Arial", 15)

    layout = [[sg.T('This program is designed to create multiple paths so you can travel safe through the city.\nPlease be as specific as you can.\n', font = font)],
              [sg.T('Origin         ', font = font), sg.Input(key='origin', font = font)],
              [sg.T('Destination', font = font), sg.Input(key='destination', font = font)],
              [sg.Button('Search', font = font), sg.Button('Exit', font = font)]]

    window = sg.Window('Safest and Shortest Path Algorithm', layout)

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': window.close()
    window.close() 
    if 'Search': return values