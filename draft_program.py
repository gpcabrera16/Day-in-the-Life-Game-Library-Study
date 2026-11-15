import random

# Basic game play loop: Arrive at library, choose action 
# Based on action, energy level and hours remaining varies
# random event occurs, energy level and hours remaining changes
# complete or don't complete work, time decreases, repeat, check planner, 
# win/lose.

# CONSTANTS
LIBRARY_HOURS_PER_DAY = 5
MAX_ENERGY_LEVEL = 5

def choose_action():
    """
    Ask the player what they would like to do.

    Inputs:
    None

    Outputs:
    Selected by the player
    """
    print("What would you like to do?")
    print("1. Work on assignment")
    print("2. Take a break")
    print("3. Get coffee")

    action = input("Choose 1, 2, or 3: ")
    return action


def choose_assignment():
    """
    Ask the player which assignment they plan to work on.

    Inputs:
    None
    
    Outputs:
    Assignment choice of the player.
    """
    assignment = input("Which assignment would you like to work on? ")
    return assignment

def work_on_assignment(energy_level, hours_remaining):
    """
    Determine whether the player has enough time and energy to complete an assignment.

    Inputs:
    energy_level: Current energy level of the player
    hours_remaining: Remaining time in library for player

    Outputs:
    Updated energy level, updated hours remaining, and whether the assignment was completed.
    """
    if energy_level >= 2 and hours_remaining >= 1:
        energy_level = energy_level - 2
        hours_remaining = hours_remaining -1
        return energy_level, hours_remaining, True

    else:
        print("You do not have enough energy to work right now.")
        hours_remaining = hours_remaining - 1
        return energy_level, hours_remaining, False

def take_break(energy_level, hours_remaining):
    """
    Have player take break to restore energy level.

    Inputs:
    energy_level: Current energy level of the player
    hours_remaining: Remaining time in library for player

    Outputs: 
    Updated energy level and hours remaining
    """
    hours_remaining = hours_remaining - 1
    energy_level = energy_level + 2

    if energy_level > MAX_ENERGY_LEVEL:
        energy_level = MAX_ENERGY_LEVEL

    print("You took a break and now have more energy.")
    return energy_level, hours_remaining

def get_coffee(energy_level, coffee_available, hours_remaining):
    """
    The player has the option to get coffee once during the game.

    Inputs:
    energy_level: Current energy level of the player
    coffee_available: Indicate if there is coffe left

    Outputs:
    Updated energy level and coffee availability
    """
    if coffee_available:
        coffee_boost = random.choice([1,2])
        energy_level = energy_level + coffee_boost
        hours_remaining = hours_remaining - 1

        if energy_level > MAX_ENERGY_LEVEL:
            energy_level = MAX_ENERGY_LEVEL

        coffee_available = False
        print("Your coffee gave you", coffee_boost, "extra energy.")
    else:
        print("You already had a coffee today.")

    return energy_level, coffee_available, hours_remaining 

def random_distraction(energy_level):
    """
    Generate a random event that may impact the energy of the player.

    Inputs:
    energy_level: Current energy level of the player

    Outputs:
    updated energy level
    """
    event = random.choice(["friend","study_room", "extra_coffee", "nothing"])

    if event == "friend":
        print("A friend stops to talk to you. You lose 1 energy.")
        energy_level = energy_level - 1

    elif event == "study_room":
        print("You find a quiet study room. You gain 1 energy.")
        energy_level = energy_level + 1 

    elif event == "extra_coffee":
        print("Surprise! You got a coupon for extra coffee. You gain 2 energy.")
        energy_level = energy_level + 2

    else:
        print("Nothing distracting happens.")

    if energy_level < 0:
        energy_level = 0

    if energy_level > MAX_ENERGY_LEVEL:
        energy_level = MAX_ENERGY_LEVEL

    return energy_level
    

def check_win(assignments_completed, total_assignments):
    """
    Determine whether the player completed all of their assignments.

    Inputs:
    assignments_completed: number of assignments finished
    total_assignments: number of assignments in planner

    Outputs:
    True if all assignments are completed, False if not. 
    """
    if assignments_completed == total_assignments:
        return True
    else:
        return False


# Ask the player to input their name
# Ask how many assignments player has

def main():
    name = input("What is your name? ")

    total_assignments = int(input("How many assignments are in your planner today? "))
    
    assignments_completed = 0
    hours_remaining = LIBRARY_HOURS_PER_DAY
    energy_level = MAX_ENERGY_LEVEL
    coffee_available = True

    print()
    print("Welcome to the the library", name + ", enjoy your studying!")
    print("You have", hours_remaining, "hours to finish your assignments.")

    while hours_remaining > 0 and assignments_completed < total_assignments:

        print()
        print("Hours remaining:", hours_remaining)
        print("Energy level:", energy_level)
        print("Assignments completed:", assignments_completed)
        print("Assignments remaining:", total_assignments - assignments_completed)

        action = choose_action()

        if action == "1":
            assignment = choose_assignment()

            energy_level, hours_remaining, completed = work_on_assignment(energy_level,hours_remaining)

            if completed:
                print("You completed", assignment + "!")
                assignments_completed = assignments_completed + 1

                energy_level = random_distraction(energy_level)

        elif action == "2":
                energy_level, hours_remaining = take_break (energy_level,hours_remaining)  

        elif action == "3":
                energy_level, coffee_available, hours_remaining = get_coffee(energy_level, coffee_available, hours_remaining)

        else:
            print("You can only choose options 1, 2, or 3.")  

    print()

    if check_win(assignments_completed,total_assignments):
            print("You completed everything in your planner. Good job!")       
    else:
        print("You ran out of library time. Try again next time!")

if __name__== "__main__":
    main()

