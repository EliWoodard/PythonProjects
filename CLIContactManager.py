# add contact
def AddContact(contactList):
    contactName = input("Contact name: ")
    phoneNumber = input("Phone Number: ")
    email = input("Email: ")
    contactList[contactName] = [phoneNumber, email]
    print(f"Added {contactName} as a contact with the phone number {phoneNumber} and email of {email}")

# Contact manager selection
def ContactHeader():
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    return int(input("\nChoose an option:"))

# Delete contact from list
def DeleteContact(contactList):
    selectedContact = input("Which contact do you want to delete: ")
    success = contactList.pop(selectedContact, None)  

    if success is not None:
        print(f"Successfully removed {selectedContact}")
    else:
        print(f"Couldn't find {selectedContact}")

# search inventory
def SearchContacts(contactList):
    contactKey = input("Enter a existing contact name: ")

    contactValue = contactList.get(contactKey)
    if contactValue is not None:
        print(f"Found {contactKey} with the phone number {contactValue[0]} and email {contactValue[1]}")
    else:
        print(f"Couldn't find {contactKey}")


# view inventory
def ViewContacts(contactList):
    contactNumber = 1
    for key, value in contactList.items():
        print(f"===== {contactNumber} =====")
        print(f"Contact: {key}")
        print(f"Phone Number: {value[0]}")
        print(f"Email: {value[1]}")
        contactNumber += 1

contacts = {}

# See if data file has been created, if not create a new one, and then populate contact dictionary
with open("dataLog.txt", "a+") as file:
    # 1. Move pointer to the beginning to read existing data
    file.seek(0)

    # 2. populate contact list with data file
    for line in file:
        if line.strip():  # Skip empty lines
            lineValues = line.strip().split(",")
            contacts[lineValues[0]] = [lineValues[1], lineValues[2]]

    userInput = ContactHeader()
    print()

    while(userInput != 5):
        if userInput > 5 or userInput < 1:
            print ("Invalid option, please choose between 1 and 5.")
        elif userInput == 1:
            AddContact(contacts)
        elif userInput == 2:
            ViewContacts(contacts)
        elif userInput == 3:
            SearchContacts(contacts)
        elif userInput == 4:
            DeleteContact(contacts)
        elif userInput == 5:
            break
        print()
        userInput = ContactHeader()
        print()

        file.seek(0)      # 1. Move pointer to the absolute beginning
        file.truncate(0)  # 2. Chop the file size down to 0 bytes (wipes everything)

        # Repopulate file with saved data
        for key, value in contacts.items():
            file.write(f"{key},{value[0]},{value[1]}\n")