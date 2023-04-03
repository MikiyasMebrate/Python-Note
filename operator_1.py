#Logical Operato and, or, not
age = 22
height = 1.76
complex_var = 3 * 3j

#Calculate Area of Triangle => 0.5 x b x h
base = input("Enter base: ")
height  = input("Enter Height: ")
area_of_triangle = 0.5*(int(base)*int(height))
print("The area of Triangle is: ", int(area_of_triangle))

#Calculate Area of perimeter of the triangle => perimeter = a + b + c
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter size c: "))
print("The perimeter of the triangle is: ", side_a+side_b+side_c)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length*width
perimeter = 2*(length+width)

print("Area: ", area)
print("Perimeter: ", perimeter)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y1,y2,x1,x2 = 2,2,10,6
print((y2-y1)/(x2-x1))

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python')>len('dragon'))


#In addition to the above comparison operator Python uses:

#is: Returns true if both variables are the same object(x is y)
#is not: Returns true if both variables are not the same object(x is not y)
#in: Returns True if the queried list contains a certain item(x in y)
#not in: Returns True if the queried list doesn't have a certain item(x in y)

print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'on' not in 'e')

#Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7)) #True

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))  #False

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
life = int(input("Enter number of years: "))
print(life*365*24*60*60)

m = "'hhh'"
print(m)