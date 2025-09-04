from pprint import pprint
from Resume_generator.console_ui.utils import clear_screen
from Resume_generator.user_info_module.Contacts import Contacts
from Resume_generator.user_info_module.Skils import Skils 
from Resume_generator.user_info_module.Exireance import Expirence
from Resume_generator.user_info_module.Education import Education
import json
class Persone:
    def __init__(self, name:str, birthday:str, contacts:Contacts,skils:Skils,
                  expirence:Expirence, education:Education):
        self.name = name
        self.birthday = birthday
        self. contacts = contacts
        self.skils = skils
        self.experience = expirence
        self.education = education
    
    def to_dict(self):
        return {
            "name": self.name,
            "birthday": self.birthday,
            "contacts": self.contacts.to_dict(),
            "skills": self.skils.to_dict(),
            "experience": self.experience.to_dict(),
            "education": self.education.to_dict()
        }
    def show_info(self):
        clear_screen()
        print(f"Name: {self.name}")
        print(f"Birthday: {self.birthday}")
        self.contacts.display()
        self.skils.display()
        self.experience.display()
        self.education.display()
    def get_name(self):
        return self.name
    
    def get_birthday(self):
        return self.birthday

    def get_contacts(self):
        return self.contacts

    def get_skills(self):
        return self.skils

    def get_experience(self):
        return self.experience

    def get_education(self):
        return self.education

    def convert_to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def update_name(self, new_name:str):
        self.name = new_name

    def update_birthday(self, new_birthday:str):
        self.birthday = new_birthday

    def update_contacts(self, new_contacts:Contacts):
        self.contacts = new_contacts
    def update_skils(self, new_skils:Skils):
        self.skils = new_skils
    def update_experience(self, new_experience:Expirence):
        self.experience = new_experience
    def update_education(self, new_education:Education):
        self.education = new_education
    