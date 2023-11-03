import random
import tkinter as tk

# Initialize the game variables
player_score = 0
computer_score = 0
turn = 0
current_round = 0

# Function to update the game state
def update_game_state():
    global player_score, computer_score, turn, current_round
    turn_label.config(text="Turn " + str(turn))
    player_score_label.config(text="Your Score: " + str(player_score))
    computer_score_label.config(text="Computer Score: " + str(computer_score))
    current_round_label.config(text="This round you have: " + str(current_round))

# Player's turn logic
def take_turn():
    global current_round, player_score
    player_choice = choice_var.get()
    if player_choice == "Roll":
        die_result = random.randint(1, 6)
        current_round += die_result
        roll_result_label.config(text="You rolled a " + str(die_result))
        if die_result == 1:
            roll_result_label.config(text="You rolled a 1! You get a zero for this round!")
            current_round = 0
            update_game_state()
    elif player_choice == "Bank":
        player_score += current_round
        current_round = 0
        update_game_state()
    current_round_label.config(text="This round you have: " + str(current_round))

# Computer's turn logic
def computer_turn():
    global current_round, computer_score
    while current_round <= 15:
        die_result = random.randint(1, 6)
        current_round += die_result
        if die_result == 1:
            current_round = 0
            break
    computer_score += current_round
    current_round = 0
    update_game_state()

def end_game_button():
    if player_score >= computer_score:
        result_label.config(text="Congratulations! You won in " + str(turn) + " turns!")
    else:
        result_label.config(text="Good try! The Computer won in " + str(turn) + " turns.")

# Initialize the main game window
window = tk.Tk()
window.title("Pig Dice Game")
window.geometry('500x500')

# Create labels to display game information
turn_label = tk.Label(window, text="Turn " + str(turn))
turn_label.pack()
player_score_label = tk.Label(window, text="Your Score: " + str(player_score))
player_score_label.pack()
computer_score_label = tk.Label(window, text="Computer Score: " + str(computer_score))
computer_score_label.pack()
current_round_label = tk.Label(window, text="This round you have: " + str(current_round))
current_round_label.pack()

# Create radio buttons for player's choice
choice_var = tk.StringVar()
choice_var.set("Roll")
roll_radio = tk.Radiobutton(window, text="Roll", variable=choice_var, value="Roll")
roll_radio.pack()
bank_radio = tk.Radiobutton(window, text="Bank", variable=choice_var, value="Bank")
bank_radio.pack()

# Create buttons to take the player's turn and the computer's turn
player_turn_button = tk.Button(window, text="Take Your Turn", command=take_turn, height=20, width=20, bg="red")
player_turn_button.place(x=0)
computer_turn_button = tk.Button(window, text="Let Computer Play", command=computer_turn, height=20, width=20, bg='blue')
computer_turn_button.place(x=350)
end_game_button = tk.Button(window, text='End Game', command=end_game_button, height=18, width=70, bg='green')
end_game_button.place(x=0, y=300)

# Create labels to display roll results and current round
roll_result_label = tk.Label(window, text="")
roll_result_label.pack()
current_round_label = tk.Label(window, text="This round you have: " + str(current_round))
current_round_label.pack()

# Label to display game result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the game loop
window.mainloop()