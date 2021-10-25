# celsius=int(input("Please input a temperature in celsius : "))
# fahrenheit=(celsius*9)/5+32
# print("The temperature is ",fahrenheit," degree fahreheit.")
# if fahrenheit<30:
# 	print("It is freezing")
# elif fahrenheit<50:
# 	print("It is chilly")
# elif fahrenheit<90:
# 	print("It is ok")
# else:
#     print("It is hot")


# my_list=[ 2.3, 'car', 12, 46, 'cat']
# if 12 in my_list:
#     print('hello')
# elif 6 > 4:
#     print('bye')
# else:
#     print('nothing')




# if 6/2:
#     print('three')
# elif 5 :
#     print('five')
# else:
#     print('zero')





# if False:
#     print('false')
# elif 2**3 == 8 :
#     print('true')
# else:
#     print('none')








# my_string="hello"
# if 10 % 5:
#     print('true')
# elif "le" not in my_string :
#     print('false')
# else:
#     print('none')




# if 6 <5:
#     print('one')
# elif 7 == 9 :
#     print('two')
# print("three")





# x = 0
# if 5 in [1, 2, 3, 4]:
#     x = x + 1
# elif 4 == 2:
#     x = x + 2
# elif 7 > 4:
#     x = x + 3
# else:
#     x = x + 4
# print (x)





# x = 5
# if 8 % 4:
#     x = x - 1
# elif 3 < 4 / 2:
#     x = x - 2
# elif "t":
#     x = x - 3
# else:
#     x = x - 4
# print (x)




# x = 12
# if "x" in "meow" and 4 > 2+1 :
#     x = x / 2
# elif 6 % 2 != 0 :
#     x = x / 3
# elif 2 in ["cat" , "dog" ]:
#     x = x / 4
# else:
#     x = x + 1
# print (x)



# x = 100
# if x > 10 :
#     x = x + 10
# if x > 20 :
#     x = x + 50
# print(x)


# x = 100
# if x > 10 :
#     x = x + 10
# elif x > 20 :
#     x = x + 50
# else:
#     x = x + 70
# print(x)  






# user_response=input("Type anything:")
# if 'dog' in user_response:
#     print ('Dog')
# elif 'cat' in user_response:
#     print ('Cat')
# else:
#     print ('None')




# number=int(input("Enter a number : "))
# if number==2:
#     print("two")
# elif number==3:
#     print("three")
# elif number==5:
#     print("five")
# else:
#     print("other")




# age=int(input("Enter age in years : "))
# if age<=0:
#     print("UNBORN")
# elif age<=150:
#     print("ALIVE")
# else:
#     print("VAMPIRE")





# n=int(input("Enter a positive number : "))
# if (n%2)==0 and (n%3)==0:
#     print("BOTH")
# elif (n%2)==0 or (n%3)==0:
#     print("ONE")
# else:
#     print("NEITHER")




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

# 4272 days 5 hours 45 minutes 17 seconds


time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("%d " "days" " %d " "hours" " %d " "minutes" " %d " "seconds" % (day,hour,minutes,seconds))