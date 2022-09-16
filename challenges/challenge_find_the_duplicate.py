def find_duplicate(nums):
    if not nums or len(nums) < 2 or type(nums) != list:
        return False

    for i in nums:
        if type(i) != int or i < 0:
            return False

    nums.sort()
    index = 0
    repeated_number = None

    while index < (len(nums) - 1):
        if nums[index] == nums[index + 1]:
            repeated_number = nums[index]
        index += 1
    if repeated_number is None:
        return False
    return repeated_number


if __name__ == "__main__":
    find_duplicate([1, 2, 2, 3])
