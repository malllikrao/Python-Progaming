my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
my_dict['key1']# dictionaries posses the key:value pairs,and find out the location through the key,value pairs
my_dict['key2']# gets value



# dictionaries are more flexible in data types they hold
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)
my_dict['key3']
my_dict['key2']
my_dict['key3']

# for the lists in the dictionaries ,we can call the index position of the dictionary

mydict = {'k':123,'f':[1,2,3],'g':['m','s','l']}

mydict['f'][0]# it grabs the index of the list


# methods in dictionary are

d = {'key1':1,'key2':2,'key3':3}
d.keys()# it grabs the dictionay keys
d.values()# it grabs the dictionary values
d.items()# it grabs the dictionary items


# nesting with dictionary

d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d)
d['key1']['nestkey']['subnestkey']# keep calling the keys ,we will get values

del d# delete the dictionary
print(d)



s = mydict

print(s)

# appending  can be done using adding key and value pair into the dictionary




