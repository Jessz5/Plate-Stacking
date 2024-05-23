# Plate Stacking

## Description

This is a simple Python application that simulates stacking plates. The application allows users to add plates to a stack, print the current stack of plates, and remove plates from the stack. The size of each plate is represented by a positive integer, and a larger plate cannot be placed on top of a smaller plate.

## Features

- **Add a Plate**: Add a plate to the top of the stack. The size of the plate must be a positive integer and less than or equal to the size of the plate below it.
- **Print Plates**: Display the current stack of plates in the terminal. Plates are shown with the largest plate on the bottom and the smallest plate on the top.
- **Remove Plates**: Remove a specified number of plates from the top of the stack. The number of plates to remove must be a positive integer and cannot exceed the number of plates currently in the stack.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Jessz5/Plate-Stacking.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Plate-Stacking
    ```

## Usage

1. Run the application:
    ```sh
    python plate_stacking.py
    ```

2. Follow the on-screen prompts to add, print, or remove plates from the stack.

## How It Works

- **Adding Plates**: The user is prompted to enter the size of the plate to add. The application validates the plate size to ensure it is a positive integer and that it is less than or equal to the size of the plate below it.
- **Printing Plates**: The application prints the current stack of plates in reverse order, so the largest plate appears at the bottom and the smallest plate at the top. If there are no plates in the stack, it displays a message indicating that.
- **Removing Plates**: The user is prompted to enter the number of plates to remove. The application validates the number to ensure it is a positive integer and does not exceed the number of plates currently in the stack.

## Example

```sh
Plate Stacking 

Menu
================
0. [Exit]
1. Add a plate
2. Print plates
3. Remove plates
Select [0-3]: 1

Add a plate
================
Enter a plate size: 5
Success!

Menu
================
0. [Exit]
1. Add a plate
2. Print plates
3. Remove plates
Select [0-3]: 2

Print plates
================
5

Menu
================
0. [Exit]
1. Add a plate
2. Print plates
3. Remove plates
Select [0-3]: 3

Remove plates
================
How many plates to remove?: 1
Success!

