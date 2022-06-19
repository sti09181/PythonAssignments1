########################
##### Practices.py #####
########################


def Solution1():
    first = int(input("Enter a number : "))
    for second in range(1, 10):
        print(f"{first} x {second} = {first * second}")


def Solution2():
    number = int(input("Enter a number : "))
    for i in range(number):
        print((number - i - 1) * " " + (i + 1) * "*")


def Solution3():
    numbers = [9, 8, 1, 3, 5, 7, 10]

    first_max = numbers[0]
    second_max = numbers[0]

    for i in numbers:
        if i > first_max:
            second_max = first_max
            first_max = i

        elif i > second_max:
            second_max = i

    print(first_max, second_max)


def Solution4():
    apart = [["101", "102"], ["201", "202"], ["301", "302"]]

    for i in range(1, len(apart)):
        if i >= 1:
            apart[i].append(str(ord(chr(i)) + 1) + "03")

    print(apart)


def Solution5():
    answer = 0
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    print(answer)
