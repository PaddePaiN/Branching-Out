import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user.get("age") == age
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]

    for user in filtered_users:
        print(user)


def main():
    filter_option = input(
        "What would you like to filter by? (name, email, age): "
    ).strip().lower()

    if filter_option == "name":
        name = input("Enter a name: ").strip()
        filter_users_by_name(name)

    elif filter_option == "email":
        email = input("Enter an email: ").strip()
        filter_users_by_email(email)

    elif filter_option == "age":
        try:
            age = int(input("Enter an age: ").strip())
            filter_users_by_age(age)
        except ValueError:
            print("Invalid input: age must be a number.")

    else:
        print("Invalid filter option. Please choose 'name', 'email', or 'age'.")


if __name__ == "__main__":
    main()
