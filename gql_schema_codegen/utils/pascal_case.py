import re


def pascal_case(string: str):
    cleaned_string = string.replace(" ", "")
    first_letter = re.search(r'\w', cleaned_string)
    if not first_letter:
        return ''

    return cleaned_string[:first_letter.start() + 1].upper() + cleaned_string[first_letter.start() + 1:]
