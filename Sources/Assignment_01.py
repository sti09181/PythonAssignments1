############################
##### Assignment_01.py #####
############################


from itertools import combinations


def Solution1(arr):
    arr.sort()

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return False

    return True


def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def Solution2(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for i in arr:
        if isPrimeNumber(sum(i)):
            answer += 1
    return answer


def Solution3(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            answer.append(arr[i])

    return answer


def Solution4(nums):
    ableToGet = len(nums) / 2
    variant = len(list(set(nums)))

    if ableToGet < variant:
        return ableToGet
    else:
        return variant


def Solution5(v):
    answer = [0, 0]

    for x, y in v:
        answer[0] ^= x
        answer[1] ^= y

    return answer


def Solution6(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer


def Solution7(n, m):
    answer = 0

    for number in range(n, m + 1):
        answer += 1
        numberToStr = str(number)
        for i in range(0, (len(numberToStr) // 2)):
            if numberToStr[i] != numberToStr[len(numberToStr) - i - 1]:
                answer -= 1
                break

    return answer


def Solution8(n, c, x):
    leftOver = n + c
    answer = n

    while leftOver >= x:
        leftOver -= x - 1
        answer += 1

    return answer


def Solution10(logs):
    answer = []

    logs.sort()

    target = 0

    while target < len(logs):
        count = 1
        duplicationScan = target + 1
        while duplicationScan < len(logs):
            if logs[duplicationScan - 1] != logs[duplicationScan]:
                break
            duplicationScan += 1
            count += 1

        if count % 2 != 0:
            answer.append(logs[target])

        target = duplicationScan

    return answer
