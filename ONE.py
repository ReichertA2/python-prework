# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Display a simple greeting."""
    print("\"hello" + "_" + user_name + "!\"")

hello_name('USERNAME')

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    """Display odd numbers"""
    num = 0
    while num < 100:
        num += 1
        if num % 2 == 0:
            continue
        print(num)
    return 
    
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of
#  a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    Max = a_list[0]
    for number in a_list:
        if number > Max:
            Max=number
    return Max

a_list = [1,3,5]
print(max_num_in_list(a_list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is
#  divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    
    if a_year % 400== 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True
    return False
        
a_year = 366
print(is_leap_year(a_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
# are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))






