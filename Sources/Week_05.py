######################
##### Week_05.py #####
######################


import math
import time


def Solution1():
    result = 0
    number = int(input("Enter a number : "))

    for count in range(number, number + 1):
        result += count

    print(result)


def Solution2():
    exp = 0
    x = int(input("Enter a number : "))

    for i in range(100):
        exp += x ** 1 / math.factorial(i)

    sigmoid = 1 / (1 + 1 / exp)

    print(exp)
    print(sigmoid)


def Solution3():
    number = int(input("Enter a number : "))

    startTime = time.time()

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"{number} is composite number")
            break
    else:
        print(f"{number} is prime number")

    print(f"Time taken around {time.time() - startTime} seconds")


def Solution4():
    year = 0
    balance = 1000000

    while balance < 2000000:
        year += 1
        balance = int(balance * 1.05)

    print(f"Estimated time : {year} years")


def Solution5():
    count = 0

    timeTaken = time.time() + 10

    while time.time() < timeTaken:
        count += 1

    print(f"Calculated about {count} times")


def Solution6():
    first = 1

    while first < 10:
        second = 1

        while second < 10:
            print(f"{first} * {second} = {first * second}")
            second += 1

        first += 1
        print()


def Solution7():
    number = int(input("Enter a number : "))
    for row in range(number):
        for dummy in range(row + 1):
            print("*", end="")
        print()


def Solution8():
    number = int(input("Enter a number : "))
    for row in range(number):
        for dummy in range(number - row - 1):
            print(end=" ")
        for dummy in range(row + 1):
            print("*", end="")
        print()


def Solution9():
    number = int(input("Enter a number : "))
    for row in range(number, 0, -1):
        for dummy in range(row):
            print("*", end="")
        print()


def Solution10():
    number = int(input("Enter a number : "))
    for row in range(number, 0, -1):
        for dummy in range(number - row):
            print(end=" ")
        for dummy in range(row):
            print("*", end="")
        print()


def Solution11():
    number = int(input("Enter a number : "))
    count = 1
    for row in range(number):
        for dummy in range(row + 1):
            print(count, end=" ")
            count += 1
        print()


def Solution12():
    number = int(input("Enter a number : "))
    for row in range(1, number + 1):
        calculate = row
        for col in range(row):
            print(calculate, end=" ")
            calculate += number - col - 1
        print()


def Solution13():
    for n in range(1, 5):
        print(f"n = {n}")
        for a in range(1, 101):
            for b in range(a, 101):
                for c in range(b + 1, 101):
                    if a ** n + b ** n == c ** n:
                        print(f"a : {a}, b : {b}, c: {c}")
        else:
            print("Complete!")


def Solution14():
    for n in range(1, 101):
        harmonicSeries = 0
        for count in range(1, n + 1):
            harmonicSeries += 1 / count
        print(f"if n = {n} than harmonic series of n : {harmonicSeries}")
        print(f"ln {n + 1} : {math.log(n + 1)}")
        print(f"error : {harmonicSeries - math.log(n + 1)}")
        print()


#####################
##### Homeworks #####
#####################


def Homework():
    number = int(input("Enter a number : "))
    for row in range(1, number + 1):
        for dummy in range(number - row):
            print(end=" ")
        for dummy in range(2 * row - 1):
            print("*", end="")
        print()
    for row in range(number - 1, 0, -1):
        for dummy in range(number - row):
            print(end=" ")
        for dummy in range(2 * row - 1):
            print("*", end="")
        print()
