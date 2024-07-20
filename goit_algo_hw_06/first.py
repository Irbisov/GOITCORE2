from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def name(self):
        return self.value


class Phone(Field):
    def phone(self):
        if len(self.value) == 10 and self.value.isdigit():
            return self.value
        else:
            print(
                f"Phone number {self.value} not correct. A class for storing a phone number. Has format validation "
                f"(10 digits).")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if bool(Phone(phone).phone()):
            self.phones.append(Phone(phone).phone())

    def remove_phone(self, phone):
        try:
            self.phones.remove(Phone(phone).phone())
        except ValueError:
            print(f'Phone number {phone} for remove not exist')

    def edit_phone(self, old_phone, new_phone):
        if Phone(old_phone).phone() in self.phones:
            for i in self.phones:
                if i == old_phone:
                    index = self.phones.index(i)
                    self.phones.remove(i)
                    if bool(Phone(new_phone).phone()):
                        self.phones.insert(index, new_phone)
        else:
            print(f'Phone nuber {old_phone} for edit not exist')

    def find_phone(self, phone):
        if Phone(phone).phone() in self.phones:
            return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}."


class AddressBook(UserDict):

    def add_record(self, contact_name: Record):
        self.data[contact_name.name.value] = contact_name

    def find(self, name) -> Record:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        del self.data[name]

    # Створення нової адресної книги


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
jane = book.find("Jane")
john.add_phone('1234567890')
john.remove_phone('1112223333')
book.add_record(john)
print(jane)
print(john)
# Видалення запису Jane
book.delete("Jane")
print(book)
