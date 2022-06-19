############################
##### Assignment_02.py #####
############################


import math


from hashlib import md5


def Solution1(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


def Solution2(no, works):
    while no > 0:
        works.sort()

        if works[-1] <= 0:
            break

        works[-1] -= 1
        no -= 1

    return sum([i ** 2 for i in works])


def Solution3(s):
    stack = []

    for characterOfS in s:
        if len(stack) == 0:
            stack.append(characterOfS)
        else:
            if stack[-1] == characterOfS:
                stack.pop()
            else:
                stack.append(characterOfS)

    if len(stack) == 0:
        return 1
    else:
        return 0


def Solution4(n):
    arr = [1, 1]

    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n - 1]


def Solution5():
    result = ""
    string = input()

    for i in range(len(string)):
        if string[i].islower():
            result += string[i].upper()
        else:
            result += string[i].lower()

    print(string)


def Solution6(n, m, numbers):
    check = set()

    for elementsOfNumbers in numbers:
        for i in range(elementsOfNumbers, m + 1, elementsOfNumbers):
            if i >= n:
                check.add(i)

    return sum(check)


def Solution7(message, n):
    answer = ""

    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                answer += chr((ord(message[i]) + n - 65) % 26 + 65)
            else:
                answer += chr((ord(message[i]) + n - 97) % 26 + 97)
        else:
            answer += message[i]

    return answer


def Solution8():
    a, b = map(int, input().strip().split(' '))

    print(math.gcd(a, b))
    print(int(abs(a * b) / math.gcd(a, b)))


def Solution9(string1, string2):
    answer = 0

    string1_hashed = md5(bytes(string1, encoding='utf8')).hexdigest()
    string2_hashed = md5(bytes(string2, encoding='utf8')).hexdigest()

    for i in range(len(string1_hashed)):
        if string1_hashed[i] != string2_hashed[i]:
            answer += 1

    return answer


def Solution10():
    count = 1
    num = int(input())

    for i in range(num):
        for j in range(i + 1):
            print(count, end=' ')
            count += 2
        print()
