num = int(input("Enter the limit: "))
a=0
b=1
print("Fibonacci series is :")
print(a)
print(b)

for i in range(2, num):  
    c = a + b
    print(c)
    a, b = b, c  
