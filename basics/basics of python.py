#1.print name

print("mallikarjunrao")# this is direct method 
name = "mallikarjun"# intialize with a variable
print(name)#print the variable

#2.single and multiline comments

# this hash is the comment where ,this not gonna execute
"""
this is multi line comment
"""
# this comments are used in understanding the code
# we can specify this comments whereever wewant to use

#3.variables for different datatypes

number = 500# assigning variable to inte
mahu = True
name = "mallikarjun"
something = 5.5
print(type(number))
print(type(mahu))
print(type(name))
print(type(something))

#4.local and global variable with same name and print both variables

var ='global value'# outsode function
def my_function():# creates the function 
    var = 'local value'
    print(var)
my_function()# this prints the local value
print(var)# this prints the global value
 # inside any function that is declared as local,when function called it prints out local value
 # out side the function that can be declared as global,either it consists the same variablename
print(var)


 
