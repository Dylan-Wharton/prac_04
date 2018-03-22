def main():
    count = 5
    numList = []
    while count != 0:
        user_number = int(input("Please input an integer"))
        numList.append(user_number)
        count -= 1


    mean = sum(numList)/len(numList)
    print("The first number is " + str(numList[0]))
    print("The last number is " + str(numList[-1]))
    print("The smallest number is " + str(min(numList)))
    print("The largest number is " + str(max(numList)))
    print("The average of the numbers is " + str(mean))


main()