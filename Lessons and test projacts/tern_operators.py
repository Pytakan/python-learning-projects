limit_str="Hello!"

result= "String is short" if len(limit_str)<10 else "String is long"
print(result)


def dict_to_list(some_dict):
    result = []
    for key, value in some_dict.items():
        result.append((key, value * 2 if isinstance(value, int) else value))
    return result

print(dict_to_list({'name': 'John', 'age': 25, 'city': 'New York'}))