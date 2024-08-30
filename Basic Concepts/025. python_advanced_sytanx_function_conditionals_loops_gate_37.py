# In math problems

# f(x) = 2*x+3
# y = f(2)
# y value?      Ans: 7

# In JavaScript

# function f(x) {
# 	return 2*x+3
#  let y = f(2)
# }

# In python
def f(x):
	return 2*x+3
print(f(2))

## Application of functions:
def sum(a,b,c):
	return a+b+c

def mul(a,b):
	return a*b

result = sum(1,2,3) + mul(10,10)
print(result)
# What is the value of the result? 106

# Define a function named oddeven. It takes num as a variable.
# If the remainder of num divided by 2 is 0
# Returns True.
# else,
# Returns False.
def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = oddeven(20)
print(result)
# What is the value of result? True

def is_adult(age):
	if age > 20:
		print('Adult')    # If the condition is true, print 'Adult'
	else:
		print('Youth')  # If the condition is false, print 'Youth'

is_adult(30)
# What will be printed? Adult


print("") # print gives a \n by deault 
# if I write print("\n") it will give two new lines

## Loops: In Python, we can use loops to pull out the elements of a list one by one.
fruits = ['Apple','Pear','Pear','Banana','Watermelon','Tangerine','Strawberry','Apple','Pear','Watermelon']

count = 0
for fruit in fruits:
    if fruit == 'Apple':
        count = count + 1
    print(fruit)

# print("Apple comes",count,"times")

# To do the same thing as above but to makie it more efficient, we can use a function
def count_fruits(target):
	count = 0
	for fruit in fruits:
		if fruit == target:
			count += 1
	return count

watermelon_count = count_fruits('Watermelon')
print(watermelon_count) # 2

pear_count = count_fruits('Pear')
print(pear_count) # 3

apple_count = count_fruits('Apple')
print(apple_count) # 2


## Let's look at a little more complex example
# This time we will have a list of dictionaries
people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'],":",person['age'])
    
# Output:
# bob : 20
# carry : 38
# john : 7
# smith : 17
# ben : 27

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return 'No such name exists'


print(get_age('bob')) # 20
print(get_age('kay')) # No such name exists