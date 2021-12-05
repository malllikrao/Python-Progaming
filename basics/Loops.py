#1. print "bright it career 10 times using for loops"

for _ in range(10):# it prints string 10 times
    print("bright it career")

#2.print"1 to 20 numbers using while loop"

i = 1# intialize the variable with 1 

while(i<=20):# numbers should be in range 1 to 20
    print(i)# print numbers
    i+=1# increment numbers by 1 upto 20


#3.print "equal operator " and "not equal operator"

number1 = 20
number2 = 30

if number1!= number2:# checking numbers are equal or not
    print("both numbers are not equal")
else:# number1 == number2
    print("numbers are equal")   


#4. program to print the odd and even numbers

for i in range(20):
    if (i%2) == 0:# number divided by 2 means it is even number
        print(i,"eeven number")
    else:# or it is odd number
        print(i,"odd number") 


#5.program to print largest among the three numbers

a =10
b =20
c =30

if a>b and a>c:
    print(a,"greater than b and c")
elif b>c and b>a:
    print(b,"greater than a andc")
else:
    print(c,"greater than a and b")   


#6.program to print the even number between 10 and 20,using while

x = int(input("enter a number:"))# we can choose whatever the range
i = 10
while i<=x:
     if i%2 == 0:# this returns numbers that are even
         print("numbers is even: ",i)
     i+=1     



#7.print 1 to 10 numbers using while loop

i = 1# initialize the number
while i<=10:# going through the numbers upto 10
    print(i)#print numbers
    i+=1# increment the values by 1,each single step upto 10

#8.program to find armstong number or not


num = int(input("enter the number: "))
sum = 0# intialize sum with zero

temp = sum
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//10

if num ==sum:# if number equal to zero then it is armstrong
    print("number is an armstrong number")
else:
    print("it is not an armstrong number")   


#9. program to find the prime or not

n = 11
if n>1:
    for i in range(2,int(n/2)+1):
        if (i%2) == 0:# if it is even  it is not prime
            print(n,"the number is notprime")
            break
        else:
            print(n,"the number is prime number")  


#10.program to palindrome or not

def ispalindrome(s):
    return s == s[::-1]# from front to rreverse or reverse to first it will be same

s = "malayalam"
ans = ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")  

#11.program to find the given number is even or not


mynumber = 10

if (mynumber%2)==0:
    print(mynumber,"this is even number ")
else:
    print(mynumber,"this is odd number")    


    