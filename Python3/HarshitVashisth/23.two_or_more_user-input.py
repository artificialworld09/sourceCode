## Normal way
#a = input('Enter your name: ')
#b = int(input('Enter your age: '))
#print(f'Hi {a} your age is: {b}')

## method-1
#a, b = input('Enter your name and age: ').split()
#b = int(b)
#print(f'Hi {a} your age is: {b+3}')

## method-2
a, b = input('Enter your name and age separeted by comma: ').split(',')
b = int(b)
print(f'Hi {a} your age is: {b+4}')