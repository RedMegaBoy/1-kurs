print ("Калькулятор")

x = float(input ("x="))

y = float(input ("y="))

b = input ("Дiя:")

if b == '+':
    def b (x, y):
        return x + y
    print (b (x, y))

if b == '-':
    def b (x, y):
        return x - y
    print (b (x, y))

if  b == '*':
    def b (x, y):
        return x * y
    print (b (x, y))

if  b == '/':
    def b (x, y):
        return x / y
    if y == 0:
        print("Дiлення на ноль!")
    print (b  (x, y))
if b == '%':
    def b(x, y):
        return x % y
    print(b(x, y))

if b == '**':
    def b(x, y):
        return x ** y
    print(b(x, y))
print ("End")