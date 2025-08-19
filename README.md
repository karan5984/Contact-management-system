---

# 📇 Contact Management System

A Python-based **Contact Management System** that allows users to easily manage contacts.
The system uses a **CSV file** for storing contacts and provides full **CRUD operations** (Create, Read, Update, Delete) through a simple menu-driven interface.

---

## 🚀 Features

* ➕ **Add Contact** – Save new contact details (Name, Number, Email)
* 📋 **View All Contacts** – Display all saved contacts in a tabular format
* 🔍 **Search Contact** – Find contacts by **Name**, **Contact Number**, or **Email**
* ✏️ **Update Contact** – Modify details of an existing contact
* ❌ **Delete Contact** – Remove a contact from the system
* 💾 **Persistent Storage** – Contacts are stored in `contacts.csv` file
* 🛡️ **Preloaded Emergency Numbers** – Police (100), Fire (101), Ambulance (102), Women Helpline (1090), Child Helpline (1098)

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Library:** `csv` (for file handling)
* **Storage:** CSV file (`contacts.csv`)

---

## 📂 Project Structure

```
📁 Contact-Management-System
│── 📄 main.py        # Main program file (Contact Management System)
│── 📄 contacts.csv   # CSV file to store contacts (auto-created if not exists)
│── 📄 README.md      # Project documentation
```

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/contact-management-system.git
   ```
2. Navigate into the project folder:

   ```bash
   cd contact-management-system
   ```
3. Run the program:

   ```bash
   python main.py
   ```
4. Follow the menu options displayed in the terminal.

---

## 📸 Sample Menu

```
=== Contact Management System ===
1. Add Contact
2. Show All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter choice: 
```

---

## 🎯 Skills Demonstrated

* Python programming
* File handling with CSV module
* CRUD operations
* Menu-driven application design
* Data validation & duplicate handling

---

## 🔮 Future Scope

* Add **GUI support** using Tkinter or PyQt
* Import/Export contacts in **CSV / Excel format**
* Connect with **SQLite/MySQL database** for large-scale use
* Add **search filters** (partial matches, case-insensitive search, etc.)
* Enable **contact groups** and tagging

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---
