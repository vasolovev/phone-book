from models.phonebook import PhoneBook


class User:

    def __init__(self, name):
        self.name = name
        self.friends = []
        self.phoneBooks = {}

    def __repr__(self):
        friend_names = "\n".join([friend.name for friend in self.friends])
        phone_books_info = '\n'.join(f"{key}: {value!r}" for key, value in self.phoneBooks.items())

        return f"{self.name}\nFriends: {friend_names}\nPhone Books:\n{phone_books_info}"

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    def add_contact(self, contact, tag):
        if tag not in self.phoneBooks:
            self.phoneBooks[tag] = PhoneBook(tag)
        self.phoneBooks[tag].add_contact(contact)

    def add_phone_book(self, tag, phone_book):
        self.phoneBooks[tag]=phone_book


    def share(self, friend, tag):
        if friend not in self.friends:
            print(f"{friend.name} is not your friend!")
            return
        if tag not in self.phoneBooks:
            print(f"You don't have a phone book with tag {tag}!")
            return
        friend.add_phone_book(tag, self.phoneBooks[tag])
