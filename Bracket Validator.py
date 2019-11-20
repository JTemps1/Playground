def validator(string):
    bracks = []
    for char in string:
        if char == '(' or char == '{' or char == '[':
            bracks.append(char)
        elif char == ')':
            if bracks[-1] == '(':
                del bracks[-1]
            else:
                return False
        elif char == '}':
            if bracks[-1] == '{':
                del bracks[-1]
            else:
                return False
        elif char == ']':
            if bracks[-1] == '[':
                del bracks[-1]
            else:
                return False
        else:
            pass
    
    if len(bracks) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    test = input('Enter bracket string: ')
    result = validator(test)

    if result == True:
        print('Valid string!\n')
    else:
        print('Invalid string\n')