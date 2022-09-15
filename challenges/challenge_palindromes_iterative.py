def is_palindrome_iterative(word):
    low_index = 0
    high_index = len(word) - 1

    if not word:
        return False

    for idx in range(len(word)):
        if word[low_index] != word[high_index]:
            return False
        elif idx >= high_index:
            return True

        low_index += 1
        high_index -= 1
