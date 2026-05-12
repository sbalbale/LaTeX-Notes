import random
import math
import os

def clear_screen():
    # Helper to hide secret inputs in PvP mode
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n[Screen cleared to hide secret inputs from the other player]\n")

class GameOfGames:
    def __init__(self):
        self.p1_wins = 0
        self.p2_wins = 0
        self.vs_computer = True # Default, set in main menu
        
        self.game_stats = {
            "Coin Flip": {"p1": 0, "p2": 0},
            "Find the Thimble": {"p1": 0, "p2": 0},
            "Guess the Number": {"p1": 0, "p2": 0},
            "Even and Odd": {"p1": 0, "p2": 0},
            "Find the Red Thread": {"p1": 0, "p2": 0}
        }

    def start(self):
        print("="*30)
        print("WELCOME TO THE GAME OF GAMES")
        print("="*30)
        print("Select Game Mode:")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        while True:
            choice = input("> ").strip()
            if choice == '1':
                self.vs_computer = False
                break
            elif choice == '2':
                self.vs_computer = True
                break
            print("Invalid. Enter 1 or 2.")
        self.main_menu()

    def main_menu(self):
        while True:
            p2_name = "Computer" if self.vs_computer else "Player 2"
            print("\n" + "="*30)
            print("      MAIN MENU")
            print("="*30)
            print("1. Play Coin Flip")
            print("2. Play Find the Thimble")
            print("3. Play Guess the Number")
            print("4. Play Even and Odd")
            print("5. Play Find the Red Thread")
            print("Q. Quit")
            
            choice = input("Select an option: ").strip().upper()
            
            if choice == '1':
                self.play_coin_flip()
                self.display_game_scoreboard("Coin Flip")
            elif choice == '2':
                self.play_find_the_thimble()
                self.display_game_scoreboard("Find the Thimble")
            elif choice == '3':
                self.play_guess_the_number()
                self.display_game_scoreboard("Guess the Number")
            elif choice == '4':
                self.play_even_and_odd()
                self.display_game_scoreboard("Even and Odd")
            elif choice == '5':
                self.play_find_the_red_thread()
                self.display_game_scoreboard("Find the Red Thread")
            elif choice == 'Q':
                self.quit_game()
                break
            else:
                print("Invalid selection.")

    def display_game_scoreboard(self, game_name):
        p2_name = "Computer" if self.vs_computer else "Player 2"
        print("\n--- Scoreboard for {} ---".format(game_name))
        print("Player 1 wins: {}".format(self.game_stats[game_name]["p1"]))
        print("{} wins: {}".format(p2_name, self.game_stats[game_name]["p2"]))
        print("---------------------------------")

    def quit_game(self):
        p2_name = "Computer" if self.vs_computer else "Player 2"
        print("\n" + "="*30)
        print("        FINAL SCOREBOARD")
        print("="*30)
        print("Overall Player 1 Wins: {}".format(self.p1_wins))
        print("Overall {} Wins: {}".format(p2_name, self.p2_wins))
        
        if self.p1_wins > self.p2_wins:
            print("\nCongratulations Player 1! You won The Game of Games!")
        elif self.p2_wins > self.p1_wins:
            print("\n{} won The Game of Games. Better luck next time!".format(p2_name))
        else:
            print("\nThe Game of Games ended in a tie!")

    # --- HELPER METHODS ---
    def get_odd_best_out_of(self):
        while True:
            try:
                val = int(input("Enter the 'best out of' number (must be odd): "))
                if val % 2 != 0 and val > 0: return val
                else: print("Error: Must be an odd, positive integer.")
            except ValueError:
                print("Error: Please enter a valid number.")

    def assign_roles(self, role_a, role_b):
        p2_name = "Computer" if self.vs_computer else "Player 2"
        print(f"\nWho will be the {role_a}?")
        print("1. Player 1")
        print(f"2. {p2_name}")
        while True:
            choice = input("> ").strip()
            if choice == '1':
                return "p1", "p2" # Guesser, Other
            elif choice == '2':
                return "p2", "p1" # Guesser, Other
            print("Invalid choice.")

    def award_win(self, winner_key, game_name):
        self.game_stats[game_name][winner_key] += 1
        if winner_key == "p1":
            self.p1_wins += 1
            print("\n*** Player 1 wins the game! ***")
        else:
            self.p2_wins += 1
            p2_name = "Computer" if self.vs_computer else "Player 2"
            print(f"\n*** {p2_name} wins the game! ***")

    # --- GAME 1: COIN FLIP ---
    def play_coin_flip(self):
        print("\n--- Playing Coin Flip ---")
        best_out_of = self.get_odd_best_out_of()
        win_threshold = math.ceil(best_out_of / 2)
        
        guesser, flipper = self.assign_roles("Guesser", "Flipper")
        points = {"p1": 0, "p2": 0}

        while points["p1"] < win_threshold and points["p2"] < win_threshold:
            # Guesser turn
            if guesser == "p2" and self.vs_computer:
                guess = random.choice(['H', 'T'])
                print(f"Computer guesses: {guess}")
            else:
                while True:
                    guess = input(f"Guesser ({'Player 1' if guesser == 'p1' else 'Player 2'}), call it - Heads (H) or Tails (T)? ").strip().upper()
                    if guess in ['H', 'T']: break

            # Flipper turn
            if flipper == "p2" and self.vs_computer:
                print("Computer is flipping the coin...")
            else:
                input(f"Flipper ({'Player 1' if flipper == 'p1' else 'Player 2'}), press Enter to flip...")
            
            result = random.choice(['H', 'T'])
            print("The coin landed on: {}".format("Heads" if result == 'H' else "Tails"))

            if guess == result:
                print("Guesser got it right!")
                points[guesser] += 1
            else:
                print("Guesser got it wrong. Point to Flipper!")
                points[flipper] += 1
            
            p2_name = "Computer" if self.vs_computer else "Player 2"
            print(f"Score -> Player 1: {points['p1']} | {p2_name}: {points['p2']}")

        winner = "p1" if points["p1"] >= win_threshold else "p2"
        self.award_win(winner, "Coin Flip")

    # --- GAME 2: FIND THE THIMBLE ---
    def play_find_the_thimble(self):
        print("\n--- Playing Find the Thimble ---")
        best_out_of = self.get_odd_best_out_of()
        win_threshold = math.ceil(best_out_of / 2)
        
        guesser, hider = self.assign_roles("Guesser", "Hider")
        points = {"p1": 0, "p2": 0}

        while points["p1"] < win_threshold and points["p2"] < win_threshold:
            # Hider turn
            if hider == "p2" and self.vs_computer:
                result = random.choice(['L', 'R'])
                print("Computer has hidden the thimble.")
            else:
                while True:
                    hider_name = 'Player 1' if hider == 'p1' else 'Player 2'
                    result = input(f"{hider_name} (Hider), which hand? Left (L) or Right (R)? ").strip().upper()
                    if result in ['L', 'R']:
                        clear_screen()
                        break

            # Guesser turn
            if guesser == "p2" and self.vs_computer:
                guess = random.choice(['L', 'R'])
                print(f"Computer guesses: {guess}")
            else:
                while True:
                    guesser_name = 'Player 1' if guesser == 'p1' else 'Player 2'
                    guess = input(f"{guesser_name} (Guesser), guess hand - Left (L) or Right (R)? ").strip().upper()
                    if guess in ['L', 'R']: break

            print("The thimble was in the {} hand.".format("Left" if result == 'L' else "Right"))

            if guess == result:
                print("Guesser found it!")
                points[guesser] += 1
            else:
                print("Empty hand! Point to Hider.")
                points[hider] += 1
                
            p2_name = "Computer" if self.vs_computer else "Player 2"
            print(f"Score -> Player 1: {points['p1']} | {p2_name}: {points['p2']}")

        winner = "p1" if points["p1"] >= win_threshold else "p2"
        self.award_win(winner, "Find the Thimble")

    # --- GAME 3: GUESS THE NUMBER ---
    def play_guess_the_number(self):
        print("\n--- Playing Guess the Number ---")
        while True:
            try:
                range_max = int(input("Enter the maximum range (e.g., 10 for 1-10): "))
                if range_max > 1: break
            except ValueError: pass

        max_allowed_guesses = max(1, range_max // 2)
        while True:
            try:
                num_guesses = int(input(f"How many guesses allowed? (Max {max_allowed_guesses}): "))
                if 0 < num_guesses <= max_allowed_guesses: break
            except ValueError: pass

        guesser, selector = self.assign_roles("Guesser", "Number Selector")

        # Selector turn
        if selector == "p2" and self.vs_computer:
            target = random.randint(1, range_max)
            print("Computer has selected a target number.")
        else:
            while True:
                try:
                    selector_name = 'Player 1' if selector == 'p1' else 'Player 2'
                    target = int(input(f"{selector_name} (Selector), enter secret number (1-{range_max}): "))
                    if 1 <= target <= range_max:
                        clear_screen()
                        break
                except ValueError: pass

        guesser_won = False
        for i in range(num_guesses):
            if guesser == "p2" and self.vs_computer:
                guess = random.randint(1, range_max) # Note: A real bot would do binary search, keeping it simple here
                print(f"Computer guesses: {guess}")
            else:
                try:
                    guesser_name = 'Player 1' if guesser == 'p1' else 'Player 2'
                    guess = int(input(f"\n{guesser_name}, Guess {i+1}/{num_guesses}: "))
                except ValueError:
                    print("Invalid input, wasted guess!")
                    continue

            if guess == target:
                guesser_won = True
                break
            elif guess < target:
                print("Too low!")
            else:
                print("Too high!")

        winner = guesser if guesser_won else selector
        print(f"\nThe target number was {target}!")
        self.award_win(winner, "Guess the Number")

    # --- GAME 4: EVEN AND ODD ---
    def play_even_and_odd(self):
        print("\n--- Playing Even and Odd ---")
        while True:
            alignment = input("Player 1, do you want to be Even (E) or Odd (O)? ").strip().upper()
            if alignment in ['E', 'O']: break

        p1_is_even = (alignment == 'E')
        p2_is_even = not p1_is_even
        
        p2_name = "Computer" if self.vs_computer else "Player 2"
        print(f"Player 1 is {'Even' if p1_is_even else 'Odd'}.")
        print(f"{p2_name} is {'Even' if p2_is_even else 'Odd'}.")

        best_out_of = self.get_odd_best_out_of()
        win_threshold = math.ceil(best_out_of / 2)
        points = {"p1": 0, "p2": 0}

        while points["p1"] < win_threshold and points["p2"] < win_threshold:
            # P1 throw
            while True:
                try:
                    p1_throw = int(input("\nPlayer 1, throw a number (1-5): "))
                    if 1 <= p1_throw <= 5: 
                        if not self.vs_computer: clear_screen()
                        break
                except ValueError: pass
            
            # P2 throw
            if self.vs_computer:
                p2_throw = random.randint(1, 5)
            else:
                while True:
                    try:
                        p2_throw = int(input("Player 2, throw a number (1-5): "))
                        if 1 <= p2_throw <= 5: break
                    except ValueError: pass
            
            total = p1_throw + p2_throw
            is_total_even = (total % 2 == 0)
            
            print(f"\nPlayer 1 threw: {p1_throw}")
            print(f"{p2_name} threw: {p2_throw}")
            print(f"Sum is: {total} ({'Even' if is_total_even else 'Odd'})")

            if (is_total_even and p1_is_even) or (not is_total_even and not p1_is_even):
                print("Point for Player 1!")
                points["p1"] += 1
            else:
                print(f"Point for {p2_name}!")
                points["p2"] += 1
                
            print(f"Score -> Player 1: {points['p1']} | {p2_name}: {points['p2']}")

        winner = "p1" if points["p1"] >= win_threshold else "p2"
        self.award_win(winner, "Even and Odd")

    # --- GAME 5: FIND THE RED THREAD ---
    def play_find_the_red_thread(self):
        print("\n--- Playing Find the Red Thread ---")
        while True:
            try:
                pull_amt = int(input("How many spools to pull at a time? (Max 10): "))
                if 1 <= pull_amt <= 10: break
            except ValueError: pass

        first_puller, second_puller = self.assign_roles("First Puller", "Second Puller")

        box = ['W'] * 19 + ['R']
        random.shuffle(box)
        
        turn = first_puller
        winner = None

        while box:
            current_name = "Player 1" if turn == 'p1' else ("Computer" if self.vs_computer else "Player 2")
            
            if turn == 'p2' and self.vs_computer:
                print(f"\n{current_name} is pulling...")
            else:
                input(f"\n{current_name}, press Enter to pull {pull_amt} spools...")
                
            pull = [box.pop() for _ in range(min(pull_amt, len(box)))]
            print(f"{current_name} pulled: {pull}")
            
            if 'R' in pull:
                winner = turn
                break
                
            turn = second_puller if turn == first_puller else first_puller

        print("\n*** The Red Thread was found! ***")
        self.award_win(winner, "Find the Red Thread")

if __name__ == "__main__":
    game = GameOfGames()
    game.start()