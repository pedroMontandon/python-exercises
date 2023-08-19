def is_palindrome_iterative(word):
    if (len(word) < 1):
        return False
    for index in range(len(word) // 2):
        if word[index] != word[len(word) - 1 - index]:
            return False
    return True


print(is_palindrome_iterative(''))
print(is_palindrome_iterative('SOCOS'))
print(is_palindrome_iterative('REVIVER'))
print(is_palindrome_iterative('COXINHA'))
print(is_palindrome_iterative('AGUA'))
