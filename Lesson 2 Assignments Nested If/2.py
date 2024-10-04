# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue1 = "large hall"
venue2 = "conference room"

if attendees > 100:
    print(venue1)
    print("audio system")  # For larger events
else:
    print(venue2)
    print("projector")  # For smaller events

# Task 2: Venue Selection
# Either "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices
vegetarian = input("Do you want vegetarian food? (yes or no): ").lower()

if vegetarian == "yes":
    print("We recommend Veggie Delight Caterers.")
else:
    print("We recommend Gourmet Meals Caterers.")
