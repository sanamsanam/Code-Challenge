a = [1, 7, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

for x in a:
    if (x < 5):
        new.append(x)

print(new)
# filter return those element which return true in lambda function other function are reduce and map
#print(list(filter(lambda x: (x < 5) , a)))

#no = int(input("enter a no: "))
#print(list(filter(lambda y: (y<no) , a)))
#print(sorted(list(filter(lambda y: (y<no) , a))))
