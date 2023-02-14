def romanToInt(s: str):
    dict = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    num = 0
    last = ''
    for i in s :
        num += dict[i]
        if (i == 'V' or i == 'X') and (last == 'I'):
            num -= dict[last] + dict[last]
        elif (i == 'L' or i == 'C') and (last == 'X'):
            num -= dict[last] + dict[last]
        elif (i == 'M' or i == 'D') and (last == 'C'):
            num -= dict[last] + dict[last]
        last = i
    print(num)

romanToInt('III')