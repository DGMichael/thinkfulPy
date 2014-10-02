#fizbuzz_args.py
#Drew Michael, 2014

import sys
import pdb

def fizzbuzz_args(arg_input):
	print "Fizzbuzz!  Let's play!"
	num = 0
	if arg_input > 0:
		num = arg_input
	else:
		while True:
			try:
				num = int(raw_input("How far should we count up to? "))
				break
			except ValueError:
				print "Please enter an integer value."
	for i in range(1, num + 1):
		if i % 3 == 0 and i % 5 == 0:
			print "Fizz Buzz"
		elif i % 3 == 0:
			print "Fizz"
		elif i % 5 == 0:
			print "Buzz"
		else:
			print i
	print "Program complete, thanks for playing."

def main():
	arg_input = 0
	if len(sys.argv) > 2:
		sys.exit("Use: python ~/path/fizzbuzz_args.py <maximum integer>")
	elif len(sys.argv) > 1:
		if sys.argv[1].isdigit():
			arg_input = int(sys.argv[1])
		else:
			while arg_input < 1:
				try:
					arg_input = int(raw_input("Please enter an interger value to count up to: "))
					break
				except ValueError:
					print "Non-integer value entered...sorry play fair."
	fizzbuzz_args(arg_input)

main()
