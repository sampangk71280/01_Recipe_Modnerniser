import csv

# open file
groceries = open('01_ingredients_ml_to_g.csv')

# read data into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary = {}

# add the data from the list into dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)


unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}


keep_going = ""
while keep_going == "":
    amount = eval(input("How much?"))
    amount = float(amount)

    # Get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ")

    if ingredient in food_dictionary:
        mult_by = food_dictionary.get(ingredient)
        amount = amount * float(mult_by) / 250
        print ("Amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))
