def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    return "Name is already taken, try another one."


def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact change."
    return "Not found user`s name"


def phone_username(name, contacts):
    name = name[0]
    return contacts[name]


def all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_username_phone(args, contacts))
            elif command == "phone":
                print(f' Number: {phone_username(args, contacts)}')
            elif command == "all":
                print(all(contacts))
            else:
                print("Invalid command.")
        except ValueError:
            print("Wrong input, try like example: comands name phone")


if __name__ == "__main__":
    main()
