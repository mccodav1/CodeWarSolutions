def pig_it(text):
    return ' '.join([(x[1:] + x[0] + 'ay') for x in text.split(' ')]).rstrip(' ')

