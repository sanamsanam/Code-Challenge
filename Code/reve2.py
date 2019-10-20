# 4 answer
ask = str(input("Please give a string: "))   # sanas
ask2 = ""
a = len(ask)
for i in range(a-1, -1, -1):
    ask2 = ask2+ask[i]
print(ask2)
if ask == ask2:
    print(" This string is palindrome")
else:
    print("this string is not palindrome")
