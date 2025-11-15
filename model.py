class Contact:

    def __init__(self, name, phone, email, date_of_birth, id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.date_of_birth = date_of_birth
        self.id = id

    def __str__(self):
        return self.name
