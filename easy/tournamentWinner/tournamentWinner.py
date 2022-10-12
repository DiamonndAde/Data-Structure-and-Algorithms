def tournamentWinner(array, arrSol):
    python = 0
    cSharp = 0
    html = 0
    for num in range(len(array)):
        if arrSol[num] == 0:
            if array[num][1] == "python":
                python += 1
            elif array[num][1] == "c#":
                cSharp += 1
            else:
                html += 1
        else:
            if array[num][0] == "python":
                python += 1
            elif array[num][0] == "c#":
                cSharp += 1
            else:
                html += 1
    if python > cSharp and python > html:
        return "python"
    elif cSharp > python and cSharp > html:
        return "c#"
    else:
        return "html"


print(tournamentWinner(
    [["html", "c#"], ["c#", "python"], ["python", "html"]], [0, 0, 1]))

# def matrixArr(arr):
# lr = 0
# rl = 0
# k = len(arr) - 1
# while k >= 0:
#     for i in range(len(arr)):
#         lr += arr[i][i]
#         rl += arr[i][k]
#         k -= 1

# SECOND SOLUTION
#     right = len(arr) - 1
#     lr = 0
#     rl = 0
#     i = 0
#     while i < len(arr):
#         lr += arr[i][i]
#         rl += arr[i][right]
#         right -= 1
#         i += 1
#     return (rl - lr)


# print(matrixArr([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))
