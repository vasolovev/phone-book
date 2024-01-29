class Admin:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def add_contact_to_any_phone_book(self, contact):
        for user in self.users:
            for tag in user.phoneBooks:
                user.phoneBooks[tag].add_contact(contact)

    def delete_contact_to_any_phone_book(self, contact):
        for user in self.users:
            for tag in user.phoneBooks:
                user.phoneBooks[tag].remove_contact(contact)