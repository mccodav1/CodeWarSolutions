"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Given:
apples, pears # and bananas
grapes
bananas !apples

Return:
apples, pears
grapes
bananas
"""


def solution(string, markers):
    totalStringSplitIntoAList = string.split('/n')
    fixedList = []
    for lineOfText in totalStringSplitIntoAList:
        newStr = str(lineOfText)
        fixedStr = ""
        for letter in newStr:
            if letter in markers:
                break
            else:
                fixedStr += letter
        if newStr.endswith('\n'):
            fixedStr += '\n'
        fixedList.append(fixedStr)
    joined = '/n'.join(fixedList)
    return joined


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

