import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to do')
input_box = sg.InputText(tooltip='Enter Todo')
add_button = sg.Button("Add")
window = sg.Window('My Todo App',layout=[[label, input_box],[add_button]])

window.read() # code is halted at this place
window.close()