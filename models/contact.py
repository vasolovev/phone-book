class Contact:

    def __init__(self, user, country_code, phone_number):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number

    def __repr__(self):
        return f"Contact(user={self.user.name!r}, country_code={self.country_code!r}, phone_number={self.phone_number!r})"
