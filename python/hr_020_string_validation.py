if __name__ == '__main__':
    string = input()
    any_alphanumeric = False
    any_alphabetic = False
    any_digit = False
    any_low = False
    any_up = False
    for char in string:
        if (not any_alphanumeric and char.isalnum()):
            any_alphanumeric = True
        if (not any_alphabetic and char.isalpha()):
            any_alphabetic = True
        if (not any_digit and char.isdigit()):
            any_digit = True
        if (not any_low and char.islower()):
            any_low = True
        if (not any_up and char.isupper()):
            any_up = True
        
    print(any_alphanumeric)
    print(any_alphabetic)
    print(any_digit)
    print(any_low)
    print(any_up)
