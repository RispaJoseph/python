# def find_sum_odd(sample_list):
#     odd_number=[]
#     my_sum=0
#     for item in sample_list:
#         if (item%2)!=0:
#             odd_number.append(item)
#             return odd_number
#         else:
#             return 0 
# sample_list=[]
# n=int(input("Enter the size : "))
# for i in range(0,n):
#     ele=int(input())
#     sample_list.append(ele)
# print(find_sum_odd(sample_list))

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





for i in range(1,9+1):
    print (i)





# def read_int(msg):
#     n = None
#     while n is None:
#         try:
#             n = int(input(msg))
#         except ValueError:
#             print("You should enter only integer values!")
#     return n
# def odd_numbers (my_list):
#     total = 0
#     count = 0
#     for number in my_list:
#         if (number % 2 == 1):
#             total = total + number 
#         else:
#             count = count + 1
#     if (number == count):
#         return (0)
#     else:
#         return (total)

# #Main Program

# my_list = []
# n = read_int("Enter the maximum length of a list: ")

# while (len(my_list) < n):
#     item = read_int("Enter integer value to the list: ")
#     my_list.append(item)


# print ("This is your list: ", my_list)
# result = odd_numbers(my_list)
# print (result)

