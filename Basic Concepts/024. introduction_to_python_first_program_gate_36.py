# Installing python is very easy, by installing we mean we install the pyton3 interpreter.

# Python is an interpreted language, which means that the code is executed line by line.
# It is very easy and intuitive to write code in python.
# Python does not require ';' at the end of the line.
# Python is case sensitive.
# Python is an object oriented language.
# Python is a high level language.
# Python is a dynamically typed language. (loosely typed)
# Python is an open source language.
# Python is a cross platform language and general purpose language.
# Python is a scripting language.

print("Let's enter the world of Python")

#Let's learn more about Pyton right here!

#Starting with the Basics Sytnax: -

## Variables & Basic Operations
# Variables are used to store data, and can be used to perform operations on the data. (they give meaning to the data and make it easier to understand)

a = 3      # put 3 in a
b = a      # put a in b
a = a + 1  # put a+1 back into a
num1 = a*b # Put the value of a*b into the variable num1
num2 = 99 # Put the value of 99 in the variable num2
#Quiz Time:
print(a)   # What is the value of a?     Ans: 4
print(b)   # What is the value of b?     Ans: 3
print(num1) # What is the value of num1? Ans: 12
print(num2) # What is the value of num2? Ans: 99


## Data Types
## Python has 4 basic data types: int, float, str, bool

# Number (int, float) and Strings (str) data types
name = 'bob' # Variables can contain strings,
num = 12 # may contain a number,

is_number = True # True or False -> "Boolean" can also be entered.

# List type (same as Javascript array type)
# List is a collection of items, it can contain different data types (similar to struct in C)
# List is defined by square brackets [] and can be accessed by index
# List can be modified (add, remove, change) after it is created (mutable) 

a_list = []
a_list.append(1)     # Put a value in the list
a_list.append([2,3]) # Put the list [2,3] back into the list

# What is the value of a_list?            Ans: [1,[2,3]]
# What is the value of a_list[0]?         Ans: One
# What is the value of a_list[1]?         Ans: [2,3]
# What is the value of a_list[1][0]?      Ans: 2

# Dictionary (dict) type (same as Javascript object type)(similar to struct in C?)

a_dict = {}
a_dict = {'name':'bob','age':21}
a_dict['height'] = 178

# What is the value of a_dict?                      Ans: {'name':'bob','age':21,'height':178}
# What is the value of a_dict['name']?              Ans: 'bob'
# What is the value of a_dict['age']?               Ans: 21
# What is the value of a_dict['height']?            Ans: 178

# Combination of Dictionary and List types
people = [{'name':'bob','age':20},{'name':'carry','age':38}]

# What is the value of people[0]['name']? 'bob'
# What is the value of people[1]['name']? 'carry'

person = {'name':'john','age':7}
people.append(person)

# What are the values of people? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# What is the value of people[2]['name']? 'john'

#Tuple type
# Tuple is a collection of items, it can contain different data types (similar to struct in C)
# Tuple is defined by parentheses () and can be accessed by index
# Tuple cannot be modified (add, remove, change) after it is created (immutable)
