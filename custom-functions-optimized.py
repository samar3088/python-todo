def get_todos(filepath='todos.txt'):
    """ Read the text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args,filepath='todos.txt'):
    """ Write the text file with list of to-do items """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


while True:
    user_action = input("Type add,show,edit,complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # todo = input("Enter a todo") + "\n"
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        # write_todos(todos,'todos.txt')
        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index,item in enumerate(todos):
            item = item.strip()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            # number = int(input("Number to be edit"))
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo :")
            todos[number] = new_todo + '\n'

            # write_todos(todos,'todos.txt')
            write_todos(todos)

        except ValueError:## error handling using try catch is explained here
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            #number = int(input("Number to be complete"))
            number = int(user_action[9:])
            todos = get_todos()

            index = number - 1

            todo_to_remove = todos[index]
            todos.pop(index)

            # write_todos(todos,'todos.txt')
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print('Please enter item that is in the list')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Thank you')