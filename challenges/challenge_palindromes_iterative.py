def is_palindrome_iterative(word):
    string_size = len(word)

    if string_size == 0:
        return False

    for i in range(string_size // 2):
        if word[i] != word[string_size - i - 1]:
            return False

    return True
