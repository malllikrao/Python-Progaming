#1. function to add integer values of the list

from typing import MappingView


mylists  = [1,2,3,4,5,6,7,8,9]

def myfunction(mylists):
    return sum(mylists)
    
myfunction(mylists) 

# lists have many methoda to addition,deltion of elements from lists
my_input = [10,20,30,40,50]
input2 = 50,60,70,80
my_input.append(input2)# append method involves in adding of lists from one into another
print(my_input)
my_input.extend(input2)# largening of lists
print(my_input)
my_input.insert(input2)# inserting values into lists
print(my_input)

#2.write a function to calcuate the average value of arrray of integers

def average(a,n):

    sum = 0

    for i in range(n):# range of n implies the total length
        sum+=a[i]# sum of numbers
    return sum/n    


# or

arr =  [1,2,3,4,5,6,7,8,9]
n = len(arr)# it imples total length of the list
print(n)
print(sum(arr)/n)# this finds the total average of numbers in the list

 #3.write a program to find the index of an array or list element

mahu  ="mallikarjunrao"
print(mahu)
mahu[0]
mahu[0:4:1]# here we can grab the elements in the list

#4.write a function to test if list contains specific value

my_list = ['mithun','sharath','mahu']

if my_list[0] == 'mithun':
    print("yes,this item is in the list")
else:
    print("the item is not in the list")    


#5.write a function to remove specific element from an array/list

mylist = ['a','b','c','d','e']
print(mylist)
mylist.remove('a')
print(mylist)

#6.write a function to copy an list to another list

arr1 = [1,2,3,4,5]
arr2 = [None]*len(arr1)
print(arr2)
for i in range(0,len(arr1)):
    arr2[i] = arr1[i]
print("elements of the originay lst:")
for i in range(0,len(arr1)):
    print(arr1[i])
print()

print("elements of new array:")
for i in range(0,len(arr2)):
    print(arr2[i])


#7. write a function to find the min and max value of an list

mylist = [1,2,3,4,5,6,7]
min(mylist)# to find the minimum value
max(mylist)# to find the maximum value

#8.write a function to insert an element at specific position in the list

mylist = [1,2,3,4,5,6,7]
mylist.insert(0,1)# at index 0 ,inserting number 1
mylist
# or
mylist = [2,3,4,5,6,7,8]
mylist[0] = 5
mylist

#9.write a function to reverse a integer value
mylist = [1,2,3,4,5,6,7,8,9]
print("the normal list is:",mylist)
rev  = mylist[::-1]
print("the reversed list is:",rev)

#10.write a function to find the duplicate values of the list

arr = [1,2,3,4,5,5,7,8,8]
print("duplicate elements in the list:",arr)

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if (arr[i] ==arr[j]):
            print(arr[j])


#11.write a program to find common values between  two lists


a  = [1,2,3,4,5]
b = [1,2,4,5]
def common(a,b):
    c = [value for value in a if value in b]
    return c
d = common(a,b)
print(d)

# or

a = [1,2,3,4]
b = [1,2,5,6]
def comon(lst1,lst2):
    return list(set(lst1)& set(lst2))

c = comon(a,b)
print(c)


#12. write a method to remove duplicate elements from a list

mylist  = [1,2,3,4,5,6,7,8,9,1,2,3]
# first thing we have to make it to ascending order
mylist.sort()
print(mylist)
# remove the duplicate elements in the list
updatedlist = list(set(mylist))
print(updatedlist)


#13. write a method to find the second largest nuumber in the list

list1 = [11,22,1,2,5,67,32,21]
# to get the unique list
new_list = set(list1)
print(new_list)
# first remove the largest number ,then we can remove the second largest number
new_list.remove(max(new_list))# this removes the first largest number
print(new_list)
print(max(new_list))# then we remove the second largest number

# 14.write a method to find the number of even numbers and odd numbers in the list
numbers = [1,2,3,4,5,6,7,8,9]
odd = []
even = []
for number in numbers:
    if int(number)%2 == 0:
        even.append(number)
    else:
        odd.append(number)



 # or

a = 0
b = 0

mylist  =[11,2,3,4,5]
for i in range(0,len(arr)):
    if (i%2 == 0):
        a+=1
    else:
        b+=1
print('there are{0} numbers that are even'.format(a))
print('there are {0}numbers that are odd'.format(b))            


#15.write a function to get the difference of largest and smallest value

mylst = [1,2,3,4,5]
print(mylist)
maxi = max(mylst)# prints the maximum value
print(maxi)
mini = min(mylst)# prints minimum value
print(mini)
difference = maxi -mini
print(difference)


# 16.write a program to remove the duplicate elements and return the new aray/list

mylist = [1,2,3,4,5,6,7,7,8,8,9,9]
print(mylist)
removedup = list(set(mylist))# this set the elements and remove the duplicates and return new list
print(removedup)




