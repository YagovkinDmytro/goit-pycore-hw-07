from collections import UserDict
from datetime import datetime
import get_upcoming_birthdays


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.strip():
            raise ValueError("Name cannot be empty")


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits long")
        
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        if self.birthday:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, value):
        self.phones = [phone for phone in self.phones if phone.value != value]

    def edit_phone(self, value, new_value):
        found = any(phone.value == value for phone in self.phones)
        if found:
            self.phones = [Phone(new_value) if phone.value == value else phone for phone in self.phones]
        else:
            raise ValueError("Phone number not found")
    
    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return f"Phone number {value} not found"
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)

    def __str__(self):
        
        return f"Contacts book: {self.data}"

     
book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("20.03.1990")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
# book.delete("Jane")

# Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)
#     print(name)

# upcoming_birthdays = get_upcoming_birthdays(users)
#     return f"Список привітань на цьому тижні: {upcoming_birthdays}"

# print(book)