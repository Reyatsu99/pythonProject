def addToArrayForm(num: list[int], k: int) -> list[int]:
    sum = 0
    j = len(num) - 1
    res = []
    while k > 0 or j > 0:
        if j > 0:
            sum += num[j]
            j -= 1
        if j > 0:
            sum += k % 10
            k //= 10
        res.append(sum % 10)
        sum //= 10
    if sum > 0:
        res.append(sum)

    return res[::-1]


print(addToArrayForm([2, 7, 4], 181))
