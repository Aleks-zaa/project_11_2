def string_check(string):
    """Функция возвращает заглавные буквы  """
    if string.isupper():
        return ("Already in UpperCase")
    else:
        string = string.upper()
        return string

print(string_check("Hello"))
