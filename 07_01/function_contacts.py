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


# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     if name in contacts:
#         user_input = input("Contact already exists. Do you want to update it? (yes/no): ")
#         if user_input.strip().lower() == "yes":
#             return change_contact(args, contacts)
#         else:
#             return "Contact not added."
#     contacts[name] = phone
#     return "Contact added."

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
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact not found."


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
