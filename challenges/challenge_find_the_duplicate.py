def find_duplicate(nums):
    try:
        numbers = sorted(nums)
        past_number = None
        for number in numbers:
            if past_number == number and number > 0:
                return past_number
            past_number = number
        return False
    except TypeError:
        return False
