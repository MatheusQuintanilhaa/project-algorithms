"""Linter"""


def quick_sort(word, start, end):
    """
    Linter
    """
    if start < end:
        par = partition(word, start, end)
        quick_sort(word, start, par - 1)
        quick_sort(word, par + 1, end)


def partition(word, start, end):
    """
    Linter
    """
    pivot = word[end]
    delimiter = start - 1

    for index in range(start, end):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[index], word[delimiter] = word[delimiter], word[index]

    word[delimiter + 1], word[end] = word[end], word[delimiter + 1]

    return delimiter + 1


def order_word(word):
    """
    Linter
    """
    letters = list(word)

    quick_sort(letters, 0, len(letters) - 1)
    sorted_letters = "".join(letters)

    return sorted_letters


def is_anagram(first_string, second_string):
    """
    Linter
    """
    if first_string == '' and second_string == '':
        return ('', '', False)
    first = first_string.lower()
    second = second_string.lower()

    word_first = order_word(first)
    word_second = order_word(second)
    verification = word_first == word_second

    return (word_first, word_second, verification)
