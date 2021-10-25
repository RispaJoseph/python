# hours = int(input("how many hours did you work this week? "))

# if hours  < 0 or hours > 168:
#     print("invalid")
#     #here i used sys.exit so that it can exit after printing invalid
#     sys.exit()
# elif hours  <= 40 and hours > 0:
#     a = hours
#     b = 0
#     c = 0 
# elif hours>40 and hours <= 50:
#     a = 40
#     b = (hours - a)
#     c = 0
# elif hours > 50:
#     a = 40
#     b = 10
#     c = hours - (a+b)

# rate = (a*8)+(b*9)+(c*10)
# print("\n\nYOU MADE {} DOLLARS THIS WEEK".format(rate))




# n=int(input("Enter an integer : "))
# if n < 0 or n >168:
#     print("INVALID")
# elif n<=40:
#     rate=n*8
#     print("YOU MADE",rate,"DOLLARS THIS WEEK")
# elif 41 <= n <= 50:
#     rate=(40*8)+(n-40)*9
#     print("YOU MADE",rate,"DOLLARS THIS WEEK")
# else:
#     a=40
#     b=10
#     c=n-(a+b)
#     rate=(a*8)+(b*9)+(c*10)
#     print("YOU MADE",rate,"DOLLARS THIS WEEK")







# m = 0
# for x in range(1,4):
#     for y in range(1,3):   
#         m = m + 1
# print (m)





# m = 0
# for x in range (1,3):
#    for y in range (4,6):
#       m = m + x + y
# print (m)






# m = 0
# for x in range (1,3):
#    k = 0
#    for y in range (-2,0):
#       k = k + y
#       m = m + k
# print (m)






# m = 0
# for x in [3,5,3]:
#    for y in range (10,11):
#       m = m + x + y
# print (m)











# m = 0
# x = 1
# while x < 4:
#     y = 1
#     while y < 3:
#         m = m + x + y
#         y = y + 1
#     x = x + 1
# print(m)











# m = 0
# x = 1
# while x < 4:
#     y = 1
#     while y < 5:   
#         m = m + y
#         y = y + 1
#         if x + y == 5:
#             break
#     x = x + 1
# print (m)














# m = 0
# x = 10
# while x > 8:
#     for y in range(1,3):
#         m = m + 1
#     x = x - 1
# print(m)



# m = 1
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x == y:
#             m = m * x 
# print (m)








# m = 1
# my_list_1 = [2 , 4, 1]
# for x in my_list_1:
#     for y in range(1,3):
#         if (x + y) % 3:
#             m = m * x
# print (m)








# m = 0
# my_str_1 = "university"
# my_str_2 = "mississipy"
# for char_1 in my_str_1:
#     for char_2 in my_str_2:
#         if char_1 == char_2:
#             m = m + 1
# print(m)










#.............function.................
# def test(x):
#     a=7
    
# # Main Program
# print(test(5))





# def my_fun(a):
#     return a*2

# # Main Program #
# print(my_fun(2) + my_fun(3))










# def my_fun(a):
#     return a*2

# # Main Program #
# print(my_fun(my_fun(2)))




# count = 0
# for x in range(2,5):
#     count = count + x
# print(count)


# k = 10
# while k > 2:
#     x = k / 2
#     k = k - 1
# print(x)




# count = 10
# for x in range(0,7):
#     count = count + 2
#     if x == 4:
#         break
# print(count)




# k = 1
# count = 0
# while count < 10:
#     if k % 4 == 0:
#         break
#     count = count + k
#     k = k + 1
# print(count)




# my_list = ["pet" ,"dog", 35, "cat", 23]
# count = 0
# for item in my_list:
#     if type(item)== str:
#         continue
#     count = count + 1
# print(count)






# m = 0
# my_str= "mississipi"
# for char in my_str:
#     if char == "s":
#         continue
#     if char == "p":
#         break
#     m = m +1
# print(m)








# m = 0
# for x in range (4,6):
#    for y in range (2,4):
#       m = m + x + y
# print (m)







# m = 0
# x = 1
# while x < 5:
#     y = 1
#     while y < 4:
#         m = m + y
#         y = y + 3
#     x = x + 2
# print(m)






# m = 0
# my_list_1 = [1, 2, 5]
# my_list_2 = [1, 3, 2, 6, 5]
# for x in my_list_1:
#     for y in my_list_2:
#         if x == y :
#             m = m + 1
# print (m)





# m = 0
# my_list_1 = [1, 2, 5]
# my_list_2 = [1, 3, 2, 6, 5]
# for x in my_list_1:
#     for y in my_list_2:
#         if x == y :
#             m = m + 1
# print (m)







# m = 0
# my_str_1 = "cat"
# my_str_2 = "pet"
# for char_1 in my_str_1:
#     # for char_2 in my_str_2:
#     #     if char_1 != char_2:
#     m = m + 2
# print(m)






# def say_hello():
#     print('Hello Universe!') 
# say_hello()






# def func(x):
#     x = 2
#     print('x is', x)
# func(50)





