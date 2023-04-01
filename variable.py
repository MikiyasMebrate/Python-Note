#Practice 2:30 days of python programming 

#Level 1
first_name ='Mikiyas'
last_name = 'Mebrate'
full_name = 'Mikiyas Mebrate'
country = 'Ethiopia'
city = 'Addis Ababa'
age = 22
year = 2000
is_married = False
is_true = True
is_light_on = False

level, batch = "bachelor's degree", "B2"


#Level 2
#1 Check data types of all variable
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2  Find the length of your first name
print("First Name Length: ",len(first_name))

#3 Compare length of first name and last name
if(len(first_name) > len(last_name)): print("First Name")
else: print("Last Name")

#4 Declearing variable
num_one, num_two = 5,4
total = num_one + num_two
diff = num_one - num_two
division = num_one / num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

#5 Calculate Radius
radius = input("Enter the radius of Circle: ")
pi = 3.14
area_of_circle = pi*(radius**2)
circumference_of_circle = 2*area_of_circle

#6 check keywords in python 
help('keywords')