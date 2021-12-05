# different ways of creating strings and usage

# string indexing
s = 'mahu'
s[1]
print(s[1])# prints the index postion of the string


# string slicing

s = 'mallikarjun rao'
s[::-1]# slicing having three types which involves start index ,stop index and step size of index
# single line quptes 
s = 'mahu'
print(s)

# multiple line quotes
s = "mahu"
print(s)
#string concatenation
s = "mahu"
print(s+"how are you?")


# to find the length of the string

s = "mallikarjunrao"
len(s)# this is bulit in method to finc tthe length

# adding up with two strings using concatenation

s = "mahu"
b = "bhanu"
k = s+b
print(k)
# or we can print the string using the fstring or .format method,this are called print formattting

# extract substring from mainstring

mainstring  = "mallik"
mainstring[::-1]# through this slicing we can extrect the sub string 

# strings with methods

s = "mallikarjun"
s
s.upper()
s.split()
s.lower()
s.startswith('s')# returs boolen 
s.endswith('k')


s = "mallik"
b = "bhanu"
print("hii this is {} and this is {}".format(s,b))