# def even(x):
#     if x % 2 == 0:
#         return x
#     else:
#         return x+1
# print(even(3))




# def cube(x):
#     return x * x * x   
# y = cube(3)    
# print(y)





# def fun(x, y, z): 
#     z = x * y
#     return x + y + z
# print(fun(2, 30))




# def fun1(x,y):
#    z = multiply(x,y)
#    m = x + z
#    return m
  
# def multiply(a,b):
#    n = a * b
#    return n
  
# x = 2
# y = 4
# z = fun1(x,y)
# print (x,y,z)





# def my_fun(x):
#     for m in range(0,3):
#         n = 2
#         while n <= 4:
#             if m == n:
#                 x = x + 1
#             n = n + 1
#     return x
# print(my_fun(5))







# for i in range(4):
#     for j in range(4):
#         print("*",end='')
#     print()












# Write a function that accepts a list of integers as parameter. 
# Your function should return the sum of all the odd numbers in the list. 
# If there are no odd numbers in the list, your function should return 0 as the sum.

# def odd_numbers (my_list):
#     total = 0
#     for number in my_list:
#         if (number % 2 == 1):
#             total = total + number 
#     return (total)
# my_list=[]
# n=int(input("Enter the size : "))
# for i in range(0,n):
#     ele=int(input())
#     my_list.append(ele)

# print(odd_numbers(my_list))






# Write a function that receives a positive integer as function parameter and 
# returns True if the integer is a perfect number, False otherwise. 
# A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to 
# itself. For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. 
# Therefore, 6 is a perfect number.

# def absolute_number(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
#     if(sum==n):
#         return True
#     else:
#         return False

# n=int(input("Enter a absolute number : "))
# print(absolute_number(n))






# Write a function that accepts a positive integer n as function parameter and 
# returns True  if n is a prime number, False otherwise. 
# Note that zero and one are not prime numbers and two is the only prime number that is even.


# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# n=int(input("Enter the number : "))
# print(test_prime(n))





# Write a function that accepts two positive integers as function parameters 
# and returns their least common multiple (LCM). 
# from math import*
# import math
# def least(n,m):
#     math.lcm(n,m)
     
# n=int(input("Enter 1st integer : "))
# m=int(input("Enter 2nd integer : "))
# print(least(n,m))






# def lcm(x, y):
#     for i in range(max(x,y), (x*y)+1):
#          if((i % x == 0) and (i % y == 0)):
#               return i
# x=int(input("Enter 1st integer : "))
# y=int(input("Enter 2nd integer : "))
# print(lcm(x,y))


# n=int(input("enter n: "))
# for i in range(1,n):
#     print (n*i)


















# Python Program to find the L.C.M. of two input number

def _least_common_multiple_sample_(a, b):
    # first make a backup/copy of a
    copy_of_a = a
    # While the remainder when a is divided by b is not 0
    # continue to add a to its backup (copy_of_a)
    while (copy_of_a % b) != 0:
        copy_of_a = copy_of_a + a
    return copy_of_a
    
a=int(input("Enter first number: "))  
b=int(input("Enter second number: "))  
print(_least_common_multiple_sample_(a,b))




# Python Program to find the LCM of Two Numbers using GCD 
# num1 = int(input())
# num2 = int(input())
# a = num1
# b = num2
# while(num2 != 0):   # When num2 is not equal to 0 # Swap num2 with num1 using temp
#     temp = num2
#     num2 = num1 % num2   # Modulus of num1 and num2
#     num1 = temp
# gcd = num1  
# lcm = (a * b) // gcd   # LCM is found using GCD
# print(lcm)







# def lcmul(a,b):
#     # a = num1
#     # b = num2
#     while(num2 != 0):   # When num2 is not equal to 0 # Swap num2 with num1 using temp
#         temp = num2
#         num2 = num1 % num2   # Modulus of num1 and num2
#         num1 = temp
#         gcd = num1  
#         lcm = (a * b) // gcd 

# num1 = int(input())
# num2 = int(input())
# a = num1
# b = num2
# print(lcmul(a,b))



# defining a function to calculate LCM  
# def calculate_lcm(x, y):  
#     # selecting the greater number  
#     if x > y:  
#         greater = x  
#     else:  
#         greater = y  
#     while(True):  
#         if((greater % x == 0) and (greater % y == 0)):  
#             lcm = greater  
#             break  
#         greater += 1  
#     return lcm    
  
# # taking input from users  
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: "))  
# # printing the result for the users  
# print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  







# def findgcd(a, b):
#     if(b == 0):
#         return a
#     else:
#         return findgcd(b, a % b)
    
# num1 = float(input(" Please Enter the First Value  Num1 : "))
# num2 = float(input(" Please Enter the Second Value Num2 : "))

# gcd = findgcd(num1, num2)
# # print("\n GCD of {0} and {1} = {2}".format(num1, num2, gcd))

# lcm = (num1 * num2) / gcd
# print(format(num1, num2,lcm))




# import NumPy as np
# num1=4
# num2=6
# x=np.lcm(num1,num2)
# print(x)


