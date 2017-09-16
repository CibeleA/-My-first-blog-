# print("Hello, Django girls!")
# if 3>2: print ("It works")
# if 5>2: print("sim")
# else: print("no")
# name = 'Sonja'
# if name == 'Ana':
#     print('Hey Ana!')
# elif name == 'Sonja':
#     print('Hey Sonja!')
# else:
#     print('Hey anonymous!')
# volume = 57
# if volume < 20:
#     print("It's kinda quiet.")
# elif 20 <= volume < 40:
#     print("It's nice for background music")
# elif 40 <= volume < 60:
#     print("Perfect, I can hear all the details")
# elif 60 <= volume < 80:
#     print("Nice for parties")
# elif 80 <= volume < 100:
#     print("A bit loud!")
# else:
#     print("My ears are hurting! :(")
#     
def hi(): 
	print("Hi there!")
	print("How are you?")
hi()
def hi(name):
	if name== "cibele":
		print("Hi cibele!")
	elif name== "Sonja":
		print("Hi Sonja")
	else:
		print ("Hi anonymous!")
hi("Renato")
hi("Sonja")
def hi(name):
	print("Hi"+ name + "!")
hi("Rachel")
girls = ["Islanny", "Nancy", "Bia", "Luiza"]
for name in girls:
	hi(name)
for i in range(1,6):
	
	print(i)