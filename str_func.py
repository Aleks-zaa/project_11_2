def string_check(string):
    """Функция возвращает заглавные буквы"""
    if string.isupper():
        return ("Already in UpperCase")
    else:
        string = string.upper()
        return string


# print(string_check("Hello"))

def string_title(string):
    """Функция возвращает заглавные буквы всем словам"""
    string = string.title()
    return string


print(string_title("dfggh fgdj"))