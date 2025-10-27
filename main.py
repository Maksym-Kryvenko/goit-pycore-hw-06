from collections import UserDict
import re

class Field:
    """
    Base class for fields in a contact record.
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Class for contact name with validation.
    """
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters and spaces")
        super().__init__(name)

class Phone(Field):
    """
    Class for contact phone number with validation.
    """
    def __init__(self, number):
        clean_number = re.sub(r"\D", "", number)
        if not re.fullmatch(r"\d{10}", clean_number):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(clean_number)
    
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

class Record:
    """
    Class representing a contact record.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        phone = Phone(number)
        if phone in self.phones:
            raise ValueError("Phone number already exists")
        self.phones.append(phone)

    def delete_phone(self, number):
        phone = self.find_phone(number)
        if not phone:
            raise ValueError("Phone number not found")
        self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        if self.find_phone(old_number):
            if self.find_phone(old_number) != Phone(new_number):
                self.delete_phone(old_number)
                self.add_phone(new_number)
            else:
                raise ValueError("New phone number already exists")
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, number):
        phone = Phone(number)
        if phone in self.phones:
            return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Class representing an address book.
    """
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found")