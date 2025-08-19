import csv

def default():
    with open("contacts.csv",'a+') as f:
        writer = csv.DictWriter(f, fieldnames = ["Name","Contact no.","Email"],delimiter= "|")
        f.seek(0)
        if f.read(1):
            pass
        else:
            writer.writeheader()
            writer.writerow({"Name":"Police Control Room","Contact no.":"100","Email":"never.come.on.time@gmail.com"})
            writer.writerow({"Name":"Fire Brigade","Contact no.":"101","Email":"majedaar.matter@gmail.com"})
            writer.writerow({"Name":"Ambulance","Contact no.":"102","Email":"rest.in.peace@gmail.com"})
            writer.writerow({"Name":"Women Helpline","Contact no.":"1090","Email":"dish.washer@gmail.com"})
            writer.writerow({"Name":"Child Helpline","Contact no.":"1098","Email":"bacche.mann.k.sacche@gmail.com"})
default()

def display_contacts(reader):
    contacts = list(reader)
    if not contacts:
        print("No contacts found.")
        return
    print("\n" + "-"*70)
    print(f"{'Name'.ljust(25)} | {'Contact no.'.ljust(15)} | {'Email'}")
    print("-"*70)
    for row in contacts:
        print(f"{row['Name'].ljust(25)} | {row['Contact no.'].ljust(15)} | {row['Email']}")
    print("-"*70 + "\n")

def add():
    with open("contacts.csv",'r') as f:
        reader = csv.DictReader(f, delimiter = "|")
        print("\n--- Adding Contact ---")
        name = input("Enter Name: ").strip()
        contact = input("Enter contact number: ").strip()
        email = input("Enter email: ").strip()
        for row in reader:
            if(row["Contact no."].strip() == contact):
                print("\nContact already exists:")
                display_contacts([row])
                return
    with open("contacts.csv",'a') as f:
        writer = csv.DictWriter(f, fieldnames = ["Name","Contact no.","Email"], delimiter="|")
        writer.writerow({"Name":name,"Contact no.":contact,"Email":email})
        print("\nContact added successfully!\n")

def read():
    with open("contacts.csv",'r') as f:
        reader = csv.DictReader(f, delimiter= "|")
        print("\n--- All Contacts ---")
        display_contacts(reader)

def search():
    with open("contacts.csv",'r') as f:
        reader = csv.DictReader(f, delimiter= "|")
        print("\n--- Searching Contact ---")
        while True:
            print("1. Search by name\n2. Search by contact no.\n3. Search by email")
            searchby = input("Enter search method: ").strip()
            sname = scontact = semail = None
            if(searchby == "1"):
                sname = input("Enter name: ").strip().lower()
                break
            elif(searchby == "2"):
                scontact = input("Enter contact no.: ").strip()
                break
            elif(searchby == "3"):
                semail = input("Enter email: ").strip().lower()
                break
            else:
                print("Invalid input!!! Try again.")
        results = []
        for row in reader:
            if (
                (sname and row["Name"].strip().lower() == sname) or
                (scontact and row["Contact no."].strip() == scontact) or
                (semail and row["Email"].strip().lower() == semail)
            ):
                results.append(row)
        if results:
            display_contacts(results)
        else:
            print("\nNo contact found with this detail.\n")

def update():
    with open("contacts.csv",'r') as f:
        reader = csv.DictReader(f, delimiter= "|")
        contact = input("\nEnter contact no. to update its details: ").strip()
        updated_contacts = []
        found = False
        for row in reader:
            if (row["Contact no."].strip() == contact):
                print("\nFound Contact:")
                display_contacts([row])
                print("\n--- Enter New Details ---")
                uname = input("Enter Name: ").strip()
                ucontact = input("Enter contact number: ").strip()
                uemail = input("Enter email: ").strip()
                row["Name"] = uname
                row["Contact no."] = ucontact
                row["Email"] = uemail
                found = True
            updated_contacts.append(row)
    with open("contacts.csv",'w') as f:
        writer = csv.DictWriter(f, fieldnames = ["Name","Contact no.","Email"],delimiter= "|")
        writer.writeheader()
        writer.writerows(updated_contacts)
        if(not found):
            print("\nNo contact found with this number.\n")
        else:
            print("\nContact updated successfully!\n")

def delete():
    with open("contacts.csv",'r') as f:
        reader = csv.DictReader(f, delimiter= "|")
        print("\n--- Deleting Contact ---")
        dcontact = input("Enter contact no. to delete its details: ").strip()
        updated_contacts = []
        found = False
        for row in reader:
            if(row["Contact no."].strip() == dcontact):
                print("\nDeleted Contact:")
                display_contacts([row])
                found = True
                continue
            else:
                updated_contacts.append(row)
    with open("contacts.csv",'w') as f:
        writer = csv.DictWriter(f, fieldnames = ["Name","Contact no.","Email"],delimiter= "|")
        writer.writeheader()
        writer.writerows(updated_contacts)
        if(not found):
            print("\nNo contact found with these details.\n")
        else:
            print("\nContact deleted successfully!\n")

def menu():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add()
        elif choice == "2":
            read()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!!! Try again.")

menu()