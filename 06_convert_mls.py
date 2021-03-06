# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is

# Functions
def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T" "tbsp"]
    ounce = ["oz", "fluid-ounce", "fl-oz", "ounce"]
    cup = ["cup", "c"]
    pint = ["pint", "p", "pt", "fl-pt"]
    quart = ["q", "qt", "fl-qt"]
    ml = ["milliliter", "millitre", "cc", "mL"]
    l = ["litre", "liter", "L"]
    dl = ["deciliter", "decilire", "dL"]
    pound = ["lb", "#"]

    if unit_tocheck == "":
        print("You chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck == "mL" or unit_tocheck.lower in ml:
        return "ml"
    elif unit_tocheck == "L" or unit_tocheck.lower() in l:
        return "l"
    elif unit_tocheck == "dL" or unit_tocheck.lower() in dl:
        return "dl"
    elif unit_tocheck.lower() in pound:
        return "pound"


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
while keep_going  == "":
    amount = eval(input("How much?"))
    amount = float(amount)

    # Get unit and change it to match dictionary
    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q")