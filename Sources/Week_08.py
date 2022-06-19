######################
##### Week_08.py #####
######################


def Solution1():
    print("My name is Carl.")
    print("I'm 20 years old.")
    print("It's a pleasure to meet you.")


def Solution2():
    def Combination(n, r):
        result = [1, 1]
        if n > 1:
            for dummy in range(r):
                result[0] *= n
                result[1] *= r
                n, r = n - 1, r - 1
            return result[0] // result[1]
        else:
            return "Please, Enter a Integer."

    def Recombination(n, r):
        return Combination(r + (n - 1), r)

    print(Combination(5, 2))
    print(Recombination(5, 2))


def Solution3():
    def PrintInfo(name="", age=0):
        name = "Carl"
        age = 20
        print(f"In the Function : {name}, {age}")

    previousName = "James"
    previousAge = 19
    print(f"Before the Function : {previousName}, {previousAge}")
    PrintInfo(previousName, previousAge)
    print(f"After the Function : {previousName}, {previousAge}")


def Solution4():
    def Summary(*args):
        result = 0
        for i in args:
            result += i
        return result

    print(Summary(1, 2, 3, 4, 5, 6, 7, 8, 9))


#####################
##### Homeworks #####
#####################


def Homework():
    file = open("Input_File.txt", "r")
    words = file.read().split()
    file.close()

    needsToBeDeleted = "~ ` ! @ # $ % ^ & * ( ) { } : \" < > ? [ ] ; \' , . / 1 2 3 4 5 6 7 8 9 0 _ - + = \t \n"
    needsToBeDeleted = needsToBeDeleted.split()
    needsToBeDeleted.append(" ")

    result = {}

    for i in range(len(words)):
        words[i] = words[i].upper()

        for j in range(len(needsToBeDeleted)):
            words[i] = words[i].replace(needsToBeDeleted[j], "")

        if words[i] not in result:
            result[words[i]] = 1
        else:
            result[words[i]] += 1

    result = {key: value for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    print(result)
