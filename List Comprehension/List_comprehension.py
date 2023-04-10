#List Comprehension
#List comprehension in Python is a compact way of creating a list from a sequence. 
#It is a short way to create a new list. List comprehension is considerably faster than processing a
# list using the for loop.


#Syntax 
## syntax
#[i for i in iterable if expression]

language = 'python'
lst = [i for i in language]
print(lst)

numbers = [i for i in range(10) if i%2==0]
print(numbers)


square = [i*i for i in range(11)]
print(square)

print()
print()
number_square = [(i, i*i) for i in range(11)]
print(number_square)

number_square = [[i,i*i] for i in range(11)]
print(number_square)



#Lambda Function
#Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.
square = lambda x: x**2
print(square(3))


loop_lambda = lambda x : [x for i in range(x) if i%2==0 ]
print(loop_lambda(10))


#Exercises
#1 Filter only negative Numbers
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_number = [i for i in numbers if i<0]
print(negative_number)

#2 Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list_of_number = [i for row in list_of_lists for j in row for i in j] 
print(list_of_number)

#3 Using list comprehension create the following list of tuples:
ten_by_ten = [(i,1,i,i*i,i*i*i,i*i*i*i,i*i*i*i*i) for i in range(11) ]
print(ten_by_ten)

#4 Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_code = [[i[0].upper(), i[0][0:3].upper(), i[1].upper()] for count in countries for i in count]
print(countries_code)

#5  list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_contries = [{'country':i[0],'city':i[1]} for count in countries for i in count]
print(dict_contries)


# 6 Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_name  = [i[0]+" "+i[1] for full in names for i in full]
print(full_name)