import logging
import argparse

from models.admin import Admin
from models.contact import Contact
from models.user import User


def main():
    parser = argparse.ArgumentParser(description="Contact sharing system")
    parser.add_argument("--admin", action="store_true", help="Run as admin")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    if args.admin:
        admin = Admin()
        while True:
            command = input("Enter command: ")
            command_args = command.split(" ")

            if len(command_args)  <2:
                if command_args[0] == "users":
                    print (*admin.users)
                else:
                    print("Unknown command")

            if len(command_args)  >1:
                if command_args[0] == "add_user":
                    print(command_args[1])
                    admin.add_user(User(command_args[1]))

                elif command_args[0] == "remove_user":
                    admin.remove_user(User(command_args[1]))
                elif command_args[0] == "add_contact":
                    contact = Contact(User(command_args[1]), command_args[2], command_args[3])
                    admin.add_contact_to_any_phone_book(contact)
                else:
                    print("Unknown command")
    else:
        admin = Admin()

        user1 = User("Kolya")
        user2 = User("Ivan")

        admin.add_user(user1)
        admin.add_user(user2)

        user1.add_friend(user2)

        contact = Contact(user1, "+7", "123456789")
        user1.add_contact(contact, "family")

        contact = Contact(user1, "+808", "7778889911")
        user1.add_contact(contact, "work")

        user1.share(user1.friends[0], "family")

        admin.add_contact_to_any_phone_book(Contact(User("vanya"), "+7", "9832472434"))

        print(user1)


if __name__ == "__main__":
    main()
