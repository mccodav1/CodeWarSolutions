def validBraces(string):
    if len(string) % 2 == 1:
        return False
    else:
        if string[0] == string[-1]:
            if len(string) == 2:
                return True
            else:
                validBraces(string[1:-1])
        else:
            return False



print(validBraces(r"(){}[]"))
print(validBraces(r"([{}])"))
print(validBraces(r"(}"))
print(validBraces(r"[(])"))
print(validBraces(r"[({})](]"))


