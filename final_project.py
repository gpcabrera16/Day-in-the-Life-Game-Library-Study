from draft_program import (
   choose_action,
   work_on_assignment,
   take_break,
   get_coffee,
   random_distraction,
)

def get_assignment_count():
    """
    Ask the player how many assignments they have and only accept whole numbers between 1 and 5.

    Output:
    int: Valid number of assignments
    """
    while True:
        answer = input("How many assignments are in your planner today? ")

        try:
            total_assignments = int(answer)

            if 1 <= total_assignments <=5:
                return total_assignments
            else:
                print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a whole number.")

def get_assignments(total_assignments):
    """
    Ask the player to name each of their assignments.

    Input:
    total_assignments (int): Number of assignments

    Output:
    list: Names of the player's assignments
    """
    assignments = []

    for i in range(total_assignments):
        while True:
            name = input(f"Enter assignment {i + 1}: ").strip()

            if name:
                assignments.append(name)
                break
            else:
                print("Assignment name cannot be blank.")
    return assignments

def select_assignment(assignments):
    """
    Have the player choose an assignment from their list.

    Input:
    assignments (list): Remaining assignments

    Output:
    int: Index of the assignment that's selected
    """
    print("\nYour remaining assignments:")

    for i, assignment in enumerate(assignments):
        print(f"{i+1}. {assignment}")

    while True:
        choice = input("Which assignment would you like to work on? ")

        try:
            choice = int(choice)

            if 1<= choice <= len(assignments):
                return choice -1
            else:
                print("Please select an assignment from the list.")
        except ValueError:
            print("Please enter a whole number.")

def check_assignments_complete(assignments):
    """
    Check whether the player has finished all of their assignments.

    Input:
    assignments (list): Remaining assignments

    Output:
    bool: True if no assignments remain, else False
    """
    return len(assignments) == 0

def check_game_result(assignments):
    """
    Determine if player has won or lost.

    Input:
    assignments (list): Remaining assignments

    Output:
    bool: True if player won, else False
    """
    return check_assignments_complete(assignments)


def main():
    """
    Runs the final version of the library studying game.
    """
    total_assignments = get_assignment_count()

    assignments = get_assignments(total_assignments)
    hours_remaining = total_assignments + 3
    energy = 5
    coffee_available = True
    print("\nHere are your assignments for today:")
    for assignment in assignments:
        print("-", assignment)

    while hours_remaining > 0 and len(assignments) > 0:

        print("\nHours remaining:",hours_remaining)
        print("Energy level:", energy)
        print("Assignments remaining:", len(assignments))

        action = choose_action()

        if action == "1":
            print("Working on an assignment requires 2 energy.")
            selected_index = select_assignment(assignments)

            energy, hours_remaining, completed = work_on_assignment(energy, hours_remaining)

            if completed:
                completed_assignment = assignments.pop(selected_index)
                print(f"You completed {completed_assignment}")
                print("Energy after working:", energy)

                energy = random_distraction(energy)
                print("Energy after random event:", energy)

        elif action == "2":
            energy, hours_remaining = take_break(energy, hours_remaining)

        elif action == "3":
            if coffee_available:
                energy, coffee_available, hours_remaining = get_coffee(
                    energy, coffee_available, hours_remaining
            )
            else:
                print("You already had your coffee today!")
                print("You waste an hour trying to get another coffee.")
                hours_remaining -=1

        else:
            print("Invalid choice, please choose 1, 2, or 3!")
            print("You wasted an hour deciding on what to do.")
            hours_remaining -= 1


    print("\nYour remaining assignments:")
    for assignment in assignments:
        print("-", assignment)

    if check_game_result(assignments):
        print("\nCongratulations! You completed all your assignments.")
        print("You win!")
    else:
        print("\nYou ran out of time!")
        print(f"You still have {len(assignments)} assignments remaining")
        print("You lost the game!")

if __name__ == "__main__":
    main()