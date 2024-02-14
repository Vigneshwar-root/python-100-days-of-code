programming_dictionary = {"Bug": "An error in a program that preveents the program from running as expected.", 
"Function":"A piece of code that you can easily call over and over again"}

#retreiving items from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#loop through a dictionary
for thing in programming_dictionary:
    print(f"key: {thing} value: {programming_dictionary[thing]}")
