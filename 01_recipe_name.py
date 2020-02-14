# Gets recipe name and checks it is not blank

# Not Blank Function goes here
def not_blank(question):
    error = "Your reciple name has numbers in it."
    has_errors = ""

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response




# Main routine goes here

recipe_name = not_blank("What is the recipe name?")
print("You are making {}".format(recipe_name))




