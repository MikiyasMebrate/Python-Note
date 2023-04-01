# There are four collection data types in Python :

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

#A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.
#In to ways lists can be created
#1
lst = list()
print(len(lst))  #0

#2
lst = ['banana','orange','mango','lemon']
print("Fruits: ",lst)

#Unpacking List Items
first_name,last_name,*others = lst;  # * Symbol->rest all 
print(first_name + " "+last_name+" "+str(others))

first,second,third,*other, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(other)
print(tenth)

#Slicing Items from a List
all_fruits = lst[0:4]
print(all_fruits)
print(lst[0][0:4])   #bana


#Adding Item to a List
lst1 = list()
lst1.append("Mike")
print(lst1)


#Inserting Items into a List in Specific Position
lst = ['item1', 'item2']
lst.insert(0,"item0")
print(lst)


#Removing Item from list
lst.remove('item0')
print(lst)

#The pop() method removes the specified index, (or the last item if index is not specified):
lst.pop(0)  
#The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
#del lit[index]
del lst[0]

# Clearing List Items
# The clear() method empties the list:
lst.clear()  #[]


#Joining Lists
list1 = list()
list2 = list()
list3 = list1 + list2

#Ecercises 
name = []
names = ['Mikiyas','kaleab','Abel','kaleb','list']  
#finding length
print(len(names))

#get the first item, middle and last item
print(names[0])  #First Item
print(names[int(len(names)/2)]) #Middle Item
print(names[len(names)-1]) #Last Item


#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Mikiyas', 22 , 1.76, False, 'Signal']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)  
print(len(it_companies))
it_companies.append('HP')
print(it_companies)

it_companies.insert(int(len(it_companies)/2), 'Toshiba')
print(it_companies)

it_companies[0].upper()
it_companies[1].upper()


ages = [19,22,19,20,25,24,25,24]
ages.sort()
print(ages)
print(min(ages))