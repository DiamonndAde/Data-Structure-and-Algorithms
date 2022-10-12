# O(n) time and O(1) space
def isValidateSubstring(array, sequence):
    seqPos = 0
    for num in array:
        if seqPos == len(sequence):
            return True
        if num == sequence[seqPos]:
            seqPos += 1
    return seqPos == len(sequence)


print(isValidateSubstring([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
