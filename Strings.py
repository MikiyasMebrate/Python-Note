#Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings.
multiple_string = ''' I am student at American College of Technology'''
print(multiple_string)

#String Concatenation: We can connect strings together. Merging or connecting strings is called concatenation. See the example below:
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name

#Escape Sequences in Strings
#In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")

print("Days\tTopic\tExercises")
print("Day 1\t 5\t5")
print("Day 2\t 6\t10")
print("Day 3\t 5\t23")
print("Day 4\t 1\t35")
print("This is backslash symbol \\")
print("\"Hello World\"")


#New Style String Formatting (str.format)
first_name1 = "Mikiyas"
last_name1 = "Mebrate"
formmated_name = "I am {} {}".format(first_name1,last_name1)
print(formmated_name) #I am Mikiyas Mebrate

#String Interpolation / f-Strings (Python 3.6+)
formmated_name1 = f" I am {first_name1}"
print(formmated_name1)

#Slicing Python Strings In python we can slice strings into substrings.
language = 'python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]

#Reversing a String
greeting = 'Hello World'
print(greeting[::-1])

#Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #0 Starting Point 6 last Point
print(pto) # Pto

#String Methods
#capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())  

#count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y')) #3
print(challenge.count('y',7,14))  #Starting Point 7 and ending point 14 --> occurrence -> 1

#endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))  #True

#find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(challenge.find('y'))  #5

#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print(challenge.find('y'))  #16

#isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False


#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


#Exercises
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s1,s2,s3,s4 = 'Thirty','Days','Of', 'Python'
sentense = s1 + " " + s2 + " " + s3  +" " + s4
sentense2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sentense)
print(len(sentense))
print(sentense.upper())
print(sentense.lower())
print(sentense.replace('Thirty','three'))
print(sentense2.split(', '))