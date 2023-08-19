def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    first = word[low_index]
    last = word[high_index]

    if first != last:
        return False

    if low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
