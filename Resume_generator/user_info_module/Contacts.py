class Contacts:
    def __init__(self, email:str, phone:str, linkedin:str, adress:str):
        self.email = email
        self.phone = phone
        self.linkedin = linkedin
        self.adress = adress

    def to_dict(self):
        return {
            "email": self.email,
            "phone": self.phone,
            "linkedin": self.linkedin,
            "adress": self.adress
        }
    def display(self):
        print("Contacts:")
        print(f"    Email: {self.email}")
        print(f"    Phone: {self.phone}")
        print(f"    LinkedIn: {self.linkedin}")
        print(f"    Address: {self.adress}")

    def update_email(self, new_email:str):
        self.email = new_email
    def update_phone(self, new_phone:str):
        self.phone = new_phone
    def update_linkedin(self, new_linkedin:str):
        self.linkedin = new_linkedin
    def update_adress(self, new_adress:str):
        self.adress = new_adress
    def get_contacts(self):
        return self.to_dict()
    def clear_contacts(self):
        self.email = ""
        self.phone = ""
        self.linkedin = ""
        self.adress = ""
    def is_empty(self):
        return not any([self.email, self.phone, self.linkedin, self.adress])
