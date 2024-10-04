# Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Invalid action choice in the forest
elif place == "cave":
    # Task 2: Setting the Scene
    action2 = input("light a torch or proceed in the dark? ")
    if action2 == "light a torch":
        print("You found a hidden treasure!")
    elif action2 == "proceed in the dark":
        print("You found a monster!")
    else:
        pass  # Invalid action choice in the cave
# Task 3: Default Path
else:
    pass  # Invalid place choice
