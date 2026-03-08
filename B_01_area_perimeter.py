# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Please enter a number that is greater than 0")


# Main Routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter key to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")