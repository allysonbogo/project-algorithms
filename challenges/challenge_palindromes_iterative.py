def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    reverse = "".join(reversed(word))

    if reverse == word:
        return True

    return False
