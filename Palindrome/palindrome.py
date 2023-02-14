def isPalindrome(x):
    reverseNum = 0
    num = x
    while x > 0:
        reverseNum = (reverseNum * 10) + (x % 10)
        x = x // 10
    print(x)
    print(reverseNum)
    if num == reverseNum :
        return True
    else:
        return False

print(isPalindrome(-121))
