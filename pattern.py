# for i  in range(4):
#     for j in range(4):
#         print("*",end='')
#     print()


# for i in range(4):
#     for j in range(i+1):
#         print("*",end='')
#     print()




n=int(input("Enter the number : "))
m=n-1
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(m):
    for j in range(m-i):
        print("*",end='')
    print()

