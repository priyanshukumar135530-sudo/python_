#write a program for print the fibonacci series
#Write a program for print sum of n natural numbers
a = 0
b = 1
n=int(input("Enter the number of terms : "))
print(a,b)
for i in range(3,n):
    c = a+b
    print(c)
    a = b
    b = c

