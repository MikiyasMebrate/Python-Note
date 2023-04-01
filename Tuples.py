#A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, ()


#Creating Empty Tuple
empty_tuple = ()
empty_tuple1 = tuple()

#Tuple with Intial Value
tpl = ("item1","item2","item3")

#Tuple Length
len(tpl)

#Accessign Tuple
first_Item = tpl[0]

#Slicing Tuple
all_item = tpl[0:3]
all_item = tpl[0:]
item2_3 = tpl[1:]


#Casting into List
lst = list(tpl)
print(lst)

#Checking Item
print('item1' in tpl)

#Deleting Tuple
del tpl

