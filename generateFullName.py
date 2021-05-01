# to run
# python3 generateFullName.py
# then input firstname then lastname



def checkIfNumber(firstName,lastName):
    validInput = True
    validStrings = True
    try: 
        # case where the input is a number
        if (int(firstName) or int(lastName)):
            validInput = False
            print("no integers in first or last name")
    except ValueError:
        if (firstName == "" or lastName == ""):
            print("missing firstname or lastname")
            validStrings = False

    return validInput and validStrings

def main():
    firstName = input("Enter firstname: ")
    lastName = input("Enter lastname: ")
    userInputChecker = checkIfNumber(firstName,lastName)

    if (userInputChecker):
        print("Your full name is: {0} {1} ".format(firstName,lastName))


if __name__ == "__main__":
    main()
