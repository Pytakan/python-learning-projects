class Education:
    def __init__(self):
        self.education_dict = {}
            
    def to_dict(self):
        return self.education_dict
    
    def add_education(self, institution_name:str, degree:str, field_of_study:str, duration:str, description:str):    
            if institution_name not in self.education_dict:
                self.education_dict[institution_name] = {
                    "degree": degree,
                    "field_of_study": field_of_study,
                    "duration": duration,
                    "description": description
                }
            else:
                raise ValueError("Education entry already exists")
            
    def display(self):
        print("Education:")
        for institution, details in self.education_dict.items():
            print(f"Institution: {institution}")
            for key, value in details.items():
                print(f"  {key}: {value}")

    def remove_education(self, institution_name:str):
        if institution_name in self.education_dict:
            del self.education_dict[institution_name]
        else:
            raise ValueError("Education entry not found")
    
    def update_education_period(self, institution_name:str, new_duration:str):
        if institution_name in self.education_dict:
            self.education_dict[institution_name]["duration"] = new_duration
        else:
            raise ValueError("Education entry not found")
    def update_education_degree(self, institution_name:str, new_degree:str):
        if institution_name in self.education_dict:
            self.education_dict[institution_name]["degree"] = new_degree
        else:
            raise ValueError("Education entry not found")
    def update_education_field_of_study(self, institution_name:str, new_field_of_study:str):
        if institution_name in self.education_dict:
            self.education_dict[institution_name]["field_of_study"] = new_field_of_study
        else:
            raise ValueError("Education entry not found")
    
    def update_education_description(self, institution_name:str, new_description:str):
        if institution_name in self.education_dict:
            self.education_dict[institution_name]["description"] = new_description
        else:
            raise ValueError("Education entry not found")
    
    def get_education(self):
        return self.education_dict
    def clear_education(self):
        self.education_dict = {}
    def count_education_entries(self):
        return len(self.education_dict)