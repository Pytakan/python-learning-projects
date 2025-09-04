# functionn image_info принимает обязательный параметр dict с двумя обязательными клбчами image_id and image_title ключей может приниматся много но обязательных 2
def image_info(image_dict, **kwargs):
    if ('image_id' not in image_dict or 'image_title' not in image_dict) and type(image_dict) is dict:
        raise TypeError("image_dict must contain 'image_id' and 'image_title' keys.")
    
    return f"Image '{image_dict['image_title']}' hase id {image_dict['image_id']}"
    
   

try:
    img = {'image_id': 101, 'image_title': 'Sunset', 'resolution': '1920x1080'}
    print(image_info(img))
    
    img_invalid = {'image_title': 'Sunset'}
    print(image_info(img_invalid))
except TypeError as e:
    print(f"Error: {e}")