# O(n^2) time and O(1) space memory 
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if((array[i] + array[j]) == targetSum):
                return array[i], array[j]
    return[]


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
