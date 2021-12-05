# exceptions in python are finding out the runtime error in the code
# they are try,catch and finally exceptions

#1. Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("An error occurred")



#2.catching the specfic exception



# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")


#3.

# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')


#4.raising an exception in try block

# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not

#5.program to except the arthematic KeyError

try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")


6.#program for exception lookup KeyError

try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")


#7.exception not implemented error


class BaseClass(object):
	"""Defines the interface"""
	def __init__(self):
		super(BaseClass, self).__init__()
	def do_something(self):
		"""The interface, not implemented"""
		raise NotImplementedError(self.__class__.__name__ + '.do_something')

class SubClass(BaseClass):
	"""Implementes the interface"""
	def do_something(self):
		"""really does something"""
		print (self.__class__.__name__ + ' doing something!')

SubClass().do_something()
BaseClass().do_something()


#8. exception zerp divison error

print(1/0)

try:
    print(1/0)    
except:
    ZeroDivisionError


