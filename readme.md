# Система для управління адресною книгою.

## Сутності:

* Field: Базовий клас для полів запису.
* Name: Клас для зберігання імені контакту. Обов'язкове поле.
* Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
* Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
* AddressBook: Клас для зберігання та управління записами.


## Функціональність:

AddressBook:
* Додавання записів.
* Пошук записів за іменем.
* Видалення записів за іменем.

Record:
* Додавання телефонів.
* Видалення телефонів.
* Редагування телефонів.
* Пошук телефону.

## Приклад використання:
```python
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
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
