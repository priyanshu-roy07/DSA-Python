# Find the smallest number without using min()
"""numbers = [7, 2, 9, 4, 1]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)"""

#Find the second-largest number.
#numbers = [10, 7, 8, 9, 4, 1]
#numbers = [7, 10, 8, 9, 4, 1]
#numbers = [7, 8, 9, 4, 1]
numbers = [10, 10, 8, 7, 6]
#numbers = [10, 8, 8, 7, 6]
#numbers = [1,2,3,4,5,6]
#numbers = [55, 66, 77, 88, 99]
largest = None
second_largest = None
"""if second_largest > largest:
    largest = numbers[1]
    second_largest = numbers[0]
elif second_largest == largest:
    second_largest = numbers[2]"""
for i in numbers:
    if largest == None:
        largest = i
    elif i > largest:
        second_largest = largest
        largest = i
    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i
print("largest = ",largest)
print("second_largest =", second_largest)