from random import randint

player_HP = 3
computer_HP = 3
player = False


# available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    # check to see if you picked the same thing
    if (player == computer):
        player_HP = player_HP - 0
        computer_HP = computer_HP - 0
        print("Tie! Live to shoot another day")
        print("Your Hp:", player_HP, "Com. HP:", computer_HP,)

    elif player == "Rock":
        if computer == "paper":
            # compuer won
            player_HP = player_HP - 1
            print("You lose", computer, "covers", player)
            print("Your Hp:", player_HP, "Com. HP:", computer_HP, "Cheer up!")
        else:
            computer_HP = computer_HP - 1
            print("You win!", player, "smashes", computer)
            print("Your Hp:", player_HP, "Com. HP:", computer_HP, "Cheer up!")

    elif player == "paper":
        if computer == "Scissors":
            player_HP = player_HP - 1
            print("You lose!", computer, "cuts", player)
            print("Your Hp:", player_HP, "Com. HP:", computer_HP, "Cheer up!")
        else:
            computer_HP = computer_HP - 1
            print("You win!", player, "covers", computer)
            print("Your Hp:", player_HP, "Com. HP:", computer_HP, "Cheer up!")

    elif player == "Scissors":
        if computer == "Rock":
            player_HP = player_HP - 1
            print("You lose!", computer, "samshes", player)
            print("Your Hp:", player_HP, "Com. HP:", computer_HP, "Cheer up!")
        else:
            computer_HP = computer_HP - 1
            print("You win!", player, "cuts", computer)

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    if player_HP > 0 and computer_HP > 0:

        player = False
        Computer = choices[randint(0, 2)]

    else:
        if player_HP == 0:
            print("Gameover")
        else:
            print("congratulation! You win! ")



