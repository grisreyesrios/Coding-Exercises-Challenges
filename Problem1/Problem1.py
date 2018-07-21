# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10,15,3,7] and k = 17, return since 10+7 is 17.
# It considers for the list a maximum of 4 numbers and introduce by the user.


# Define the function
def addtwo(listnumber, k):
    for a in range(len(listnumber)):
        for b in range(len(listnumber)):
            if a != b and listnumber[a] + listnumber[b] == k:
                return listnumber[a], listnumber[b]
    return False


lstnum = []  # Creation of a list
x = 0
while len(lstnum) < 4:  # Loop to introduce the numbers by the user and add it to the list.
    try:
        number = int(input("Please enter a number:"))   # Start the exception to avoid a traceback.
        lstnum.append(number)
    except ValueError:
        print("Invalid input, please introduce only integers")

    if x == 4:           # Stop the loop
        break

print("Your list of numbers is:")
lstnum.sort()  # Sorting the list
print(lstnum)  # Print sorted list
k1 = int(input("Enter a number for the k value:"))
screen = addtwo(lstnum, k1)   # Calling the function
print("The two numbers from the list that add up k are:", screen)  # Print final result
