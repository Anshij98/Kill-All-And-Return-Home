This code simulates the movement of a specialized castle on a chessboard, providing predefined unique paths for the castle to follow. Here is a step-by-step explanation of each part of the code:

parse_input()
This function collects user input to define the initial setup of the chessboard.

Input Number of Soldiers: Prompts the user to enter the number of soldiers.
Soldier Coordinates: Collects the coordinates for each soldier from the user and stores them in a list.

Grid Initialization: Initializes an empty dictionary.
Populate Grid: Fills the dictionary with soldier coordinates and their identifiers.
Return: Returns the grid dictionary.
find_unique_paths(special_castle)
This function defines three unique paths that the special castle can follow. These paths are hard-coded and represent different possible movements and actions of the castle.

Path Definitions: Each path is a list of strings describing the steps the castle takes, including killing soldiers, turning left, jumping, and arriving at the destination.
Return: Returns a list of paths.
main()
This function orchestrates the flow of the program.

Parse Input: Calls parse_input() to get the initial setup from the user.
Initialize Grid: Calls initialize_grid(soldiers) to create the grid with soldier positions.
Find Unique Paths: Calls find_unique_paths(special_castle) to get the predefined paths for the castle.
Print Results: Outputs the number of unique paths and details of each path to the user.

OUTPUT-
![Screenshot 2024-08-01 at 1 12 52 PM](https://github.com/user-attachments/assets/9bb5fda1-cd65-4500-b908-4dba17efb9b8)

![Screenshot 2024-08-01 at 1 12 45 PM](https://github.com/user-attachments/assets/81c28cd5-2ab6-4184-a975-1d5be52627e2)


The code provided does not use any external libraries. It utilizes only built-in Python functionalities. Here's a breakdown of what is used:

Built-in Python Functionalities:

Input and Output:
Basic Data Structures:
String and List Manipulations:

