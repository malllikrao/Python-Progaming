#1. write function for arthematic operations 

def adition(n1,n2):# taken two arguements
    return n1+n2
def multiply(n1,n2):
    return n1*n2 
def subtract(n1,n2):
    return n1-n2
def divison(n1,n2):
    return n1/n2    

add = adition(10,20) # variable assigned to adition function
mul = multiply(10,20)# variable assigned to multiply function
sub = subtract(10,20)#variable assigned to subtract function
divi = divison(20,100)# variable assigned to divison functin
print(add) #prints addition of numbers
print(mul)# prints multiply of numbers
print(sub)# print subtract of numbers
print(divi)#prints out the output of numbers




#2. increment and decrement operators

a = 0 # intial with o 
a+=1 # incremnet of 1
a # result as 1 as output

a = 1
a -=1# decrements the value by 1
a # result as o as output

#3.program to find two numbers equal or not

a = 10# initialize the vaiables 
b = 20

if a==b:# checking weather variables are equal or not ,if equal return true else return false
    print("equal")
else:
    print("unequal")  


#4. program for relational operators


x =1
y =2

if x<y or x==y or x!=y or x<=y:# checking weather equal or not if equal or less than or greater the return right ,or else return wrong
    print("yes ,you are correct")
else:
    print("you're wrong")


#5. print smaller and longer number

a =int(input("enter the first number:"))# taking input of numbers

b = int(input("enter the second number:"))

if a>=b:# if a is greater or equal then print a is greater
    print(a,"is greater!")
else:# or b is greater
    print(b,"is greater!")    


    






        



