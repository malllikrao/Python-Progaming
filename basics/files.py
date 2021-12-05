# write a program to read and write into the file and at last check wheather file having the read or write acesses
# and write into the file and read file by seek()method

#Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

#Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

#When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.


#f = open(filename, mode)(mode = r,w,w+,a,r)# write ,read,append

myfile = ("file.text",'r')# read the file

# a file named "mallik", will be opened with the reading mode.
file = open('mallik.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print (each)


# Python code to illustrate read() mode
file = open("file.text", "r")
print (file.read())


# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))

# Python code to create a file
file = open('mallik.txt','w')# file for writing
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Python code to demonstrate
# use of seek() function

	
# Opening "GfG.txt" text file
# in binary mode
f = open("data.txt", "rb")

# sets Reference point to tenth
# position to the left from end
f.seek(-10, 2)

# prints current position
print(f.tell())

# Converting binary to string and
# printing
print(f.readline().decode('utf-8'))

f.close()

# deleting of text file
import os
os.remove("file.txt")
# checking file exists or deleted
import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")



  # Open a file, reading and seek function
fo = open("foo.txt", "rw+")
print ("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opend file
fo.close()





