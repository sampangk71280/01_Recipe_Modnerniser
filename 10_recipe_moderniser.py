# modules to be used...
import csv
import re

# Functions

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok !="yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Number checking function (number must be a float that is more than 0)
def num_check(question):

    error = "Please enter a number that is more than zero:"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response


        except ValueError:
            print(error)

def get_sf():
    serving_size = num_check("What is the recipe serving size?")

    # Main routine goes here
    dodgy_sf = "yes"
    while dodgy_sf == "yes":

        desired_size = num_check("How many servings are needed?")

        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small"
                             "and you might struggle to accurately weigh"
                             "the ingredients \n"
                             "Do you want to keep going (type 'no' to change"
                             "your desired serving size")
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This sclae facor is quite large - ytou might"
                             "have issues with mixing bowl space / oven space. \n"
                             "Do you want to keep going (tpye 'no to change"
                             "your desired serving size")
        else:
            dodgy_sf = "no"

        return scale_factor


# Main Routine

# set up Dictionaries

# set up list to hold 'modernised' ingredients

# ask user for recipe name and check its not blank
recipe_name = not_blank("Where is the recipe name? ",
                   "The recipe name can't be blank and can't contain numbers.",
                   "no")

# ask user where the recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank.",
                   "yes")

# get serving sizes and scale factor
scale_factor = get_sf()
print(scale_factor)
# Loop for each ingredient ...

# get ingredient amount
# get ingredient name
# get unit
# convert unit to ml
# convert from ml to g
# put updated ingredient in list

# output ingredient list