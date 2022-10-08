''' Speech Method:
x = int(input('Input First Number: '))
s = input('Input Symbol: ')
y = int(input('Input Second Number: '))

^ Old input type '''

i = input()

x1, s, y1 = list(i)

x = int(x1)
y = int(y1)

def add():
    answer = x + y
    print()
    print(answer)

def sub():
    answer = x - y
    print()
    print(answer)

def mult():
    answer = x * y
    print()
    print(answer)

def div():
    answer = x / y
    print()
    print(answer)

if (s == '+'):
    add()

elif (s == '-'):
    sub()

elif (s == '*'):
    mult()

elif (s == '/'):
    div()

else:
    print('Wrong Input')




