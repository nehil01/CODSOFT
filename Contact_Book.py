contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input("""
                       1. Add new Contact
                       2. Search Contact
                       3. Display Contact
                       4. Edit Contact
                       5. Delete Contact
                       6. Exit 
                       
                       Enter Your Choice :"""))
    if choice == 1:
        name = input("Enter the Contact Name : ")
        phone = input("Enter the Mobile Number : ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter Name to be Searched : ")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("Contact not Found !")
    elif choice == 3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter contact to be Edited : ")
        if edit_contact in contact:
            phone = input("Enter Mobile Number : ")
            contact[edit_contact]=phone
            print("Contact Updated")
            display_contact()
        else:
            print("Contact not Found !")
    elif choice == 5:
        del_contact = input("Enter contact to be Deleted : ")
        if del_contact in contact:
            confirm = input("Do you want to Delete this Contact y/n : ")
            if confirm =='y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Contact not Found !")
    else:
        break
