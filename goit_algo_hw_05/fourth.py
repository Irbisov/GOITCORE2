def input_error(function):
    match function.__name__:
        case "add_contact":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (TypeError, ValueError):
                    return print("Func add, give me name and phone please.")
        case "parse_input":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (ValueError, TypeError):
                    return print("Func input, give any command .")
        case "change_username_phone":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (TypeError, ValueError):
                    return print("Func change_phone, give me name and phone please.")
        case "phone_username":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (TypeError, ValueError, IndexError):
                    return print("Func phone, give me name please.")
        case _:
            return print("Func not found")
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return print("Contact added.")
    return print("Name is already taken, try another one.")


@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return print("Contact change.")
    return print("Not found user`s name")


@input_error
def phone_username(name, contacts):
    name = name[0]
    if name in contacts:
        return print(f"Number: {contacts[name]}")
    return print("Not found user`s name")


def all(contacts):
    counter = 0
    for i, j in contacts.items():
        counter += 1
        print(f"№{counter}  name: {i}, phone: {j}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            if command in ["close", "exit", ]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                add_contact(args, contacts)
            elif command == "change":
                change_username_phone(args, contacts)
            elif command == "phone":
                phone_username(args, contacts)
            elif command == "all":
                all(contacts)
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
