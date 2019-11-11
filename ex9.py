from sys import argv
filename,script=argv
txt=open(filename)
print(f'here is your filename {filename}:')
print(txt.read())
print(f'type your filename again:')
file_again=input('>')
txt_again=open(file_again)
print(txt_again.read())
