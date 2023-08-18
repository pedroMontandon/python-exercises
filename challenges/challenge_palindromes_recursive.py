def is_palindrome_recursive(word, low_index, high_index):
    try:
        if word[low_index] != word[high_index]:
            return False
        if len(word) / 2 >= high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False


print(is_palindrome_recursive('ANA', 0, len('ANA') - 1))
print(is_palindrome_recursive('SOCOS', 0, len('SOCOS') - 1))
print(is_palindrome_recursive('REVIVER', 0, len('REVIVER') - 1))
print(is_palindrome_recursive('COXINHA', 0, len('COXINHA') - 1))
print(is_palindrome_recursive('AGUA', 0, len('AGUA') - 1))