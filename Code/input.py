from datetime import datetime
name = input("Enter your name: ")
age = int(input("Enter you Age: "))
yr = ((datetime.now().year - age) + 100)
print(f"{name} will be 100 years old in year {yr}")
no = int(input("How many time to see above message: "))
while no>0:
  print(f"{name} will be 100 years old in year {yr}")
  no-=1