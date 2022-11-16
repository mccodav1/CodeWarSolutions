# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.


def xo(s):
    return s.count('x') + s.count('X') == s.count('o') + s.count('O')

#    x = s.countif('x') + s.countif('X')
#    o = s.countif('o') + s.countif('O')