class UserManager:
    def __init__(self):
        self.users = []
        self.admins = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, name):
        if name in self.users:
            self.users.remove(name)

    def add_admin(self, admin):
        self.admins.append(admin)

    def remove_admin(self, admin):
        if admin in self.admins:
            self.users.remove(admin)

    def find_admin(self, admin):
        for admin in self.admins:
            if admin == admin:
                return admin