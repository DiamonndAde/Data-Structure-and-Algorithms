# O(n) time and O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialSearch = targetSum - num
        if potentialSearch in nums:
            return [potentialSearch, num]
        else:
            nums[num] = True
    return[]


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
