import re
def sum_numbers_in_paragraph(text):
    numbers = re.findall(r'\d+', text)
    return sum(int(number) for number in numbers)