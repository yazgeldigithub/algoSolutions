def alphaNumericRestriction(input_str):
    if input_str.isalpha():
        return True
    elif input_str.isdigit():
        return True
    else:
        return False


print(alphaNumericRestriction("5dfg4"))

