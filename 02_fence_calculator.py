# functions go here

# checks input is more than zero
def num_check(question):
    while True:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# main routine goes here

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost_per_m = num_check("Price per meter: $")

    # calculate perimeter (width + height x2)
    perimeter = 2 * (width + height)

    # calculate the cost of the fencing
    final_cost = (perimeter * cost_per_m)

    # output area and perimeter
    print("Perimeter: {} units".format(perimeter))
    print("The cost of the fencing is: ${}".format(final_cost))
    print()
    keep_going = input("Press <enter> to keep going or press any key to quit.")
    print()
    print("-" * 30)

print()
print("Thanks for using this Fencing Cost Calculator")
