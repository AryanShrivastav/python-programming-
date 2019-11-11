def print_two(*args):arg1,arg2=args
print_two(f"arg1: {arg1}, arg2: {arg2}")
def print_two_again(arg1,arg2):
print(f"arg1: {arg1}, arg2: {arg2}")
def print_one(arg1):
print('arg1:{arg1}')
def print_none():
print('i got nothing')
print_two('hobbs','shaw')
print_two_again('hobbs','shaw')
print_one('frist!')
print_none()
