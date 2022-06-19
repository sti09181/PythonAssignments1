#########################
##### Week_01_03.py #####
#########################


import keyword
import random
import math


def Solution1():
    print(keyword.kwlist)


def Solution2():
    teacher = "Mr. Morton"
    print(f"teacher id = {id(teacher)}")
    teacher = "Mr. Senders"
    print(f"teacher id = {id(teacher)}")

    myTeacher = "Ms. Senders"
    yourTeacher = myTeacher
    print(f"myTeacher id = {id(myTeacher)}")
    print(f"yourTeacher id = {id(yourTeacher)}")


def Solution3():
    integer = 10
    floating = 3.14159265358979323846
    string = "Hello World!"
    print(f"{integer} | {floating} | {string}")
    print(f"{str(type(integer))} | {str(type(floating))} | {str(type(string))}")
    print(not ((integer > floating) and (integer == 10)))


def Solution4():
    integer = "10"
    floating = "3.14159265358979323846"
    string = "Hello World!"
    print(int(integer) * float(floating))
    print(string[0:5])
    print(len(string))
    print(f"{chr(ord('A'))} | {ord('A')}")


def Solution5():
    integers = [10, 3]
    print(integers[0] + integers[1])
    print(integers[0] - integers[1])
    print(integers[0] * integers[1])
    print(integers[0] / integers[1])
    print(integers[0] // integers[1])
    print(integers[0] % integers[1])
    print(integers[0] ** integers[1])

    for dummy in range(3):
        integers[0] **= integers[1]
    print("%e" % integers[0])


def Solution6():
    integers = [23, 5]
    print(f"x & y : {integers[0] & integers[1]} | Binary : {bin(integers[0] & integers[1])}")
    print(f"x | y : {integers[0] | integers[1]} | Binary : {bin(integers[0] | integers[1])}")
    print(f"x ^ y : {integers[0] ^ integers[1]} | Binary : {bin(integers[0] ^ integers[1])}")
    print(f"x << y : {integers[0] << integers[1]} | Binary : {bin(integers[0] << integers[1])}")
    print(f"x >> y : {integers[0] >> integers[1]} | Binary : {bin(integers[0] >> integers[1])}")
    print(f"~y : {~integers[1]} | Binary : {bin(~integers[1] & 0xFFFFFFFF)}")


def Solution7():
    integer = 20212952
    print(f"{integer} is {bin(integer)} in Binary")
    print(f"{integer} is {oct(integer)} in Binary")
    print(f"{integer} is {hex(integer)} in Binary")

    integer = "10101010101010"
    print(f"{integer} is {int(integer, 2)} in Integer")

    integer = "1726354"
    print(f"{integer} is {int(integer, 8)} in Integer")

    integer = "F1"
    print(f"{integer} is {int(integer, 16)} in Integer")


def Solution8():
    integers = [random.randint(1, 6), random.randint(1, 6)]
    print(f"integers[0] == {integers[0]}")
    print(f"integers[1] == {integers[1]}")
    print(f"Answer : {integers[0] == integers[1]}")


#####################
##### Homeworks #####
#####################


def Homework():
    # Followed instructions based on Zeller's congruence
    year = int(input("Year? : "))
    month = int(input("Month? : "))
    dayOfTheMonth = int(input("Day of the month? : "))

    yearOfTheCentury = year % 100
    zeroBasedCentury = math.floor(year / 100)
    dayOfTheWeek = (dayOfTheMonth + math.floor(13 * (month + 1) / 5) +
                    yearOfTheCentury + math.floor(yearOfTheCentury / 4) +
                    math.floor(zeroBasedCentury / 4) - 2 * zeroBasedCentury) % 7

    switcher = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }

    print(f"Day of the week : {switcher.get(int(dayOfTheWeek), 'Invalid day')}")
