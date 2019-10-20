num = int(input("enter a no: "))
divisor = list(filter(lambda x: num % x == 0, range(1, num+1)))
print(divisor)

num = int(input("enter a no: "))
new = []
for items in range(1, num+1):
    if num % items == 0:
        new.append(items)
print(new)
