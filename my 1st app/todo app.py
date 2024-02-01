#from functions import get_todos, write_todos
import functions


while True:
    user_action= input("Type add,show,edit,complete,exit")
    user_action= user_action.strip()

    if user_action.startswith("add"):
        todo =user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item= item.strip('\n')
            row =f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number= int(user_action[5:])
            print(number)

            number = number  -1
            todos = functions.get_todos()
            new_todo = input("Enter your new todo: ")
            todos[number] =new_todo+ '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your Command Isn't Valid.")
            continue