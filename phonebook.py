#!/usr/bin/python3
import json
from os.path import isfile


phonebook = []


def reloadbook(phonebookFile):
    if (isfile(phonebookFile)):
        with open(phonebookFile, mode='r', encoding='utf-8') as jsonFile:
            return json.loads(jsonFile.read())
    else:
        return None


def write_to_file(list: phonebook):
    pyObj = json.dumps(phonebook)
    with open("phonebook.json", mode='w+', encoding='utf-8') as jsonFile:
        jsonFile.write(pyObj)


def show_book(phonebook=None):
    if phonebook:
        for contact in phonebook:
            print("\nNAME:\t\t{}\nEmail:\t\t{}\nContact:\t{}".format(contact['name'], contact['email'], contact['number']))
    else:
        print("Phonebook is Empty")


while True:
    print("\nWELCOME TO YOUR PHONEBOOK")
    print("\t1. SHOW ALL CONTACTS\n\t2. ADD A CONTACT\n\t3. SEARCH FOR A CONTACT\n\t4. DELETE A CONTACT\n\t5. UPDATE A CONTACT\n\t6. EXIT\n")
    phonebook = reloadbook('phonebook.json')
    try:
        choice = int(input("What do you want to do today? "))
    except ValueError as err:
        print("INVALID OPTION PLEASE CHECK OPTIONS ABOVE")
        continue

    if choice == 1:
        show_book(phonebook)

    elif choice == 2:
        name = input("Enter name of contact: ")
        email = input("Enter contact email address: ")
        number = input("Enter contact number: ")
        contact = {'name': name, 'email': email, 'number': number}
        phonebook.append(contact)
        write_to_file(phonebook)
        print("\nNAME:\t{}\nEmail:\t{}\nContact:\t{} ".format(contact['name'], contact['email'], contact['number']))

    elif choice == 3:
        name = input("Enter name of contact to find: ")
        conta = [cont for cont in phonebook if name == cont['name']]
        if conta:
            contact = conta[0]
            print("\nNAME:\t{}\nEmail:\t{}\nContact:\t{} ".format(contact['name'], contact['email'], contact['number']))
        else:
            print('Please there is no contact with such name')

    elif choice == 4:
        name = input("Enter name of contact to delete: ")
        conta = [cont for cont in phonebook if name == cont['name']]
        if conta:
            contact = conta[0]
            phonebook.remove(contact)
            write_to_file(phonebook)
        else:
            print('Please there is no contact with such name')

    elif choice == 5:
        name = input("Enter name of contact to update: ")
        conta = [cont for cont in phonebook if name == cont['name']]
        if conta:
            contact = conta[0]
            contact['name'] = input("Enter name of contact: ")
            contact['email'] = input("Enter contact email address: ")
            contact['number'] = input("Enter contact number: ")
            write_to_file(phonebook)
        else:
            print('Please there is no contact with such name')

    if choice == 6:
        break
