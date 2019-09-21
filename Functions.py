Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Below is the function
>>> def hello():
	print ("hello")
	return 1234
#And here is the function being used
print hello()
SyntaxError: invalid syntax
>>> print(hello())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(hello())
NameError: name 'hello' is not defined
>>> ef hello():
	print ("hello")
	return 1234
#And here is the function being used
print (hello())
SyntaxError: invalid syntax
>>> def hello():
	print ("hello")
	return 1234
#And here is the function being used
print(hello())
SyntaxError: invalid syntax
>>> hello
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> #How parameters work
>>> def funnyfunction(first_word,second_word,third_word):
	print("The word created is: " + first_word + second_word + third_word)
	return first_word + second_word + third_word

>>> #Calculator program
>>> #NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
>>> #Here we will define our functions
>>> #this prints the main menu, and prompts for a choice
>>> def menu():
	#print what options you have
	print("Welcome to calculatory.py")
	print("your options are:")
	print(" ")
	print("1) Addition")
	print("2) Subtraction")
	print("3) Multiplication")
	print("4) Division")
	print("5) Quit calculator.py")
	print(" ")
	return input ("Choose your option: ")
#this adds two numbers given
def add(a,b):
	
SyntaxError: invalid syntax
>>> def add(a,b):
	print a, "+", b, "=", a + b
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a, "+", b, "=", a + b)?
>>> def add(a,b):
	print(a, "+", b, "=", a + b)

	
>>> #this subtracts two numbers given
>>> def sub(a,b)
SyntaxError: invalid syntax
>>> def sub(a,b):
	print(b, "-", a, "=", b - a)

	
>>> #this multiplies two numbers given
>>> def mul(a,b):
	print(a, "*", b, "=", a * b)

	
>>> #this divides two numbers given
>>> def div(a,b):
	print(a, "/", b, "=", a / b)

	
>>> #NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
>>> loop = 1
>>> choice = 0
>>> while loop == 1:
	choice = menu()
	if choice == 1:
		add(input("Add this: "),input("to this: "))
	elif choice == 2:
		sub(input("Subtract this: "),input("from this: "))
	elif choice == 3:
		mul(input("Multiply this: "),input("from this: "))
	elif choice == 4:
		div(input("Divide this: "),input("from this: "))
	elif choice == 5:
		loop = 0
print("Thank you for using calculator.py")
SyntaxError: invalid syntax
>>> add(2,30)
2 + 30 = 32
>>> sub(2,30)
30 - 2 = 28
>>> num1 = 45
>>> num2 = 8
>>> add(num1,num2)
45 + 8 = 53
>>> div(num1,num8)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    div(num1,num8)
NameError: name 'num8' is not defined
>>> div(num1,num2)
45 / 8 = 5.625
>>> 
