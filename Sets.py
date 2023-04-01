#Set is a collection of items. Set is a collection of unordered and un-indexed distinct elements.
# possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

#Creating sets we use curly bracket
st = {}
#OR
st = set()

#Creating a set with initial items
st = {'item1', 'item2', 'item3'}

#Length
len(st)

#Accessing Items in a Set We use loops to access items. We will see this in loop section

#Once a set is created we cannot change any items and we can also add additional items.
st.add('item4')
#Multiple
st.update(['item5', 'item6', 'item4'])
print(st)

#Remove
st.remove('item1')

#The pop() methods remove a random item from a list and it returns the removed item.
st.pop()  #random element 

#Clearing
st.clear()

#deleting
del st

#Join
#Union 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8','item1'}
st3 = st1.union(st2)
print(st3)

#Intersection 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}