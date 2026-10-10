from abobakr_tools import get_pseudo_random_int

user_wins = 0
computer_wins = 0

# تحسين الأسماء: أسماء أكثر وضوحاً
user_win_conditions = ["rock", "paper", "scissors"]
computer_win_conditions = ["scissors", "rock", "paper"]

valid_choices = ["rock", "paper", "scissors"]

while True:
    user_won = False
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower().strip()
    
    if user_input == "q":
        break

    if user_input not in valid_choices:
        continue

    random_number = get_pseudo_random_int(0, 2)
    computer_pick = valid_choices[random_number]
    print("Computer picked", computer_pick + ".")

    # نفس المنطق الأصلي تماماً، فقط مع أسماء أوضح
    for i in range(len(valid_choices)):
        if user_input == user_win_conditions[i] and computer_pick == computer_win_conditions[i]:
            user_wins += 1
            user_won = True
            break
    
    if user_won:
        print("You won!")
    elif user_input == computer_pick:
        print("You drew.")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")