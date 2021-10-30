#create a list of numbers ^2
numbers = [x**2 for x in range(1,101)]
print(numbers)

#no divisible by 3
squares = [x  for x in range(1,101) if x %3!=0]
print(squares)