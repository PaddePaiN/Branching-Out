# Branching-Out
Codio Assessment

# Branching-Out

A simple Python application that loads user data from a JSON file and allows filtering users by name, email, or age.

## Features

* Filter users by name (case-insensitive)
* Filter users by email (case-insensitive)
* Filter users by age
* Interactive command-line interface
* User-friendly error handling
* PEP 8 compliant code

## Requirements

* Python 3.10+

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Branching-Out.git
```

Navigate to the project directory:

```bash
cd Branching-Out
```

## Usage

Run the application:

```bash
python main.py
```

Choose a filter option:

```text
What would you like to filter by? (name, email, age):
```

### Example

```text
What would you like to filter by? (name, email, age): email
Enter an email: alice@example.com
```

## Project Structure

```text
Branching-Out/
├── main.py
├── users.json
└── README.md
```

## Available Filters

### Name

Searches for users by name.

### Email

Searches for users by email address.

### Age

Searches for users by age.

## Error Handling

Invalid filter options are handled gracefully:

```text
Invalid filter option. Please choose 'name', 'email', or 'age'.
```

## Learning Goals

This project was created to practice:

* Git branching strategies
* Feature development workflows
* Creating meaningful commits
* GitHub collaboration
* JSON processing in Python
* Writing clean, maintainable Python code

## Author

Patrick Förderer

```
```

