from models.user import User


class Admin(User):
    def __init__(self, name):
        self.user = User(name)

    def add_contact(self, users, user, contact, tag):
        for u in users:
            if u == user:
                user.add_contact(contact, tag)

    def delete_contact(self, users, user, contact, tag):
        for u in users:
            if u == user:
                if tag in user.phoneBooks:
                    user.phoneBooks[tag].remove_contact(contact)
