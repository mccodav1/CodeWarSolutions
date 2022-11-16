"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def good_make_readable(seconds):
    readable = ""

    returnHours = seconds // 3600
    seconds -= (returnHours*3600)
    returnHours = str(returnHours).zfill(2)

    returnMinutes = seconds // 60
    seconds -= (returnMinutes*60)
    returnMinutes = str(returnMinutes).zfill(2)

    returnSeconds = str(seconds).zfill(2)

    readable += returnHours + ":" + returnMinutes + ":" + returnSeconds
    return readable

def make_readable(seconds):
    readable = ""

    returnHours = seconds // 3600
    seconds -= (returnHours*3600)
    returnHours = str(returnHours).zfill(2)

    returnMinutes = seconds // 60
    seconds -= (returnMinutes*60)
    returnMinutes = str(returnMinutes).zfill(2)

    returnSeconds = str(seconds).zfill(2)

    readable += returnHours + ":" + returnMinutes + ":" + returnSeconds
    return readable



print(make_readable(23583))








