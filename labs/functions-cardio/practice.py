import random
from math import sqrt

def longest_word(*args_compare):
    longest = ""
    for compare in args_compare:
        if len(longest) < len(compare):
            longest = compare
    return longest

def reverse_string(arg):
    return arg[::1]

def sum_to_n(num):
    total = 0
    for i in range(1, int(num) + 1):
        total += i
    return total

def is_triangle(s1,s2,s3):
    if s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2):
        return True
    else:
        return False

def roll_dice(numDice,numFace):
    sum = 0
    rand = 0
    ind_dice = []
    for i in range(numDice):
        rand = random.randint(1,numFace)
        sum += rand
        ind_dice.append(rand)
    print(ind_dice)
    return sum

def isPrime(num):
    prime = False
    for i in (2,int(sqrt(num))):
        if not num % i == 0:
            prime = True
    if prime:
        return "Prime"
    else:
        return "Not prime"
    
def snake_case(camel_arg):
    index = []
    for i in camel_arg:
        if(i.isupper()):
            index.append(i)
    snake_str = ""
    for j in index:
        snake_str = camel_arg.replace(j,("_%s" % j.lower()))
    return snake_str

def get_num_input(prompt):
    num = raw_input(prompt)
    if(isinstance(num, int)):
        get_num_input(prompt)