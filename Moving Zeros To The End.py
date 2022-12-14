# Write an algorithm that takes an array and moves all of the
# zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


def move_zeros(array):
    fixedList = []
    zeros = 0
    for i in array:
        if not i and type(i) is int or type(i) is float:
            zeros += 1
        else:
            fixedList.append(i)
    for i in range(zeros):
        fixedList.append(0)
    return fixedList

