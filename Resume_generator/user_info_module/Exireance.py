class Expirence:
    
    def __init__(self):
        self.expireance_dict = {}

    def to_dict(self):
        return self.expireance_dict
    
    def display(self):
        print("Experience:")
        for company, details in self.expireance_dict.items():
            print(f"Company: {company}")
            for key, value in details.items():
                print(f"  {key}: {value}")
    
    def add_experience(self, company_name:str, role:str, duration:str, description:str):    
            self.expireance_dict[company_name] = {
                "role": role,
                "duration": duration,
                "description": description
            }
    def find_experience_by_company_name(self, company_name:str):
        return self.expireance_dict.get(company_name, None)
    def find_experience_by_role(self, role:str):
        results = []
        for company, details in self.expireance_dict.items():
            if details["role"] == role:
                results.append({company: details})
        return results
    def find_experience_by_year(self, year:str):
        results = []
        for company, details in self.expireance_dict.items():
            if details["duration"].startswith(year) or details["duration"].endswith(year):
                results.append({company: details})
        return results
    def remove_experience(self, company_name:str):
        if company_name in self.expireance_dict:
            del self.expireance_dict[company_name]
        else:
            raise ValueError("Experience not found")    
    
    def update_experience_period(self, company_name:str, new_duration:str):
        if company_name in self.expireance_dict:
            self.expireance_dict[company_name]["duration"] = new_duration
        else:
            raise ValueError("Experience not found")    
    def update_experience_role(self, company_name:str, new_role:str):
        if company_name in self.expireance_dict:
            self.expireance_dict[company_name]["role"] = new_role
        else:
            raise ValueError("Experience not found")
    def update_experience_description(self, company_name:str, new_description:str):
        if company_name in self.expireance_dict:
            self.expireance_dict[company_name]["description"] = new_description
        else:
            raise ValueError("Experience not found")
        
    def get_experience(self):
        return self.expireance_dict
    
    def clear_experience(self):
        self.expireance_dict = {}

    def count_experiences(self):
        return len(self.expireance_dict)    