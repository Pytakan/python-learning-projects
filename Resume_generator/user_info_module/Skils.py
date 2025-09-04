class Skils:
    def __init__(self, skills_list:list):
        self.skills_list = skills_list
    
    def to_dict(self):
        return {
            "skills": self.skills_list
        }   
    def display(self):
        print("Skills:")
        for skill in self.skills_list:
            print(f"       {skill}")
    def add_skill(self, skill:str):
        if skill not in self.skills_list:
            self.skills_list.append(skill)
        else:
            raise ValueError("Skill already exists")
        
    def remove_skill(self, skill:str):
        if skill in self.skills_list:
            self.skills_list.remove(skill)
        else:
            raise ValueError("Skill not found") 
        
    def update_skill(self, old_skill:str, new_skill:str):
        if old_skill in self.skills_list:
            index = self.skills_list.index(old_skill)
            self.skills_list[index] = new_skill
        else:
            raise ValueError("Skill not found")
   
    def get_skills(self):
        return self.skills_list
    
    def clear_skills(self):
        self.skills_list = []

    def count_skills(self):
        return len(self.skills_list)