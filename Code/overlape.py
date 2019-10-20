a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = list(set(a) & set(b)) 
print (new)

a = [1, 1, 2,2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4,5,5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new =[]
for items in b:
  if items in a and items not in new:
    new.append(items)
print(new)