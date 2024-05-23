# Plate Stacking
# Add a plate: add a plate to the top of the stack (Larger plate cannot be stacked on top of a smaller plate)
# Print plates: display the stack of plates in the terminal
# Remove plates: remove 1-to-n plates from the top of the stack

# List to track plates
plates = []

# Add Plate
def add_plate(n):
    # if plate size is less than or equal to zero, don't add plate
    if n <= 0:
        print("Cannot place a plate of size 0 or smaller.")
        return
    # 'not plates' checks if stack is empty -> if no plates on stack, add it
    # size of new plate -> n must be less than or equal to the size of the previous plate
    if not plates or n <= plates[-1]:
        plates.append(n)
        print("Success!")
    else:
        print(f"Cannot place a plate of size {n} on top of another plate of size {plates[-1]}.")

# Print Plates
def print_plates():
    # print message for no plates in stack
    if not plates:
        print("There are no stacked plates.")
    # print plates using [::-1] to reverse the list so the largest
    # plate is at the bottom and the smallest plate is at the top
    else:
        for i in plates[::-1]:
            print(i)

# Remove Plates
def remove_plates(n):
    # if value is less than or equal to zero, reject operation and print warning message
    if n <= 0:
        print(f"Cannot remove {n} plates. Number of plates to remove must be a positive integer.")
        return
    # value should not exceed stack size
    if n > len(plates):
        print(f"Cannot remove more than {len(plates)} plates. You chose {n}.")
        return
    # remove plates from stack
    for i in range(n):
        plates.pop()
    print("Success!")

def run():
    print("Plate Stacking \n")
    option = ""
    while option != "0":
        print("Menu")
        print("================")
        print("0. [Exit]")
        print("1. Add a plate")
        print("2. Print plates")
        print("3. Remove plates")
        option = input("Select [0-3]: ")
        print("")
        if option == "0":
            print("Goodbye!")
            print("")
        elif option == "1":
            print("Add a plate")
            print("================")
            try:
                add_plate_prompt = input("Enter a plate size: ")
                plate_size = int(add_plate_prompt)
                add_plate(plate_size)
                print("")
            except ValueError:
                print("Error. Please enter a positive integer.")
                print("")
        elif option == "2":
            print("Print plates")
            print("================")
            print_plates()
            print("")
        elif option == "3":
            print("Remove plates")
            print("================")
            if not plates:
                print("There are no stacked plates.")
                print("")
            else:
                try:
                    remove_plate_prompt = input("How many plates to remove?: ")
                    num_plates = int(remove_plate_prompt)
                    remove_plates(num_plates)
                    print("")
                except ValueError:
                    print("Error. Please enter a positive integer.")
                    print("")
        else:
            print("I don't understand that command.")
            print("")


if __name__ == "__main__":
    run()
