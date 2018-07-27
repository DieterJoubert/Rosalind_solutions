def main():
	print fib(25)

def fib(x):
	fib = [0, 1]

	for i in range(2, x+1):
		fib.append(fib[i-1]+fib[i-2])

	return fib[-1]

if __name__ == "__main__":
	main()