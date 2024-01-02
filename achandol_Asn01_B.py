'''
CS1026a 2023
Assignment 01 Project 01 - Part B
Krish Chandola
251371956
October 4th 2023
'''

print("Part One - Project B: Prime Choice")

# Enter a range so all prime numbers within that range are displayed
start = int(input("Prime numbers starting with: "))
end = int(input("and ending with: "))
# line space
print("")

# in case starting number is bigger than the ending number
if start > end:
    print(f"Incorrect Input: {start} is greater than {end} numbers have automatically been switched"f"")
    print("")
    # switch variables by using temporary variables
    temp = start
    start = end
    end = temp

# Create a variable for the numbers in the range
for nums in range(start, end + 1):
    # All numbers are prime until a test is done
    Prime = True

    # all numbers that are equal or lower than 1 cannot be prime numbers
    if nums <= 1:
        Prime = False
    else:
        # Start a for loop from 2 to the end of range
        for Divider in range(2,nums):
             # Test the numbers in the range to check if they divisible by any number apart from 1 or themselves
             if nums % Divider == 0:
                 # If they are remove them from the list and
                 Prime = False
                 # Break the loop once a divisor has been found
                 break

    if Prime:
        print(f"{nums} is prime")

print("END: Project One <01> - Part B")
print("Krish Chandola    Achandol    251371956")