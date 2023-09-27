def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first = list(first_string.lower())
    second = list(second_string.lower())

    if len(first) != len(second_string):
        return False

    for row in first:
        if row in second:
            second.remove(row)
        else:
            return False
    return True
