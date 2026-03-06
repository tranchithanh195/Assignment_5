import re
def is_valid_hex_code(color_code):
    pattern = r'^#[0-9a-fA-F]{6}$'
    return bool(re.fullmatch(pattern, color_code))