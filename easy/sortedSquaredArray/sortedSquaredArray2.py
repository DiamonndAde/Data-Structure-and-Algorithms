# O(n) time and O(n) space
def sortSquaredArray(array):
    left = 0
    right = len(array) - 1
    sortedArray = [0 for _ in array]
    for num in reversed(range(len(array))):
        leftSquared = (array[left]) ** 2
        rightSquared = (array[right]) ** 2
        if leftSquared > rightSquared:
            sortedArray[num] = leftSquared
            left += 1
        else:
            sortedArray[num] = rightSquared
            right -= 1
    return(sortedArray)


print(sortSquaredArray([-9, -8, -7, -6, 1, 2, 3, 4, 5]))
