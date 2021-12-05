#python does not support method overloading by default. But there are different ways to achieve method overloading in Python. 



# First product method.
# Takes two argument and print their
# product
def product(a, b):
	p = a * b
	print(p)
	
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error	
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)




# Function to take multiple arguments
def add(datatype, *args):

	# if datatype is int
	# initialize answer as 0
	if datatype =='int':
		answer = 0
		
	# if datatype is str
	# initialize answer as ''
	if datatype =='str':
		answer =''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'mallik')



# examples of method overloading
class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
             print('Hello ')
# Create instance
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('jala technologies')


