def is_palindrome_recursive(word, low_index, high_index):
    int_low_index = int(low_index)
    int_high_index = int(high_index)
    if len(word) == 0:
        return False
    elif word[int_low_index] != word[int_high_index]:
        return False
    elif int_low_index >= int_high_index:
        return True

