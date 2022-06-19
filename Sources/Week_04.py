######################
##### Week_04.py #####
######################


import random
import datetime
import turtle


def Solution1():
    string = input("Enter a name : ")
    print(f"Hello {string}!")


def Solution2():
    first_number = int(input("Enter a first number : "))
    second_number = int(input("Enter a second number : "))
    print(f"Addition result is {first_number + second_number}!")


def Solution3():
    print("""\
        /\\_____/\\
       /  O   O  \\
      ( ==  ^  == )
       )         (
      (           )
     ( (  )   (  ) ) 
    (__(__)___(__)__)
     """)


def Solution4():
    print(random.randint(1, 6))


def Solution5():
    num = [30, 20]

    if num[0] < num[1]:
        print(f"{num[0]} is less then {num[1]}")
    elif num[0] > num[1]:
        print(f"{num[0]} is greater then {num[1]}")
    else:
        print(f"{num[0]} is equal then {num[1]}")


def Solution6():
    number = int(input("Enter a number : "))

    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")


def Solution7():
    score = int(input("Enter your score : "))

    if 90 <= score <= 100:
        print("Your grade is A")
    elif 80 <= score:
        print("Your grade is B")
    elif 70 <= score:
        print("Your grade is C")
    elif 60 <= score:
        print("Your grade is D")
    else:
        print("Your grade is F")


def Solution8():
    age = int(input("Enter your age : "))
    score = float(input("Enter your score : "))

    if (age > 19) and (score > 90.0):
        print("You're allowed to enter")
    else:
        print("You're not allowed to enter")


def Solution9():
    number = [0, 0, 0]

    for i in range(len(number)):
        number[i] = int(input("Enter a number : "))

    maxCondition = max(number[0], number[1], number[2])
    minCondition = min(number[0], number[1], number[2])
    print(f"Maximum : {maxCondition} | Minimal : {minCondition}")


def Solution10():
    clock = datetime.datetime.now()

    if clock.hour < 12:
        print("Before midday")
    else:
        print("After midday")


def Solution11():
    clock = datetime.datetime.now()

    if 3 <= clock.month <= 5:
        print("Spring")
    elif 6 <= clock.month <= 8:
        print("Summer")
    elif 9 <= clock.month <= 11:
        print("Autumn")
    else:
        print("Winter")


def Solution12():
    number = [0, 0, 0]

    for i in range(len(number)):
        number[i] = int(input("Enter a number : "))

    if number[0] ** 2 + number[1] ** 2 == number[2] ** 2:
        print("Right triangle")
    if number[0] ** 2 + number[1] ** 2 > number[2] ** 2:
        print("Acute triangle")
    else:
        print("Obtuse triangle")


def Solution13():
    height = float(input("Enter your height : "))
    weight = float(input("Enter your weight : "))

    height /= 100
    BMI = weight / height ** 2

    if BMI <= 18.5:
        print("You're underweight!")
    elif BMI <= 24.9:
        print("You're normal")
    elif BMI <= 29.9:
        print("You're overweight!")
    else:
        print("You're FAT!!!!")


def Solution14():
    year = int(input("Year? : "))

    if (year % 4 == 0) or (year % 100 != 0 and year % 400 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")


def Solution15():
    for i in range(10):
        print(i, end=" ")

    print()

    for i in range(1, 11):
        print(i, end=" ")

    print()

    for i in range(2, 11, 2):
        print(i, end=" ")


#####################
##### Homeworks #####
#####################


def Homework1():
    pointer = turtle.Turtle()

    pointer.pensize(3)

    x = -100
    y = 100

    pointer.penup()
    pointer.goto(x, y)
    pointer.pendown()

    pointer.circle(100)

    pointer.penup()
    pointer.goto(x - 60, y + 65)
    pointer.pendown()
    pointer.setheading(-60)
    pointer.circle(70, 120)

    pointer.penup()
    pointer.goto(x - 30, y + 120)
    pointer.pendown()
    pointer.dot(30)

    pointer.penup()
    pointer.goto(x + 30, y + 120)
    pointer.pendown()
    pointer.dot(30)

    turtle.done()


def Homework2():
    score = int(input("Enter your score : "))

    if 81 <= score <= 100:
        print("Your grade is A")
    elif 61 <= score <= 80:
        print("Your grade is B")
    elif 41 <= score <= 60:
        print("Your grade is C")
    elif 21 <= score <= 40:
        print("Your grade is D")
    else:
        print("Your grade is E")


def Homework3():
    for number in [10, 20, 30]:
        print(number)


def Homework4():
    for number in [1, 2, 3]:
        print(f"3 x {number} = {3 * number}")


def Homework5():
    for number in [3, 100, 23, 44]:
        if number % 3 == 0:
            print(number)


def Homework6():
    for number in [13, 21, 12, 14, 30, 18]:
        if (number < 20) and (number % 3 == 0):
            print(number)
