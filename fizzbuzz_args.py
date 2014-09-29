#fizbuzz_args.py
#Drew Michael, 2014

import sys

def fizzbuzz_args(arg_input):
	print "Fizzbuzz!  Let's play!"
	num = 0
	if arg_input > 0:
		num = arg_input
	else:
		while True:
			try:
				num = int(raw_input("How far should we count up to? ")) + 1
				break
			except ValueError:
				print "Please enter an integer value."
	for i in range(0, int(num)):
		if i % 3 == 0:
			print "Fizz"
		elif i % 5 == 0:
			print "Buzz"
		else:
			print i
	print "Program complete, thanks for playing."

def main():
	if len(sys.argv) > 2:
		sys.exit("Use: python ~/path/fizzbuzz_args.py <maximum integer>")
	arg_input = 0
	if len(sys.argv) > 1:
		while type(sys.argv[1]) != type(int(1)):
			try:
				arg_input = int(raw_input("Please enter an interger value to count up to: ")) + 1
				break
			except ValueError:
				print "Non-integer value entered...sorry play fair."
	fizzbuzz_args(arg_input)

main()