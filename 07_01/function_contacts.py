from functools import wraps
from addres_book import AddressBook, Record


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter 'Name' and 'Phone number'"
        except KeyError:
            return f"Contact not found."
        except IndexError:
            return "Please enter 'Name'"
        except Exception as e:
            return f"Unexpected error: {e}"
          
    return inner


def parse_input(user_input):
    params = user_input.split()
    if not params:
        return "", []
    cmd, *args = params
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args 
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone)
        return "Contact added."
    if any(phone_number.value == phone for phone_number in record.phones):
        return f"Phone number already exists: {phone}."
    record.add_phone(phone)
    return "Phone number added to existing contact."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args 
    record = book.find(name)
    if record is None:
        return "Contact not found"
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args 
    record = book.find(name)
    if record is None:
        return "Contact not found"
    phones = ', '.join(phone.value for phone in record.phones)
    return phones

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    
    contacts = [(f"Name: {key} || Phone#: {value}") for key, value in contacts.items()]

    return "\n".join(contacts)

@input_error
def add_birthday(args, book):
    # реалізація
    pass

@input_error
def show_birthday(args, book):
    # реалізація
    pass

@input_error
def birthdays(args, book):
    # реалізація
    pass
