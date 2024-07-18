# logical operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("{a} is greatest".format(a=a))
elif b > c:
    print("{b} is greatest".format(b=b))
else:
    print("{c} is greatest".format(c=c))

if a > b or a > c:
    print("{a} is might be greatest".format(a=a))
elif b > c:
    print("{b} is greater".format(b=b))
else:
    print("{c} is greater".format(c=c))

print("not True is", not True)
print("not False is", not False)

print("\nYash Gupta\t23BCS11317")
