from time import sleep

n: int = int(input("Enter number: "))
s: int = 0

if n < 0:
    print("Invalid input")
    exit()

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

sleep(1000)
