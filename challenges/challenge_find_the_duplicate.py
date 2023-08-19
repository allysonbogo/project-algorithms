def find_duplicate(nums):
    if not check_array(nums):
        return False

    nums.sort()

    for i in range(0, len(nums)):
        if i == len(nums) - 1:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]


def check_array(array):
    if len(array) <= 1 or type(array) == str:
        return False

    for num in array:
        if type(num) == str:
            return False
        if num <= 0:
            return False

    return True
