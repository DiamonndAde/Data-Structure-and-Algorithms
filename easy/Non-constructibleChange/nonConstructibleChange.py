# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    coins.sort()

    currentChange = 0

    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1

        currentChange += coin

    return currentChange + 1


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
