#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
words =  ['apple', 'banana', 'cherry', 'mango', 'oranges', 'berries', 'fig', 'grape', 'honeydew']


# Use list comprehension to create a new list of words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list of words
print("Words with an odd number of characters:", odd_length_words)