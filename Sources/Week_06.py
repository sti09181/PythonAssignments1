######################
##### Week_06.py #####
######################


import copy


def Solution1():
    family = ["Mother", "Father", "Brother", "Sister"]
    print(family)


def Solution2():
    family = []
    family.append("Mother")
    family.append("Father")
    family.append("Brother")
    family.append("Sister")
    print(family)


def Solution3():
    print(dir(list))


def Solution4():
    family = ["Mother", "Father", "Brother", "Sister"]
    print(family[2])
    print(family[3])
    print(family[0:2])
    print(family[0:4:3])


def Solution5():
    family = ["Mother", "Father", "Brother", "Sister"]
    age = [48, 58, 18, 18]

    combined = family + age

    print(combined)
    print(family * 2)
    print(age * 2)


def Solution6():
    family = ["Mother", "Father", "Brother", "Sister"]

    print(f"Count of family members : {len(family)}")


def Solution7():
    family = ["Mother", "Father", "Brother", "Sister"]
    family.append("Wife")
    family.insert(2, "Granny")
    family.extend(["Son", "Daughter"])
    print(family)


def Solution8():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    family.remove("Brother")
    print(family)

    del family[2]
    print(family)

    copied = family.pop()
    print(family)
    print(copied)


def Solution9():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(f"Is \"Granny\" is exist in this list? : {'Granny' in family}")

    if "Granny" in family:
        print(family)

    print(f"Index of \"Granny\" : {family.index('Granny')}")


def Solution10():
    numbers = [1, 2, 3, 4]
    result = [number * 3 for number in numbers]
    print(result)
    result = [number * 3 for number in numbers if number % 2 == 0]
    print(result)


def Solution11():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(family)

    family.sort()
    print(family)


def Solution12():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(family)

    familyCopy = family[:]
    familyCopy.sort()
    print(familyCopy)


def Solution13():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(family)

    familyCopy = sorted(family)
    print(familyCopy)


def Solution14():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(family)

    familyCopy = family
    familyCopy.sort()

    print(id(familyCopy))
    print(id(family))

    print(familyCopy)
    print(family)


def Solution15():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(family)

    familyCopy = copy.deepcopy(family)
    familyCopy.sort()

    print(id(familyCopy))
    print(id(family))

    print(familyCopy)
    print(family)


def Solution16():
    numbers = [8, 4, 9, 5]
    minimal = numbers[0]

    for i in range(1, len(numbers)):
        if minimal > numbers[i]:
            minimal = numbers[i]

    print(minimal)


def Solution17():
    numbers = [8, 4, 9, 5]
    maximum = numbers[0]

    for i in range(1, len(numbers)):
        if maximum < numbers[i]:
            maximum = numbers[i]

    print(maximum)


#####################
##### Homeworks #####
#####################


def Homework1():
    strings = ['stdio.h', 'main.c', 'stdlib.h', 'run.py']

    for string in strings:
        split = string.split(".")

        if split[1] == "h":
            print(string)


def Homework2():
    apartment = [[101, 102], [201, 202], [301, 302]]

    for row in apartment:
        for column in row:
            print(f"Room {column}")
    print("-----")


def Homework3():
    additionResult = 0

    for oddNumber in range(1, 11, 2):
        additionResult += oddNumber

    print(f"Addition result : {additionResult}")


def Homework4():
    for dummy in range(4):
        print("-------")


def Homework5():
    characters = ["A", "b", "c", "D"]
    for character in characters:
        if character.isupper():
            print(character)
