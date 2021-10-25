# import math
# x=math.sin(30)
# print(x)









# from math import sqrt,sin
# print(sqrt(4))
# print(sin(2))






# from math import*
# x=1
# y=sin(x)-cos(x)+sin(x)*cos(x)
# print(y)



# import math
# def _evaluate_expression_sample3_(x):
#     y = math.sin(x) - math.cos(x) + math.sin(x)*math.cos(x)
#     return y
# x=int(input("Enter x :"))
# print(_evaluate_expression_sample3_(x))









# from math import*
# def _evaluate_expression_sample4_(x):
#     y = abs(x**3)+cos(sqrt(3*x))
#     return y
# x=int(input("Enter value for x : "))
# print(_evaluate_expression_sample4_(x))








def _find_distance_sample_(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )**(1/2)
    return distance
a = [2, 3, -5] 
b = [4, -3, 12]
print(_find_distance_sample_(a,b))










#*******************************************Assignment*******************************************************

# Write a function that accepts two positive integers which are the height and width of a rectangle 
# and returns a list that contains the area and perimeter of that rectangle.



# def rectangle (l,b):
#     area=l*b
#     perimeter=2*(l+b)
#     return [area,perimeter]
# l=int(input("Enter the length for the rectangle : "))
# b=int(input("Enter the breadth for the rectangle : "))
# print(rectangle(l,b))










# Write a function that accepts a list of integers and returns the average. 
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

# def cal_average(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t           

#     avg = sum_num / len(num)
#     return avg

# print("The average is", cal_average([18,25,3,41,5]))
    













# Write a function which accepts an input list of numbers and 
# returns the largest number in the list (Do not use python's built-in max() function).

# def _find_min_sample_(sample_list):
#     my_max = sample_list[0]     
#     for item in sample_list:
#         if item > my_max:
#             my_max = item
#     return my_max
# sample_list=[]
# n = int(input("Enter the size :"))
# for i in range(0,n):
#     ele = int(input())
 
#     sample_list.append(ele)
# print(_find_min_sample_(sample_list))

