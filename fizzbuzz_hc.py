#fizbuzz_hc.py
#Drew Michael, 2014

import sys

def fizzbuzz_hc():
    """Prints hardcoded fizzbuzz exercise to standard output."""
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print 'Fizz Buzz'
        elif i % 3 == 0:
            print 'fizz'
        elif i % 5 == 0:
            print 'buzz'
        else:
            print i

def main():
    fizzbuzz_hc()

main()


