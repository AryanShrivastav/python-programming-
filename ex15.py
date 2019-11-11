def add(a,b):
    print(f'ADDING {a} + {b}')
    return a+b
def substract(a,b):
    print(f'SUBSTRACTING {a} - {b}')
    return a-b
def multiply(a,b):
    print(f'MULTIPLYING {a} * {b}')
    return a*b
def divide(a,b):
    print(f'DIVIDE {a} / {b}')
    return a/b
print('lets do some maths with only some functions')
age=add(10,9)
height=substract(6,.3)
weight=multiply(17.5,4)
iq=divide(100,2)
print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")
print('here is a pyzzle')
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
