# Q) Find whether target exists in the list and return it's index value.
"""
numbers = [7, 2, 9, 4, 9, 1]
target = 9
found = False
index = 0
for i in numbers:
    if i == target:
        found = True
        break
    index += 1

if found:
    print("Target found at", index)
else:
    print("Target not found")
"""
#TC = O(n)
#SC = O(1)

# Q) Find how many times target appears in the list.
"""numbers = [2, 5, 2, 7, 2, 9, 5]
target = 2
count = 0
for i in numbers:
    if i == target:
        count += 1
print("Total occurrence of", target, "in the array is", count)"""
#TC = O(n)
#SC = O(1)

# Q) Find duplicates
"""numbers = [2, 5, 2, 7, 2, 9, 5]
first = numbers[0]
duplicates = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])
print(duplicates)"""
#TC = O(n³)
#SC = O(n)