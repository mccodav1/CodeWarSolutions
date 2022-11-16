def snail(snail_map):
    newList = []
    length = len(snail_map[0])
    height = length
    width = length
    while height > 0 and width > 0:
        for number in range(width):
            newList.append(snail_map[length-height][number])
        height -= 1
        for number in range(height):
            newList.append(snail_map[number][]