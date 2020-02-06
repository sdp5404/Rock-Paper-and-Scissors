import random
import sys
import time

class RPS():

    def __init__(self):
        # setup the random chooser for the computer
        self.rand = random.Random()
        self.score1 = 0  # computer score
        self.score2 = 0  # human score
        self.attempt_remaining = 3

    def comp_move(self):
        return self.rand.randrange(1, 4)

    def human_move(self):

        while True:
            if self.attempt_remaining != 0:

                print("Please make your move by entering 1, 2, or 3.")
                print("                     or                      ")
                print("Please make your move by entering 'Rock', 'Paper', or 'Scissor'.")
                print("\nNumber of attempt left : " + str(self.attempt_remaining))
                print("\nRock (1), Paper (2), Scissors(3) Shoot -->")
                choice = input("Make your move:")
                choice = choice.strip()
                if choice == "1" or choice == "Rock":
                    return 1
                elif choice == "2" or choice == "Paper":
                    return 2
                elif choice == "3" or choice == "Scissors":
                    return 3
                else:
                    print("\nIt's an invalid move, please try again.\n")
                    print('-' * 20)
                    self.attempt_remaining -= 1
            else:
                return 4

    def decide_winner(self, comp, human):
        score1 = 0
        score2 = 0
        if (comp, human) == (1, 3):
            print("Rock breaks Scissors")
            print("Computer Wins")
            print("-------------")
            self.score1 += 1
        elif (human, comp) == (1, 3):
            print("Rock breaks Scissors")
            print("You Win")
            print("-------")
            self.score2 += 1
        elif (comp, human) == (2, 1):
            print("Paper covers Rock")
            print("Computer Wins")
            print("-------------")
            self.score1 += 1
        elif (human, comp) == (2, 1):
            print("Paper covers Rock")
            print("You Win")
            print("-------")
            self.score2 += 1
        elif (comp, human) == (3, 2):
            print("Scissors cuts Paper")
            print("Computer Wins")
            print("-------------")
            self.score1 += 1
        elif (human, comp) == (3, 2):
            print("Scissors cuts Paper")
            print("You Win")
            prnit("-------")
            self.score2 += 1
        else:
            print("It's a Draw!!")
            print("-------------")

    def display_score(self):
        print("Score:")
        print("Computer: ", self.score1, " You: ", self.score2)

    def play_again(self):
        yes_no = input("\nDo you want to play again (to reset score type 'r') ? (y/n/r):")
        yes_no = yes_no.strip()
        yes_no = yes_no.lower()
        if yes_no == "n" or yes_no == "no":
            return False
        elif yes_no == "r":
            self.score1 = 0
            self.score2 = 0
            self.attempt_remaining = 3
            print("Score is now reset")
            print("--------------------")
            print("Computer: ", self.score1, " You: ", self.score2)
        return True

    def game_loop(self):
        while True:
            computerMove = self.comp_move()
            humanMove = self.human_move()
            if humanMove != 4:
                print()
                print("you chose: ", humanMove, " computer chose: ", computerMove)
                self.decide_winner(computerMove, humanMove)
                print()
                self.display_score()
                if self.play_again() == False:
                    print("Bye Bye....")
                    sys.exit(0)
                print("\n")
            else:
                print("\nToo many wrong attempt, Bye Bye\n")
                time.sleep(1.0)
                sys.exit(0)


if __name__ == '__main__':
    print('*' * 50)
    print('-' * 50)
    print("|         Rock, Paper, Scissors The Game         |")
    print("-" * 50)
    print("     Welcome to Rock Paper Scissors The Game.")
    print('*' * 50)
    rps = RPS()
    rps.game_loop()