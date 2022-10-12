# O(nlog(n)) time and O(n) space
def sortSquaredArray(array):
    sortedArray = []
    for num in array:
        sortedArray.append(num**2)
    sortedArray.sort()
    return(sortedArray)


print(sortSquaredArray([-6, -7, 1, 2, 3, 4, 5]))
