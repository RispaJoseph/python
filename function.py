# This function prints "Hello there!" when it's called

# def hello():                                    #function definition               
#     print("Hello There!")
# hello()                                         #function calling




# for k in range(1,5):
#     print("k is equals to",k)
#     hello()









# def hello(input_string):
#     print("Your input string is ",input_string)
# for k in range(1,5):
#     print("k is equal to ",k)
#     # hello("Rispa")
#     s="Rispa"
#     hello(s)



# def add(a,b):
#     print(a+b)
# add(2,3)






#functions and arguments
# 1. Nothing goes in, nothing comes out. 

# def display_message():
#     print("****   PYTHON IS GREAT   ****")
#     print("=============================")
    
# # Main Program #
# radius = 5
# print("The radius of the circle is: ", radius)
# display_message()    # The function call 

# circumference = 2*3.14*radius
# print("The circumference of the circle is:", circumference)
# display_message()    # The function call 








# .............2. Nothing goes in, something comes out............... 

# function does not receive any arguments but each time we call this function it returns 
# a random integer between 20 and 100 and assigns the returned value 
# to the variable the function call was set equal to.

# import random

# def report_random():
#     #randint() function to get a random integer number from the inclusive range
#     my_number = random.randint(20, 100)   
#     return my_number

# # Main Program #
# a = report_random()    # return a random int and assign it to a
# print("a is equal to ", a)
# b = report_random()    # return a random int and assign it to b
# print("b is equal to ", b)
# c = report_random()    # return a random int and assign it to c
# print("c is equal to ", c)







#....................3. Something goes in, nothing comes out.........................

# This function does receive two arguments length and breadth and when we call this function, 
# it calculates the area and perimeter of a rectangle and prints the results 
# but it does not return anything! And again printing something is not the same as returning some value.
# The return value once again for this function is None as there is no return keyword.

# def calculate_area(length, breadth):
#     area = length * breadth
#     perimeter = 2*length + 2*breadth
#     print("area is equal to", area)
#     print("perimeter is equal to", perimeter)

# # Main Program #
# calculate_area(10, 20)





#.....................4. Something goes in, something comes out................................

# def calculate_area(length, breadth):
#     area = length * breadth
#     perimeter = 2*length + 2*breadth
#     my_result = [area, perimeter]    # put results in a list
#     return my_result                 # return the list
#     # return area,perimeter            # return as the tuple

# # Main Program #
# my_list = calculate_area(10, 20) # two arguments are supplied 
# print("The resulting list looks like:", my_list)







# ...................................Built-in-functions.......................

# 1. abs(x) - This method returns the absolute value of a number.

# my_value = -11.55                             # Notice that my_value is a negative floating point number
# absolute = abs(my_value )                     # Return the absolute value 
# print("The absolute value is:", absolute)  










# # 2. len(x)- This method returns the length (the number of items) of an object.

# my_list = ["abs", "len", 1, 2, "many", "more to come"]      # Create a list called "my_list"
# my_size = len(my_list)                                      # Return length (the number of items) of my_list
# print("The length of my_list is:", my_size)   












# 3. max(iterable, *[, key, default])
#    max(arg1, arg2, *args[, key])    -   This method returns the largest item in an iterable or the largest of two or more arguments.


# my_list = [-10, 12, 111, 32.3, 0, 4, 24]                        # Create a list called "my_list"
# my_max1 = max(my_list)                                          # Return the largest item in my_list
# my_max2 = max(my_list[0], my_list[-1])                          # Return the largest among first & last element
# print("The largest item of my_list is:", my_max1)               # Print my_max1 to see what was returned
# print("The larger among first and last item is:", my_max2) 













# 4. min(iterable, *[, key, default])
#    min(arg1, arg2, *args[, key]) 
#  This method returns the smallest item in an iterable or the smallest of two or more arguments.


# my_list = [10, -12, 11, 32.3, 1, 14, -5]                         # Create a list called "my_list"
# my_min1 = min(my_list)                                           # Return the smallest item in my_list
# my_min2 = min(my_list[0], my_list[-1])                           # Return the smallest among first & last element
# print("The smallest item of my_list is:", my_min1)               # Print my_min1 to see what was returned
# print("The smaller among first and last item is:", my_min2)    


















# 5. pow(x, y[, z]) 


# x = 5                                                   # initialize a variable x
# y = 3                                                   # initialize a variable y
# result = pow(x, y)                                      # Return x to the power of y. Same as x**y
# print("The result of the operation is", result)   







# 6. sorted(iterable[, key][, reverse])

