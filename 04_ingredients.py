# Ingredients List


# Not blank function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok  != "yes":
            # look at each character in string and if it's a number
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                break

        if response == "":
            print(error)
        elif has_errors != "":
            print(error)
        else:
            return response


# Main Routine...

# Set up empty ingredient list
ingredients = []
# Loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":
    # Ask user for ingredient (via not blank function)
    get_ingredient = not_blank("Please type in an ingredient name:",
                               "This can't be blank",
                               "yes")

    # Stop looping if exit code is type and there are more
    # than 2 ingredients...
    if get_ingredient.lower() == "xxx" and len(ingredients) > 1:
        break
    elif get_ingredient.lower() == "xxx" and len(ingredients) <2:
        print("You need a lot two ingredient in the list."
              "Please add more ingredients.")

    # If exit code is not entered, add ingredient to list
    else:
        ingredients.append(get_ingredient)

# Output list
print(ingredients)