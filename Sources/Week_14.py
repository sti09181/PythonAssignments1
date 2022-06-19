######################
##### Week_14.py #####
######################


import random
import math


def Solution1():
    random.seed(1)
    print(random.random())
    print(random.random())


def Solution2():
    print(random.uniform(1, 10))
    print(random.uniform(1, 10))


def Solution3():
    print(random.randrange(1, 100, 2))
    print(random.randrange(0, 101, 2))


def Solution4():
    family = ["Mother", "Father", "Brother", "Sister", "Granny"]
    print(random.choice(family))
    random.shuffle(family)
    print(family)
    print(random.sample(family, 3))


def Solution5():
    n = 100000
    inside = 0

    for dummy in range(n):
        x = random.random()
        y = random.random()

        if math.sqrt(x * x + y * y) <= 1:
            inside += 1

    estimatedPI = 4 * inside / n

    print(f"PI : {math.pi}")
    print(f"Estimated PI : {estimatedPI}")
