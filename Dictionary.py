#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
#Creating Dictionary

empty_dict = dict()
dct = {
    'key1':'Value1',
    'key2':'value2',
    'key3':'value3'
}

persion = {
    'first_name':'Mikias',
    'last_name':'Mebrate',
    'age':'22',
    'country':'Ethiopia',
    'is_married': False,
    'skills':['JavaScript','python','Java'],
    'address':{
       'street':'Signal Street',
       'zipcode': '02210'
    }
}

#length of Dictionary
len(persion)

#Accessing Items
#We can access Dictionary items by referring to its key name.

print(persion['first_name'])
print(persion['address']['street'])

#to get avoid we use get method
print(persion.get('first_name'))
print(persion.get('city'))

#Adding Element
persion['key1'] = 'value1'
persion['skills'].append('HTML')
print(persion)

#Checking key in Dictionary
print('key' in persion)
print('first_name' in persion)

#Removing Key and Value
persion.pop('first_name')
del persion['address']
print(persion)

#Casting into list
print(persion.items())

#Getting Keys
print(persion.keys())
#Getting Values
print(persion.values())