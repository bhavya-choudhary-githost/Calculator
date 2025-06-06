import math

num_1 = float(input('Enter first number: '))
op = input("Enter operator(=, - ,/ , *, ^, log): ")
num_2 = float(input('Enter second number: '))

if op == '+':
    print(num_1 + num_2)

elif op == '-':
    print(num_1 - num_2)

elif op == '/':
    print(num_1 / num_2)

elif op == '*':
    print(num_1 * num_2)

elif op == '^':
    print(num_1 ** num_2)

elif op == 'log':
    print(math.log(num_1, num_2))

else :
    print('Invalid operator, man')
