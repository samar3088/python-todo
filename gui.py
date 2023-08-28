import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to do')
input_box = sg.InputText(tooltip='Enter Todo',key='todo')
add_button = sg.Button("Add")
window = sg.Window('My Todo App',
                   layout=[[label, input_box],
                           [add_button]],
                   font=('Helvetica','12'))

# event = window.read() # code is halted at this place
while True:
    event, values = window.read()
    print(event,values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()