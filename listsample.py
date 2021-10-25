# MyList = [3, "dog", 9, "cat"]
# print (len(MyList))



# my_list = ['two', 5, ['one', 2]]
# print(len(my_list))



# MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
# print (MyList.count('dog'))




# MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
# x = MyList.count('car')
# print(x)





# my_list = [4, 'two' , 'one' ,5,3,2,'bye']
# print (my_list.index('one'))





# MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
# print (MyList.index(5))




# MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
# print (MyList.index('dog'))




# # MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
# # print (MyList.index('car'))



# # MyList = [1, 5, 67, 3, 4]
# # x = MyList.sort()
# # print (x)



# # MyList = [3, 7, 9, 0, 4]
# # MyList.sort()
# # print (MyList)





# MyList = ['cow', 'cat', 'dog', 'pet']
# MyList.sort()
# print (MyList)







# MyList = [3, "dog", 9, "cat"]
# MyList.extend([7,8])
# print (MyList)



# #Extend the list by appending all the items in the given list.
# MyList = ['dog',3]
# MyList.extend('cat')
# print (MyList)




# MyList = ['pet' , 'dog' ,5]
# MyList.append('cat')
# print(MyList)






# my_list = ['two' , 'one' ,5,3,2,'bye']
# my_list.append (['one',2])
# print(my_list)
  






# list.insert(i, x)	
# Insert an item at a given position. 
# The first argument is the index of the element to insert.

# my_list=[1,'dog',2.3]
# my_list.insert(2,'cat')
# print(my_list)











# MyList = [3, "dog", 9, "cat"]
# MyList.insert(1, [6, 9])
# print (MyList)






# MyList = [3, "dog", 9, "cat"]
# MyList.remove(3)
# print (MyList)







# MyList = [3, "dog", 9, "cat"]
# MyList.pop()
# print (MyList)





# MyList=[2,5,6,7,8,5]
# MyList.pop()
# print (MyList)





# MyList = [3, "dog", 0, "cat"]
# del MyList[0]
# print (MyList)

  
# MyList = [3, "dog", 9, "cat"]
# print (MyList.extend([7,8]))




# MyList = ['pet' , 'dog' ,5]
# print (MyList.append('cat'))







# my_list=[1,"dog",2.3]
# print(my_list.insert(2,"pet"))






# my_list = ['two' , 'one' ,5,3,2,'bye']
# print (my_list.remove('one'))






# MyList = ['pet' , 'dog' ,1]
# print (MyList.pop(1))





# MyList = ['pet' , 'dog' ,5]
# print (MyList.pop('dog'))
  




# my_list = []
# for x in range(2,11,3):
#     my_list.append(x)
# print(my_list)
  







# my_list = []
# for x in range(4,30,3.0):
#     my_list.append(x)
# print(my_list)








# a = range(3,20,4)
# b = []
# for k in a:
#     if k % 2:
#         b.append(k)
# print (b)







# my_list = []
# for x in range(1,10):
#     if not (x % 3):
#         my_list.append(x)
# print(my_list)










# def mul(k):
#     my_list=[]
#     for i in range(1,5+1):
#         n=i*k
#         my_list.append(n)
#     return my_list
# n=int(input("Enter the value : "))
# print(mul(n))







# Write a function that accepts two positive integers a and b 
# and returns a list of all the even numbers between a and b (including a and not including b).

# def even(a,b):
#     my_list=[]
#     for i in range(a,b):
#         if i%2==0:
#             my_list.append(i)
#     return my_list
# a=int(input("Enter the 1st number :"))
# b=int(input("Enter the last number : "))
# print(even(a,b))








# Write a function that accepts two positive integers 
# a and b (a is smaller than b)and returns a list that contains 
# all the odd numbers between a and b (including a and including b if applicable) 
# in descending order.



# def odd(a,b):
#     my_list=[]
#     for i in range(a,b+1):
#         if i%2!=0:
#             my_list.append(i)
#     return my_list

# a=int(input("Enter 1st number : "))
# b=int(input("Enter last number : "))
# print(odd(a,b))


# decending order
# def odd(a, b):
#     output_list = []
#     number = b
#     while number >= a:
#         if number % 2 != 0:
#             output_list.append(number)
#         number = number - 1
#     return output_list
# a=int(input("Enter 1st number : "))
# b=int(input("Enter last number : "))
# print(odd(a,b))








# Write a function that accepts a positive integer k and 
# returns the ascending sorted list of cube root values of all the numbers 
# from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]

# def cube_root(k):
#     my_list=[]
#     for i in range(1,k):
#         n=i**3
#         my_list.append(n)
#     return my_list
# k=int(input("Enter the integer : "))
# print(cube_root(k))










# Write a function that accepts a positive integer k and returns 
# the list of all the divisors of k. Your list should include both 1 and k.

def divisor(k):
    my_list=[]
    for i in range(1,k+1):
        if k%i==0:
            my_list.append(i)
    return my_list

k=int(input("Enter a positive integer : "))
print(divisor(k))

































