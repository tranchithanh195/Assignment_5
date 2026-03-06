import re

def is_valid_course_code(code):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.fullmatch(pattern, code))