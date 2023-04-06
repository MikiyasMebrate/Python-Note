#A module is a file containing a set of codes or a set of functions which can be included to an application. 
#A module could be a file containing a single variable, a function or a big code base.


#Importing a Module
#To import the file we use the import keyword and the name of the file only.
import my_module
print(my_module.full_name('Mikiyas','Mebrate'))


#Importing SPecific from module
from my_module import full_name
print(full_name('kaleab','hegie'))


#Import Functions from a Module and Renaming
from my_module import full_name as names

print(names('Abel', 'Berhe'))


#Import Built-in Modules
#1 OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder),
# fetching its contents, changing and identifying the current directory.

# import os
# # Creating a directory
# os.mkdir('directory_name')
# # Changing the current directory
# os.chdir('path')
# # Getting current working directory
# os.getcwd()
# # Removing directory
# os.rmdir()


#2 Statistics Module
#The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: 
# mean, median, mode, stdev etc.

from statistics import *
ages = [20,22,3,5,7,6,6,4,333,54,67,8,9,87,66]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#3 Math Module
#Mathematical Operation and constants 

import math
print(math.pi)
print(math.pow(2,3))
print(math.floor(9.81))


#4 Sring Module 
#useful module for many purposes 
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#4 Random Module 
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

