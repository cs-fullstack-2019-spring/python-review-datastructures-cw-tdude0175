def main():
    # problem1()
    problem2()

# Create a function that has a loop that quits with q
# Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names
# ADDITIONAL REQUIREMENTS:
#
# Your code should be able to process the quit command (q) the User enters regardless of case

# wow
#how to add flourish? make code more readable?

def problem1():
    theDeepList =[]
    userInput = input("we need to go deeper.")
    while(userInput.lower() != "q"):
        theDeepList.append("\n"+userInput)
        userInput = input("I need a name of the best of the best!")

    for name in theDeepList:
        print(name)


# Given the following List of Dictionaries:
#
#     myDictionaryList = [
#         {
#             "name": "Kelvin",
#             "age": 30
#         },
#         {
#             "name": "Bob",
#             "age": 50
#         },
#         {
#             "name": "Alex",
#             "age": 21
#         }
#     ]
# Create a function that does the following when called:
#
# Prints a formatted list of names and ages
# ex.
#
# Name: Kelvin
# Age: 30
#
# Name: Bob
# Age: 50
#
# Name: Alex
# Age: 21
# Prompts the User for which property they want to use to sort the list (e.g. AGE or NAME).
# Print the formatted list of names and ages sorted by the specified sort criteria.
#
# Continue prompting the User for the sort criteria and print a sorted list until the User enters q then exit.
#
# ADDITIONAL REQUIREMENTS:
#
# Your code should be able to process the sort criteria the User enters regardless of case
# Your code should be able to process the quit command (q) the User enters regardless of case
# If the User enters something other than q or a valid sort criteria (e.g. AGE or NAME)
# your code should display INVALID ENTRY. PLEASE TRY AGAIN and continue the process.

# .sort works like maps BUT IT WON'T LET YOU ADD A FUNCTION INTO IT
# you MUST USE [key=] TO TELL IT WHAT FUNCTION TO USE


def problem2():
    def sortbyage(thisisdictionary):
        return(thisisdictionary["Age"])

    def sortbyname(whatIsThis): # {whatIsThis} is the object,element returning the ["Name"] tells it to sort by THAT VALUE
        return whatIsThis["Name"]
    listofpeople =[
        {"Name":"Kelvin","Age": 30},   #0
        {"Name":"Alex","Age":50},       #1
        {"Name":"Bob","Age":21},      #2
                 ]

    userinput = input("how do you want to sort the list of people? age / name")
    while(userinput.lower() != "q"):
        if(userinput.lower() == "age"):
                listofpeople.sort(key=sortbyage)

        elif(userinput.lower() == "name"):
            listofpeople.sort(key= sortbyname)   # DO NOT LET CALLING THE FUNCTION ADD PARENTHSIS! IT WON'T WORK

        else:
            print("INVALID, PLEASE TRY AGAIN")
        for dictionary in listofpeople:
            print(f"{dictionary['Name']} {dictionary['Age']} \n ")
        userinput = input("How to sort? age / name / q to quit")





if __name__ == '__main__':
    main()