def string_check(string):
    if string.isupper():
        return ("Already in UpperCase")
    else:
        string = string.upper()
        return string

print(string_check("Hello"))
