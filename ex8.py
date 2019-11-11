from sys import argv
script,user_name=argv
prompt=">"
print(f"hi {user_name},i'm the {script} script")
#when prompted to write in powershell terminal,write a single word or letter or number;write 1 thing without giving any space cuz that'll become 2 or more thingsand here we only have to write 1 thing (eg:x)
#in other scripts,argument can have 5 or 3 things, so write according to that;that is write 3 or 5 things with 2 or 4 spaces between them respectively (eg:x y z) or (eg:x y z a d)
print(" i'd like to ask you a few questions")
print(f'do you like me {user_name}')
likes=input(prompt)
print(f'where do you live {user_name}')
lives=input(prompt)
print('what kind of computer do you have')
computer=input(prompt)
print(f'''so you said {likes}about liking me.you live in {lives}.not sure where that is.and you have a nice {computer} computer''')
