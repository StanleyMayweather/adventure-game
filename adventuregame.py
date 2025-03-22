# Adventure Game: A man in a leaking boat surrounded by sharks
# This program involves choices that lead to different outcomes.
# The user can make decisions at each stage, and the story changes based on those decisions.

print("You are in a leaking boat, 10 kilometers away from an island. You're surrounded by 5 sharks!")
print("You need to make a quick decision to survive. Good luck!")

# First decision: Should you try to repair the boat or fight the sharks?
choice1 = input("Do you want to REPAIR the boat or FIGHT the sharks? ").lower()

if choice1 == "repair":
    print("You start patching up the boat, but the sharks are getting closer!")
    # Second decision after repairing the boat
    choice2 = input("Do you want to PADDLE towards the island or WAIT and hope the sharks leave? ").lower()
    
    if choice2 == "paddle":
        print("You begin paddling towards the island. The boat seems to be holding up.")
        # Third decision while paddling
        choice3 = input("You're almost halfway there, but your paddle breaks. Do you want to KEEP paddling or SIGNAL for help? ").lower()
        
        if choice3 == "keep paddling":
            print("You manage to reach the island, barely alive but victorious!")
        elif choice3 == "signal":
            print("You signal for help, but no one is around to rescue you. The sharks catch up to you.")
        else:
            print("Invalid choice! The sharks catch up to you.")
    elif choice2 == "wait":
        print("You wait, but the sharks grow more aggressive. Eventually, your boat sinks.")
    else:
        print("Invalid choice! The sharks catch up to you.")
        
elif choice1 == "fight":
    print("You try to fight the sharks off, but you’re outnumbered and quickly overwhelmed.")
    # Second decision after fighting the sharks
    choice2 = input("Do you want to ESCAPE into the water or WAIT to see if they go away? ").lower()
    
    if choice2 == "escape":
        print("You jump into the water, but the sharks circle around you!")
        # Third decision after jumping into the water
        choice3 = input("Do you want to SWIM to the island or DIVE deep to escape? ").lower()
        
        if choice3 == "swim":
            print("You swim towards the island, but the sharks catch up before you can make it.")
        elif choice3 == "dive":
            print("You dive deep into the water and manage to escape the sharks, but you’re lost and exhausted.")
        else:
            print("Invalid choice! The sharks catch up to you.")
    elif choice2 == "wait":
        print("You wait, hoping the sharks will leave. Unfortunately, they don’t. The boat sinks, and you're left stranded.")
    else:
        print("Invalid choice! The sharks catch up to you.")
        
else:
    print("Invalid choice! The sharks attack, and the boat sinks.")
    
