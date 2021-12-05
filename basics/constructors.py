# constructor is the special method used for the creation and intialize the object of the class
# default constructor

class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()


 # here invovles 3 types of constructers 
 # default constructor 
 # parameterized constructor
 # non-parameterized constructor

 # parameterized constructor

class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor:A constructor with defined parameters or arguments is called a parameterized constructor. We can pass different values to each object at the time of creation using a parameterized constructor.


	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()


# non-parameterized constructor:constructor without any arguments is called a non-parameterized constructor. This type of constructor is used to initialize each object with default values.



class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()


# while coming to access modifiers in constructors ,invovles three types
# public,private and protected

# public access modifiers

#The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default. 
# program to illustrate public access modifier in a class

class mahu:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members
		self.name = name
		self.age = age

	# public member function	
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.age)

# creating object of the class
obj = mahu("R2J", 20)

# accessing public data member
print("Name: ", obj.name)

# calling public member function of the class
obj.displayAge()



# protected acess modifiers

#The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 


# program to illustrate protected access modifier in a class

# super class
class Student:
	
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch):
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)


# derived class
class Geek(Student):

	# constructor
	def __init__(self, name, roll, branch):
				Student.__init__(self, name, roll, branch)
		
	# public member function
	def displayDetails(self):
				
				# accessing protected data members of super class
				print("Name: ", self._name)
				
				# accessing protected member functions of super class
				self._displayRollAndBranch()

# creating objects of the derived class	
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()






#private access modifiers


# program to illustrate private access modifier in a class

class mahu:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch):
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function
	def __displayDetails(self):
		
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
			
		# accesing private member function
		self.__displayDetails()

# creating object
obj = mahu("R2J", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()









