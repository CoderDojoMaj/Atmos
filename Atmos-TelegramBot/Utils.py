import sys


def sprint(*args):
    r = ''
    for arg in args:
        r+=str(arg) + ' '

    r += '\n'
    sys.stdout.write(r)
