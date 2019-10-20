no = int(input("enter a no: "))
if (no%4) == 0:
  print("This no is even and divisable by 4: ")
elif (no%2) == 0:
  print("this no is even")
else:
  print("this no is odd")

num = int(input("enter a no: "))
check = int(input("enter a no: "))
if (num%check) == 0:
  print(f"{num} is divisible by {check}")
else:
  print(f"{num} is not divisible by {check}")