import re
def redact_phone_numbers(document):
    phone_pattern = r'\+84\d+|\d{10}'
    return re.sub(phone_pattern, '[REDACTED]', document)