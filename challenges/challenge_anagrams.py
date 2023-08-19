def is_anagram(first_string, second_string):
    if (len(first_string) < 1 and len(second_string) < 1):
        return ('', '', False)
    sorted1 = merge_sort(list(first_string.lower()))
    sorted2 = merge_sort(list(second_string.lower()))

    if len(first_string) != len(second_string):
        return (''.join(sorted1), ''.join(sorted2), False)
    return (''.join(sorted1), ''.join(sorted2), sorted1 == sorted2)


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


print(is_anagram('roma', 'amor'))
print(is_anagram('rio', 'ryo'))
print(is_anagram('pedra', 'perdaaa'))
