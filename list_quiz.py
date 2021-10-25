# **************** List creating from user-input************************
 
# lst = []
 
# # number of elements as input
# n = int(input("Enter number of elements : "))
 
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
 
#     lst.append(ele) # adding the element
     
# print(lst)



# ************Bubble Sort*******************

# def numsort(nums):
#     for i in range(0,len(nums)):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp

# nums=[1256, 0, 2, -3, 4, 10, 7, 8, 9]
# numsort(nums)
# print (nums)








# ................Bubble sort-EDX......................

# def _custom_bubble_sort_sample_(original_list):
#     # make a copy of the original list
#     my_list = original_list[:]
  
#     # get the length of the list
#     length = 0
#     for element in my_list:
#         length = length + 1
#     unSorted = True
#     while unSorted:
#         unSorted = False
#         for index in range(0, length-1):
#             # if next element is greater element then swap them
#             if my_list[index] > my_list[index + 1]:
#                 temporary_variable = my_list[index]
#                 my_list[index] = my_list[index + 1]
#                 my_list[index + 1] = temporary_variable
#                 unSorted = True
#     return my_list


# original_list = []
# n = int(input("Enter the length : "))
# for i in range(0, n):
#     ele = int(input("Enter the element : "))
#     original_list.append(ele) # adding the element
# print("You entered : ",original_list)
# print("The sorted list is : ",_custom_bubble_sort_sample_(original_list))







# ..................Excercise 4 ..................

# def merge_and_sort(list1,list2):
#     list1.extend(list2)
#     new_list=[]
#     while list1:
#         maximum=list1[0]
#         for element in list1:
#             if element > maximum:
#                 maximum = element
#         # append the smallest element to the new list
#         new_list.append(maximum)
#         # now remove that smallest element from the original list
#         list1.remove(maximum)
#     # Ultimately a will become empty
#     # and the loop will end
#     # now return the new list
#     return new_list
    

# list1=[]
# list2=[]
# a=int(input("Enter the length of LIST-1 : "))
# for i in range(0,a):
#     ele=int(input("Enter the element : "))
#     list1.append(ele)
# print ("LIST-1 is : ",list1)
# b=int(input("Enter the length of LIST-2 : "))
# for j in range(0,b):
#     ele=int(input("Enter the element : "))
#     list2.append(ele)
# print("LIST-2 is : ",list2)

# print(merge_and_sort(list1,list2))






# .................Exercise 5.................
# def _list_manipulation_sample3_(list1, a):
#     my_Count = 0
#     for element in list1:
#         if element == a:
#             my_Count = my_Count + 1
#     return my_Count

# list1=[]
# a=int(input("Enter the length of LIST-1 : "))
# for i in range(0,a):
#     ele=int(input("Enter the element : "))
#     list1.append(ele)
# print ("LIST-1 is : ",list1)

# print("Count of the repeated element is : ",_list_manipulation_sample3_(list1,a))





# ................Exercise 6......................

# def extracting_element(list1):
#     new_list=list1[1:-1]
#     return new_list
# list1=[]
# n=int(input("Enter the size of the list : "))
# for i in range(0,n):
#     ele=int(input("Enter the element : "))
#     list1.append(ele)
# print(list1)
# print(extracting_element(list1))




# .......................Exercise 7 (Modifying a List)....................
# def _list_manipulation_sample5_(my_list):
#     input_list = my_list[:]
#     for x in range(0, len(input_list)):
#         if input_list[x] % 2 != 0:
#             input_list[x] = input_list[x] + 1
#     return input_list

# list1=[]
# n=int(input("Enter the size of the list : "))
# for i in range(0,n):
#     ele=int(input("Enter the element : "))
#     list1.append(ele)
# print(list1)
# print(_list_manipulation_sample5_(list1))








# .......................Exercise 8 (Adding Odds from 2 Lists.............................

# def adding_odds_from_two_list(a,b):
#     total_sum = 0
#     a.extend(b)
#     for items in a:
#         if items % 2 != 0:
#             total_sum = total_sum + items
#     return total_sum

# list1=[]
# n=int(input("Enter the size of the list : "))
# for i in range(0,n):
#     ele=int(input())
#     list1.append(ele)
# list2=[]
# m=int(input("Enter the size of the list : "))
# for i in range(0,m):
#     ele=int(input())
#     list2.append(ele)
# print(list1)
# print(list2)
# print(adding_odds_from_two_list(list1,list2))








# .................Exercise 9 (Unique Elements)......................

# def _unique_list_sample_(sample_list):
#     output_list = []
#     for items in sample_list:
#         if items not in output_list:
#             output_list.append(items)
#     return output_list

# list1=[]
# n=int(input("Enter the size of the elements : "))
# for i in range(0,n):
#     ele=int(input())
#     list1.append(ele)
# print(list1)
# print(_unique_list_sample_(list1))








# ..........................Exercise 10 (Unique Elements From Multiple Lists).......................

# def _join_two_lists_unique_sample_(sample_list1, sample_list2):
#     output_list = []
#     for items1 in sample_list1:
#         if items1 not in output_list:
#             output_list.append(items1)

#     for items2 in sample_list2:
#         if items2 not in output_list:
#             output_list.append(items2)
#     return output_list

# list1=[]
# n=int(input("Enter the size of the elements : "))
# for i in range(0,n):
#     ele=int(input())
#     list1.append(ele)
# list2=[]
# n=int(input("Enter the size of the elements : "))
# for i in range(0,n):
#     ele=int(input())
#     list2.append(ele)
# print(list1)
# print(list2)
# print(_join_two_lists_unique_sample_(list1,list2))







# ................Exercise 11 (Traversing Backwards)...............

# def _reverse_of_a_list_sample_(old_list):
#     new_list = []
#     length = len(old_list)
#     i = -1
#     # Iterate the list using negative indices
#     while i >= -length:
#         new_list.append(old_list[i])
#         i = i - 1
#     return new_list
# input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
# print(_reverse_of_a_list_sample_(input_list))











# ..........................Exercise 12 (Numbers to Words)....................

n=int(input('please enter an integer between 1 and 9999: '))
one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)









