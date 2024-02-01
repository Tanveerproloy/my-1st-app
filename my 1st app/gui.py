import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box =sg.InputText(tooltip="Enter todo",key= "todo")
add_button = sg.Button("Add")
list_box= sg.Listbox(values= functions.get_todos(), key= 'todos',
                     enable_events= True, size=[45,10])
edit_button = sg.Button("Edit")
window = sg.Window('My To-Do App', layout= [[label],[input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica',20))


while True:
    event,values =window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])