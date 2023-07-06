def find_duplicate(nums):
    if not isinstance(nums, list) or any(not isinstance(num, int) for num in nums):
        return False

    counter = {}

    for num in nums:
        if num <= 0:
            continue

        if num in counter:
            return num
        else:
            counter[num] = 1

    return False
