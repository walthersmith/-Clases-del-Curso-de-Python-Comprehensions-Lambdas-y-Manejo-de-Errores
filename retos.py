#create a list of numbers ^2
numbers = [x**2 for x in range(1,101)]
print(numbers)

#no divisible by 3
squares = [x  for x in range(1,101) if x %3!=0]
print(squares)

#create with list comprehension, a list with 
#numbers multiplos of 4, 6 and 9  up to 5 digits

multiples = [x for x in range(1,100000) if x % 4 == 0 and x %6 == 0 and x %9 ==0]
print(multiples)