# Lets sort the following list by the first item in each sub-list. 
# my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]
# # First, we need to define a function that specifies what we would like our items sorted by
# def my_key(item):
#     return item[0]                                            # Make the first item in each sub-list our key
# new_sorted_list = sorted(my_list, key=my_key)                 # Return a sorted list as specified by our key
# new_sorted_list1 = sorted( my_list, reverse=True)
# print("The sorted list looks like:", new_sorted_list)   
# print("The sorted list looks like:", new_sorted_list1)      










# 7.sum(iterable[, start])   - sum() function calculates the total of all numerical values in an iterable.

# my_list = [1, 2, 3, 4, 5]                        # Create a list
# my_sum  = sum(my_list)                           # Return the sum of the list
# print("The sum of my list is :", my_sum)  












# 8. zip(*iterables) - The Python zip() function accepts iterable items and merges them into a single tuple.

# x = [1, 2, 3, 4, 5]                                      # Create a list
# y = ['a', 'b', 'c']                                      # Note that this list only has 3 elements
# zipped = list(zip(x, y) )                                # Return the zipped object as a list of tuples
# print("The result of the operation is:", zipped)   
















#*************LAB**************

# Write a function that accepts a number as argument and returns the square of the number. 
# For example if the number passed to the function is 5 then your function should return 25.

# def num(a):
#     return a*a
# print("The sqaure of the number is",num(6))



# Write a function that accepts a number as input argument 
# and adds 5 to it and returns the resulting number


# def number(k):
#     result = k + 5
#     return result

# k=float(input("Enter a number :"))
# print(number(k))



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
# 	    return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))




# Write a function that a accepts a positive number 'r' as the radius of a circle
# and calculates and returns the area of the circle. Use the value of pi as 3.14

# def circle(r):
#     radius=(r**2)*(3.14)
#     return radius
# r=int(input("circle : "))
# print(circle(r))








# Write a function that accepts a list of integers and returns the sum of all the numbers in the list. 
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

# def _find_sum_sample_(sample_list):
#     # At first initialize total_sum to 0
#     my_sum = 0
#     # Iterate through the list
#     for item in sample_list:
#         # Add each element to my_sum
#         my_sum = my_sum + item
#     return my_sum
# sample_list=[]
# n = int(input("Enter the size :"))
# for i in range(0,n):
#     ele = int(input())
 
#     sample_list.append(ele)
# print(_find_sum_sample_(sample_list))







# Write a function that accepts three numbers 
# and calculates their product and returns the result.

# def fun(a,b,c):
#     result=a*b*c
#     return result
# a=int(input("Enter value for a : "))
# b=int(input("Enter value for b : "))
# c=int(input("Enter value for c : "))

# print(fun(a,b,c))









# Write a function which accepts an input list of numbers and 
# returns a list which includes only the even numbers in the input list. 
# If there are no even numbers in the input numbers then your function should return an empty list.

# def _return_even_numbers_(sample_list):
#     # Create an empty list
#     even_numbers=[]
#     # Iterate through the input list
#     for item in sample_list:
#         # determine if an element is even
#         if item%2 == 0 :
#             even_numbers.append(item)
#     # finally return the list of even numbers
#     return even_numbers

# sample_list=[]
# n = int(input("Enter the size :"))
# for i in range(0,n):
#     ele = int(input())
 
#     sample_list.append(ele)
# print(_return_even_numbers_(sample_list))












# Write a function which accepts an input list of numbers and returns the smallest number 
# in the list (Do not use python's built-in min() function).

# def _find_min_sample_(sample_list):
#     # Initially set the first element
#     # of the list as the minimum
#     my_min = sample_list[0]     # this is your current minimum
#     # Iterate through the list
#     for item in sample_list:
#         # Compare each item from the list
#         # to the current minimum. If the item is smaller
#         # than your current minimum then set that item
#         # to be your current minimum instead
#         if item < my_min:
#             my_min = item
#     # finally return the minimum value
#     return my_min
# sample_list=[]
# n = int(input("Enter the size :"))
# for i in range(0,n):
#     ele = int(input())
 
#     sample_list.append(ele)
# print(_find_min_sample_(sample_list))








# polynomial expression

# def fun(x):
#     y=x**4 - 12*x**3 + 13*x**2* +11
#     return y
# print(fun(11.1))




# def _calculate_payment(principle, interest_rate_per_year, duration,number_of_payments):
#     if interest_rate_per_year==0:
#         return principle/(duration*12)
#     r=interest_rate_per_year/100/12
#     n=duration*12
#     montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
#     return montly_payment
# print(_calculate_payment(1000.0,4.5,5))





# def find_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
# find_max(3, 4)








