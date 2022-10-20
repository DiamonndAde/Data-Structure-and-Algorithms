# O(n) time and O(1) space memory 
def isValidateSubstring(array, sequence):
    arrPos = 0
    seqPos = 0
    while arrPos < len(array) and seqPos < len(sequence):
        if array[arrPos] == sequence[seqPos]:
            seqPos += 1
        arrPos += 1
    return seqPos == len(sequence)


print(isValidateSubstring([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
