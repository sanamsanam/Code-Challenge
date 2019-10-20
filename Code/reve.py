ask = str(input("Please give a string: "))   # sanas
ask2 = ""
# 1 answer
for items in ask:
    ask2 = items + ask2
if ask == ask2:
    print(" This string is palindrome")
else:
    print("this string is not palindrome")

# 2 answer     ask2 = ''.join(reversed(ask))
# 3 answer     ask2=ask[::-1]
