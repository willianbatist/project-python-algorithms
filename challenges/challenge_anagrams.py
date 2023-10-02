def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False


    if len(first) != len(second_string):
        return False

    for row in first:
        if row in second:
            second.remove(row)
        else:
            return False
    return True
