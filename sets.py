#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
print("Enter the elements for the first set(separated by spaces): ")
set1_input = input().split()
set1 = set(map(int, set1_input))

# Get user input for the second set of integers
print("Enter the elements of the second set (separated by spaces):")
set2_input = input().split()
set2 = set(map(int, set2_input))

# Print the two sets
print("Set 1:", set1)
print("Set 2:", set2)

# Find the intersection of the two sets
intersection = set1 & set2
print("Intersection of Set 1 and Set 2:", intersection)

# Find the union of the two sets
union = set1 | set2
print("Union of Set 1 and Set 2:", union)

# Find the difference between the two sets
difference = set1 - set2
print("Difference between Set 1 and Set 2:", difference)