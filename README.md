# Day in the Life, Library Study Session Game

## Game Summary
This game simulates a very common part of a college student's day in the life: working in the library. The player has to manage their time and energy in the library while trying to complete everything in their planner.

Throughout this game, the player can choose whether to work on an assignment, take a break, or get coffee. Random events can also happen that either help or hurt their energy level. The goal is to finish all assignments before running out of time.

## How to Play
1) Enter the amount of assignments you have
2) Enter the name of each assignment, then the game can keep track of them
3) The game starts with 5 energy points, the number of hours availble is dependent on the amount of assignments entered, with 3 additional hours given.
4) Each turn you have a choise of three different activities
    - Work on an assignment: Uses an hour and 2 energy points. The player can pick which assignment they want to work on. If the player has enough energy they can complete. it and remove it from the assignment list.
    - Take a break: Uses an hour and restores 2 energy points
    - Get coffee: Uses an hour and randomly restores 1 or 2 energy points. You can only get coffee once
5) After an assignment is completed, a random event occurs that can increase or decrease your energy
6) The game ends when all the assignments are completed or if time runs out.

Energy levels cannot go above 5 and not go below 0. You can try to work without enough energy, but you will still lose an hour. If you choose an invalid action or try to get coffee twice, you will also lose an hour. 

## How User State is Tracked
There are multiple variables used to keep track of the player's progress throughout the game
- assignments: I made a list to store the names of the assignments the player needs to complete. When they finish the assignment, the item gets removed from the list. I decided to use this list because it was easy to add assignments, display them, and remove them while the player completes their work.
- hours_remaining: This is an integer value that keeps track of how much time the player has left in the library. Hours decrease as the player makes choices
- energy: This is an integer value that represents the player's energy level. This fluctuates based on the action the player chooses to do.
- coffee_available: This is a Boolean that keeps track of whether the player has alreafy gotten coffee. It will start off as True and change to False after the player gets coffee.
- chech_assignments_complete() and check_game_result() are used to determine whether the player has won. The player wins if the assignment list is empty by the time the game ends. 

## Functions and Control Flow
I organized the game into different and specific functions in order to make the code clearer to organize and understand. The functions handle entering assignments, validating user input, selecting assignments, and checking the final result. I also imported some of the functions I worked in from draft_program.py. These were used to handle working, taking breaks, getting coffee, choosing actions, and random events.

The main game runs inside a while loop that runs as long as the player has remaining time and assignments left to complete. If the player chooses to work they select an assignment and the game will check if they have enough energy to complete it. If they do, the assignment is completed and a random event occcurs.

I used other loops to make sure that players enter valid numbers and assignment names. I used conditional statements to control what happens based on the player's decions.

The control flow goes as follows: Start game -> Enter number of assignments -> Name assignments -> Start with time and energy -> choose action

Based on the action chosen:
- work -> Select assignment -> check energy -> complete assignment -> random event
- break -> restore energy -> lose an hour
- coffee -> check availability -> restore energy if available -> lose an hour

After each action the game checks if the player has finished assignments or run out of time. If neither of these occured, the player chooses another action. 

## Peer Review Improvements
After receiving feedback from my classmates, there were several changes I decided to improve from my original draft. One of the biggest issues that both peer reviewers recognized was entering certain values could cause errors or make the game immediately end. To prevent this, I added input validation to each of my functions.

Both reviewers also pointed out that my game only had one loop. I decided to add more loops for entering and selecting assignments. I also took the suggestion of changing the game to store assignment names in a list instead of only counting completed assignments. That way, the player can keep track of the assignment they are working on and the assignments they have left.

Another suggestion I took was to adjust the amount of library time based on how many assignments the player has. I changed the starting hours so the players would have more time when they had a higher volume of assignments. 

I also fixed the issue where players could repeatedly enter invalid actions without losing time. This way players couldn't repeatedly choose coffee. I also improved the win/loss checking system and made parts of my code easier to read. 

## How to Run Game

Make sure that final_project.py and draft_program.py are in the same folder. In order to start the game, open a terminal in this folder and run the code:

python3 final_project.py

This way the code will start running. The player can follow instructions in the terminal to play the game. 


T