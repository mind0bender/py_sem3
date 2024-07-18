# logical operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("{a} is greater".format(a=a))
elif b > c:
    print("{b} is greater".format(b=b))
else:
    print("{c} is greater".format(c=c))

print("\nYash Gupta\t23BCS11317")
