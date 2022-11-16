# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
# the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would
# make this happen, return -1.


def find_even_index(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            print('index is', i)
            return
    print('none found')
    return -1
