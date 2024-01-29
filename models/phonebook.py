class PhoneBook:

    def __init__(self, tag):
        self.tag = tag
        self.contacts = []

    def __repr__(self):
        return f"PhoneBook(tag={self.tag!r}, contacts={self.contacts!r})"

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def get_contacts_by_country_code(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def get_contacts_by_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]