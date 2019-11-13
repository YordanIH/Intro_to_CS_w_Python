
#passing the length of list as a variable for range
values = [4, 10, 3, 8, -6]
print(len(values))
print(list(range(5)))
print(list(range(len(values))))

#using a loop to go through indexcies
for i in range(len(values)):
    print(i)
    print(i, values[i])

#modifying lists
for i in range(len(values)):
    values[i] = values[i] * 2

print(values)