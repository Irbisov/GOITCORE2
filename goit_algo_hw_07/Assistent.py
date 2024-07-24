from Adress_book import AddressBook, Record


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
        case "add_birthday":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (TypeError, ValueError, IndexError):
                    return print("Func add_birthday, give me inform please.")
        case "show_birthday":
            def inner(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (TypeError, ValueError, IndexError):
                    return print("Func show_birthday, give me inform please.")
        case _:
            return print("Func not found")
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_username_phone(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        message = "Contact not found."
        return print(message)
    else:
        record.edit_phone(old_phone, new_phone)


@input_error
def phone_username(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None:
        message = "Contact not found."
        return print(message)
    else:
        return print(f"Name: {record.name.value}, phones: {'; '.join(p.value for p in record.phones)}.")


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        message = "Contact not found."
        return print(message)
    else:
        record.add_birthday(birthday)


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None:
        message = "Contact not found."
        return print(message)
    else:
        return print(f"Name: {record.name}, birthday: {record.birthday}.")


def birthday(book: AddressBook):
    return AddressBook.get_upcoming_birthdays(book)

    # add i 1234567890
    # add_birthday i 25.07.1992
    # phone i
    # {record.birthday.value}
    ...
    ...


def all(book: AddressBook):
    counter = 0
    for i, j in book.items():
        counter += 1
        print(f"№{counter} {j}")


def main():
    book = AddressBook()
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
                add_contact(args, book)
            elif command == "change":
                change_username_phone(args, book)
            elif command == "phone":
                phone_username(args, book)
            elif command == "all":
                all(book)
            elif command == "add_birthday":
                add_birthday(args, book)
            elif command == "show_birthday":
                show_birthday(args, book)
            elif command == "birthdays":
                birthday(book)
            else:
                print("Invalid command.")