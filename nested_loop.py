# pgm to find if 24 a prime number or not

# current_number=24
# current_divisor=2
# is_current_number_prime=True

# while(current_divisor<current_number):
#     if current_number%current_divisor==0:
#         is_current_number_prime=False
#         break

#     current_divisor=current_divisor+1

# if is_current_number_prime:
#     print(current_number,"is Prime")
# else:
#     print(current_number,"is not Prime")
# print("All done")








#A pgm to print all the prime numbers between 2 and 5

start_number=2
end_number=100
current_number=start_number
while current_number<=end_number:
    current_divisor=2
    is_current_number_prime=True
    while(current_divisor<current_number):
        if current_number%current_divisor==0:
            is_current_number_prime=False
            break
        current_divisor=current_divisor+1
    if is_current_number_prime:
        print(current_number,"is Prime")
    current_number=current_number+1
print("All done")
