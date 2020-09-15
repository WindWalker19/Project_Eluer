# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
a = 0

for i in range (1,1000):
    if((i%3 == 0) or (i%5 == 0)):
        a +=i

print(a)


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def pro1(num,num1,num2):
    # place to hold the value
    result = 0
    d = 0
    while (d < num):
        # condition for division.
        if ((d % num1 == 0) or (d % num2 == 0)):
            result += d
            d +=1
        else:
            d +=1

    return result

#number range.
a = int(input("Enter the number range you want."))
# multiples.
b = int(input("Enter the number you want to get multiples of."))
c = int(input("Enter the other number you want to get multiples of."))

print(pro1(a,b,c))
