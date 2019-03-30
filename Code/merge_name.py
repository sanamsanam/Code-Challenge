def unique_names(names1, names2):
    unique = list(set(names1) | set(names2)) 
    
    return unique


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia