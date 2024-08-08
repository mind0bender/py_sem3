n = int(input("number:"))
s = 0

if n < 0:
    print("negative")
else:
    for i in range(1, n):
        if n % i == 0:
            print(i)
            s = s + i

    if s == n:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")
