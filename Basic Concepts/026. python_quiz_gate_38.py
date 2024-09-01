#Create a function that prints out a person’s gender (male or female) based on their “registration number”.
# def check_gender(pin):
#     if int(pin[7]) % 2 == 0:
#         print('male')
#     else:
#         print('female')
    
# my_pin = '200101-3012345'
# check_gender(my_pin)

# Alternative Solution
# def check_gender(pin):
#   num = int(pin.split('-')[1][0])

# if num % 2 == 0:
#     print("female")
# else:
#     print("male")
    

#Q2. Access the Science Score of person named Smith from the list of following dictionary 
# people = [
#     {"name": "bob", "age": "20", "score":{"math": 90, "science": 70}},
#     {"name": "carry", "age": "38", "score":{"math": 40, "science": 72}},
#     {"name": "smith", "age": "28", "score":{"math": 80, "science": 90}},
#     {"name": "john", "age": "28", "score":{"math": 80, "science": 90}},
# ]
# Solution: 1
# for person in people:
#     if(person['name'] == 'smith'):
#         print(person['score']['science'])
#         break
# Solution: 2
# science_score = people[2]['score']['science']
# print(science_score)

#Q3.  Print out only the even numbers from the below list

num_list = [1,2,3,6,3,2,4,5,6,2,4]

# for num in num_list:
#     if num % 2 == 0:
#         print(num)
        
#Q4.  Print the count of all the even numbers in the above list
# count = 0
# for num in num_list:
#     if num % 2 == 0:
#         count +=1

# print(count)

#Q5. Print the sum of all the numbers in the above list
# sum = 0
# for num in num_list:
#     sum = sum + num

# print(sum)

# we can do the same as above using the sum() function
# print(sum(num_list)) gives the sum all the elements in the list