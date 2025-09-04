import json
# generate json data
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

json_data = json.dumps(data, indent=4) # convert Python object to JSON string with indentation for readability
print(json_data) # print the JSON string
print(type(json_data)) # check the type to confirm it's a string
tmp = json.loads(json_data) # convert JSON string back to Python object
print(tmp['name']) # access data from the Python object