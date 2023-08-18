def is_anagram(first_string, second_string):

    
    
    # word1 = ''.join(sorted(first_string.lower()))
    # word2 = ''.join(sorted(second_string.lower()))
    # if len(first_string) != len(second_string):
    #     return (word1, word2, False)
    
    # for index in range(len(word1)):
    #     if first_string[index] != second_string[len(first_string) - 1 - index]:
    #         return (word1, word2, False)
    # return (word1, word2, True)

print(is_anagram('roma', 'amor'))
print(is_anagram('rio', 'ryo'))
print(is_anagram('pedra', 'perdaaa'))

# tem que ser O(n log n)
