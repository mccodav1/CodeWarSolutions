def high_and_low(numbers):
    numList = numbers.split(" ")
    numList.sort()
    numbers = str(numList[-1]) + " " + str(numList[0])
    return numbers
