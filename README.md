# Branching-Out
Codio Assessment

# Branching-Out

A Python CLI project for practicing Git, GitHub workflows, and user data filtering.

---

## 📌 Description

This project loads user data from a `users.json` file and allows filtering users by different criteria via a command-line interface.

It is designed for learning:

* Git branching
* Feature development
* Input handling in Python
* JSON processing
* Clean code structure (PEP 8)

---

## 🚀 Features

* Filter users by **name**
* Filter users by **email**
* Filter users by **age**
* Interactive command-line menu
* Input validation (prevents crashes)
* Case-insensitive search for name and email

---

## 📁 Project Structure

```text id="proj1"
Branching-Out/
├── main.py
├── users.json
└── README.md
```

---

## ▶️ Usage

Run the program:

```bash id="run1"
python main.py
```

You will see:

```text id="menu1"
What would you like to filter by? (name, email, age):
```

---

## 🔎 Examples

### Name filter

```text id="ex1"
What would you like to filter by? (name, email, age): name
Enter a name: Alice
```

### Email filter

```text id="ex2"
What would you like to filter by? (name, email, age): email
Enter an email: alice@example.com
```

### Age filter

```text id="ex3"
What would you like to filter by? (name, email, age): age
Enter an age: 25
```

---

## ⚠️ Error Handling

Invalid inputs are handled safely:

* Wrong filter option:

```text id="err1"
Invalid filter option. Please choose 'name', 'email', or 'age'.
```

* Invalid age input:

```text id="err2"
Invalid input: age must be a number.
```

---

## 🧠 Learning Goals

This project demonstrates:

* Git branching workflow
* Feature-based development
* Python functions and modular design
* Working with JSON data
* Input validation and error handling
* Writing clean, maintainable code (PEP 8)

---

## 👨‍💻 Author

Patrick Förderer
