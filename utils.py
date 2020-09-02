#will have functions to make main.py clean
import string
import random

def save_file(response_bytes, file_path):
    pass

def mark_link_crw(link, status_code):
    pass

def get_random_file_name(content_type):
    #create a random string
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
    extension = ''

    if 'image/png' in content_type:
        extension = '.png'
    elif 'image/jpeg' in content_type:
        extension = '.jpeg'
    elif 'image/pdf' in content_type:
        extension = '.pdf'
    elif 'image/mpeg' in content_type:
        extension = '.mpeg'
    elif 'image/jpg' in content_type:
        extension = '.jpg'
