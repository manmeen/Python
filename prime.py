def PrimeNum(num): #Print Prime numbers upto num numbers
	"""Print Prime Numbers or multiples of non-prime"""
	for n in range(2,num):
		for x in range(2,n):
			if n%x == 0:
				print(n,'equals',x,'*',n//x)
				break
		else:
			print(n, 'is a prime number')

#Calling the function
PrimeNum(10)