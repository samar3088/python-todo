user_prompt = "Type add, show, edit or exit : "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a Todo : ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input('Enter the item to be edited : '))
            number = number - 1
            existing_todos = todos[number]
            new_todo = input("Please enter new todo")
            todos[number] = new_todo
            ##print(existing_todos)
        case _:
            print('Hey you have entered a unknown command')

print('Thank you')

