######################
##### Week_07.py #####
######################


import math
import time


from itertools import combinations


def Solution1():
    eratosthenes = list(range(2, 65))

    for i in eratosthenes:
        for j in eratosthenes:
            if j > i and j % i == 0:
                eratosthenes.remove(j)
    print(eratosthenes)


def Solution2():
    for n in range(51):
        m = 2 ** n - 1

        for i in range(2, int(math.sqrt(m)) + 1):
            if m % i == 0:
                break
        else:
            print(m)


def Solution3():
    score = (80, 70, 90, 60)

    first, second, third, forth = score

    print(first, second, third, forth)


def Solution4():
    dictionaries = {20: "Me", 50: "Mother", 56: "Father"}

    dictionaries.update({"Passed away": "Granny"})

    print(dictionaries)
    print(dictionaries["Passed away"])
    print(dictionaries[20])

    granny = dictionaries.pop("Passed away")

    print(granny)
    print(dictionaries)


def Solution5():
    dictionaries = {20: "Me", 50: "Mother", 56: "Father"}

    dictionaries.update({"Passed away": "Granny"})

    print(dictionaries)
    print(dictionaries["Passed away"])
    print(dictionaries[20])

    del dictionaries["Passed away"]

    print(dictionaries)


def Solution6():
    dictionaries = {20: "Me", 50: "Mother", 56: "Father"}

    dictionaries.update({"Passed away": "Granny"})

    print(dictionaries)
    print(dictionaries["Passed away"])
    print(dictionaries[20])

    print(dictionaries.keys())
    print(dictionaries.values())
    print(dictionaries.items())


def Solution7():
    dictionaries = {20: "Me", 50: "Mother", 56: "Father"}

    dictionaries.update({"Passed away": "Granny"})

    for key in dictionaries:
        print(f"{key}'s value is {dictionaries[key]}")

    print()

    for key, value in dictionaries.items():
        print(f"{key}'s value is {value}")

    if "Passed away" in dictionaries:
        print(dictionaries["Passed away"])
    else:
        print("No database is found!")


def Solution8():
    A = {"A", "B", "C", 1, 2}
    B = {"A", "C", "D", 3, 4}

    print(f"A : {A}")
    print(f"B : {B}")
    print(f"A union B : {A | B}")
    print(f"A intersect B : {A & B}")
    print(f"A minus B : {A - B}")
    print(f"A symmetric difference B {A ^ B}")


def Solution9():
    primeNumbers = {2, 3, 5, 7, 9, 15}
    print(primeNumbers)

    primeNumbers.add(11)
    print(primeNumbers)

    primeNumbers.update({13, 17, 19})
    print(primeNumbers)

    primeNumbers.discard(9)
    primeNumbers.remove(15)
    print(primeNumbers)


def Solution10():
    allSet = [{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {1, 3, 5, 7, 12, 15}, \
              {3, 12, 15, 18, 20}, {12, 13, 14, 15, 16, 17, 18, 19}]

    for i in range(len(allSet) - 1):
        for j in range(i + 1, len()):
            print(len(allSet[i] & allSet[j] / len(allSet[i] | allSet[j])))


def Solution11():
    S = {-7, -3, -2, 5, 8}

    for target in range(1, len(S) + 1):
        numberOfCases = list(combinations(S, target))

        for case in range(len(numberOfCases)):
            if sum(numberOfCases[case]) == 0:
                print(numberOfCases[case])
                print("Found!")
                exit()


def Solution12():
    string = "O! LORD! have a mercy! I don't want to do this crap!"

    result1 = string.split()
    result2 = string.split(sep="! ")
    result3 = " FUCK!!! ".join(result2)
    result4 = " FUCK!!! ".join(string.split(sep="! "))

    print(result1)
    print(result2)
    print(result3)
    print(result4)


def Solution13():
    result1 = "O %s %s" % ("My", "GOD!!!!")
    result2 = "O {} {}".format("My", "GOD!!!!")
    result3 = f"O {'My'} {'GOD!!!!'}"

    print(result1)
    print(result2)
    print(result3)


def Solution14():
    string = "O! LORD! have a mercy! I don't want to do this crap! PLEASE LORD GODDAMMIT!!!! SAVE ME!!!!"

    print(f"Count of characters : {len(string)}")
    print(f"Search result of \"LORD\" : string[{string.find('LORD')}]")
    print(f"Recursive search result of \"LORD\" : string[{string.rfind('LORD')}]")
    print(f"\"LORD\" first appeared in string[{string.index('LORD')}]")
    print(f"\"LORD\" is appeared about {string.count('LORD')} times")


def Solution15():
    string = {
        "O! LORD! have a mercy! I don't want to do this crap!"
        "O! LORD! have a mercy! I don't want to do this crap! PLEASE LORD GODDAMMIT!!!! SAVE ME!!!!"
        "This is just another testing... LOL"
    }

    for i in string:
        if i.startswith("O") and i.endswith("ME!!!!"):
            print(i)
            break


def Solution16():
    print("Please enter your phone number : ")
    phoneNumber = input()
    if phoneNumber.isdecimal():
        print("Thank you!")
    else:
        print("THE FUCK IS WRONG WITH YOU???? I SAID PUT YOUR DAMN PHONE NUMBER YOU MORON!")


#####################
##### Homeworks #####
#####################


def Homework1():
    numbers = [7, 4, 5, 1, 3]

    time_start = time.time()

    for i in range(1, len(numbers)):
        flag = False

        for j in range(0, len(numbers) - i):
            if numbers[j] > numbers[j + 1]:
                flag = True
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

        if not flag:
            break

    time_end = time.time()

    print(numbers)
    print(f"Time taken : {time_end - time_start}")

    numbers = [7, 4, 5, 1, 3]

    time_start = time.time()

    numbers.sort()

    time_end = time.time()

    print(numbers)
    print(f"Time taken : {time_end - time_start}")


def Homework2():
    data = [
        [2000, 3050, 2050, 1980],
        [7500, 2050, 2050, 1980],
        [15450, 15050, 15550, 14900]
    ]

    for line in data:
        for column in line:
            print(column * 1.00014)
        print("----")


def Homework3():
    data = [
        [2000, 3050, 2050, 1980],
        [7500, 2050, 2050, 1980],
        [15450, 15050, 15550, 14900]
    ]

    result = []
    for line in data:
        for column in line:
            result.append(column * 1.00014)
    print(result)


def Homework4():
    data = [
        [2000, 3050, 2050, 1980],
        [7500, 2050, 2050, 1980],
        [15450, 15050, 15550, 14900]
    ]

    result = []
    for line in data:
        sub = []
        for column in line:
            sub.append(column * 1.00014)
        result.append(sub)
    print(result)


def Homework5():
    ohlc = [
        ["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]
    ]

    volatility = []
    for i in range(1, len(ohlc)):
        volatility.append(ohlc[i][1] - ohlc[i][2])
    print(volatility)


def Homework6():
    currencies = {"US Dollar": 1167, "Yen": 1.096, "Euro": 1268, "Yuan": 171}
    number = input("Enter a number : ")
    wonCurrency = number.split()
    print(float(wonCurrency) * currencies[wonCurrency], "Won")


def Homework7():
    strings = ['stdio.h', 'main.c', 'stdlib.h', 'run.py']
    for i in strings:
        splitted = i.split(".")
        if (splitted[1] == "h") or (splitted[1] == "c"):
            print(i)


def Homework8():
    number = 3
    for i in range(1, 10, 2):
        print(number, "x", i, " = ", number * i)
