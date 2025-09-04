import random


from Resume_generator.user_info_module.Contacts import Contacts
from Resume_generator.user_info_module.Skils import Skils
from Resume_generator.user_info_module.Exireance import Expirence
from Resume_generator.user_info_module.Education import Education
from Resume_generator.user_info_module.Persone import Persone


COUNTRIES = [
    ("United States", "+1", "New York"),
    ("United Kingdom", "+44", "London"),
    ("Germany", "+49", "Berlin"),
    ("Canada", "+1", "Toronto"),
    ("Australia", "+61", "Sydney"),
    ("India", "+91", "Bengaluru"),
    ("Netherlands", "+31", "Amsterdam"),
    ("France", "+33", "Paris"),
    ("Italy", "+39", "Rome"),
    ("Spain", "+34", "Madrid"),
    ("Sweden", "+46", "Stockholm"),
    ("Norway", "+47", "Oslo"),
    ("Switzerland", "+41", "Zurich"),
    ("Japan", "+81", "Tokyo"),
    ("South Korea", "+82", "Seoul"),
    ("Brazil", "+55", "São Paulo"),
    ("Mexico", "+52", "Mexico City"),
    ("Russia", "+7", "Moscow"),
    ("China", "+86", "Beijing"),
    ("South Africa", "+27", "Cape Town"),
]

FIRST_NAMES = [
    "Alex", "Maria", "John", "Sara", "Liam", "Noah", "Emma", "Olivia",
    "Sophia", "Ava", "Mia", "Isabella", "Charlotte", "Steven", "Andrew",
    "James", "Emily", "Benjamin", "Grace", "Lucas", "Ella", "Michael", "Chloe",
    "Daniel", "Amelia", "Matthew", "Harper", "David", "Abigail", "Joseph", "Madison",
    "Samuel", "Elizabeth", "Henry", "Scarlett", "Jack", "Victoria", "Leo", "Penelope",
    "William", "Layla", "Ethan", "Aria", "Jacob", "Lily", "Mason", "Zoey"
]

LAST_NAMES = [
    "Smith", "Johnson", "Brown", "Taylor", "Miller", "Wilson", "Davis", "Garcia",
    "Martinez", "Anderson", "Thomas", "Jackson", "White", "Harris", "Clark", "Lewis",
    "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker",
    "Adams", "Nelson", "Hill", "Ramirez", "Campbell", "Mitchell", "Roberts", "Carter",
    "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart"
]

def person_creator():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    name = f"{first_name} {last_name}"
    day = input("Enter day of birth (DD): ")
    month = input("Enter month of birth (MM): ")
    year = input("Enter year of birth (YYYY): ")
    birthday = f"{year}-{month}-{day}"
    country = input("Enter your country of residence: ")
    city = input("Enter your city: ")
    postcode = input("Enter your postal code: ")
    adress = f"{city}, {postcode}, {country}"
    email = input("Enter your email: ")
    phone = input("Enter your phone number (with country code): ")
    linkedin = input("Enter your LinkedIn profile URL: ")
    contacts = Contacts(email=email, phone=phone, linkedin=linkedin, adress=adress)
    skills_input = input("Enter your skills (comma-separated): ")
    skills_list = [skill.strip() for skill in skills_input.split(",")]
    skills = Skils(skills_list)

    exp = Expirence()
    exp.add_experience("Acme Corp", "Software Engineer", "2017-2023", "Backend services and integrations")
    exp.add_experience("Tech Solutions", "Junior Developer", "2015-2017", "Frontend development")
    exp.add_experience("Web Start", "Intern", "2014-2015", "Assisted in web development")
    exp.add_experience("Code Factory", "Trainee", "2013-2014", "Learned coding basics")

    edu = Education()
    edu.add_education("State University", "BSc", "Computer Science", "2013-2017", "Major in CS")
    edu.add_education("City College", "Diploma", "IT Fundamentals", "2011-2013", "Basic IT courses")

    return Persone(name, birthday, contacts, skills, exp, edu)


def person_generator():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    name = f"{first} {last}"

    year = random.randint(1978, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birthday = f"{year:04d}-{month:02d}-{day:02d}"

    country, dial, city = random.choice(COUNTRIES)
    phone = f"{dial}{random.randint(10**8, 10**9 -1)}"

    contacts = Contacts(
        email=f"{first.lower()}.{last.lower()}@example.com",
        phone=phone,
        linkedin=f"https://www.linkedin.com/in/{first.lower()}{last.lower()}",
        adress=f"{city}, {country}"
    )

    skills = Skils(["Python", "APIs", "Docker"])

    exp = Expirence()
    exp.add_experience("Acme Corp", "Software Engineer", "2017-2023", "Backend services and integrations")
    exp.add_experience("Tech Solutions", "Junior Developer", "2015-2017", "Frontend development")
    exp.add_experience("Web Start", "Intern", "2014-2015", "Assisted in web development")
    exp.add_experience("Code Factory", "Trainee", "2013-2014", "Learned coding basics")
   
    edu = Education()
    edu.add_education("State University", "BSc", "Computer Science", "2013-2017", "Major in CS")
    edu.add_education("City College", "Diploma", "IT Fundamentals", "2011-2013", "Basic IT courses")

    return Persone(name, birthday, contacts, skills, exp, edu)
    

def path_generator(file_name:str):
    return f"C:/Users/sokso/OneDrive/Документы/Python Projcts/Resume_generator/resumes/{file_name}.pdf"