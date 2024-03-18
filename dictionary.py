#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

person = {
        "name" : "Fatma", 
          "age" : "25", 
          "fav_color" : "pink"
          }
print(person)

print("Name:  ", person["name"])
print("Age:   ", person["age"])
print("Favorite color: ", person["fav_color"])

#add more info to the dictionary
person["height"]="160cm"
person["city"]="Istanbul"
print(person)

#remove a key value  pair from the dictionary
del person["age"]
print(person)