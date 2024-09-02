def adding(a,b):
    return (a + b)

def subtract(a,b):
    return (a - b)

def multiply(a,b):
    return (a * b)

def divide(a,b):
    return (a / b)

num1 = float(input('enter number: '))
num2 = float(input('enter another number: '))

print ('please select the operation you wish to use: ')
print ('a. add')
print('b. subtract')
print('c. multiply')
print('d. divide')
operation = input('enter the letter next to the operation you wish to use: ')

if operation == 'a':
    print(adding(num1, num2))

elif operation == 'b':
    print(subtract(num1, num2))

elif operation == 'c':
    print(multiply(num1, num2))

elif operation == 'd':
    print(divide(num1, num2))

else:
    print('invalid entry... try again.')
