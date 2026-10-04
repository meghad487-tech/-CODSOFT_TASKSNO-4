import tkinter as tk
import random


# ==========================================
# ROCK PAPER SCISSORS - TKINTER GAME
# ==========================================

class RockPaperScissors:

    def __init__(self, root):

        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # Colors
        self.bg_color = "#101828"
        self.card_color = "#1E293B"
        self.primary_color = "#38BDF8"
        self.secondary_color = "#334155"
        self.text_color = "#F8FAFC"
        self.gray_color = "#94A3B8"
        self.green_color = "#22C55E"
        self.red_color = "#EF4444"

        # Score Variables
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0

        # Set background
        self.root.configure(bg=self.bg_color)

        # Create the user interface
        self.create_interface()

    # ==========================================
    # CREATE USER INTERFACE
    # ==========================================

    def create_interface(self):

        # Main Heading
        tk.Label(
            self.root,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=(25, 5))

        tk.Label(
            self.root,
            text="Challenge the computer and become the champion",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack(pady=(0, 20))

        # Scoreboard Frame
        score_frame = tk.Frame(
            self.root,
            bg=self.card_color,
            padx=20,
            pady=15
        )

        score_frame.pack(pady=10)

        # User Score
        self.user_score_label = tk.Label(
            score_frame,
            text="YOU\n0",
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.green_color,
            width=12
        )

        self.user_score_label.grid(
            row=0,
            column=0,
            padx=15
        )

        # Tie Score
        self.tie_score_label = tk.Label(
            score_frame,
            text="TIES\n0",
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            width=12
        )

        self.tie_score_label.grid(
            row=0,
            column=1,
            padx=15
        )

        # Computer Score
        self.computer_score_label = tk.Label(
            score_frame,
            text="COMPUTER\n0",
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.red_color,
            width=12
        )

        self.computer_score_label.grid(
            row=0,
            column=2,
            padx=15
        )

        # Game Information Card
        game_frame = tk.Frame(
            self.root,
            bg=self.card_color,
            padx=40,
            pady=30
        )

        game_frame.pack(
            padx=80,
            pady=20,
            fill="both",
            expand=True
        )

        # Instruction
        tk.Label(
            game_frame,
            text="Choose Your Move",
            font=("Arial", 20, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).pack(pady=(5, 20))

        # Buttons Frame
        button_frame = tk.Frame(
            game_frame,
            bg=self.card_color
        )

        button_frame.pack(pady=10)

        # Rock Button
        self.create_choice_button(
            button_frame,
            "ROCK",
            0,
            "#475569"
        )

        # Paper Button
        self.create_choice_button(
            button_frame,
            "PAPER",
            1,
            "#2563EB"
        )

        # Scissors Button
        self.create_choice_button(
            button_frame,
            "SCISSORS",
            2,
            "#7C3AED"
        )

        # User Choice Display
        self.user_choice_label = tk.Label(
            game_frame,
            text="Your Choice: Waiting...",
            font=("Arial", 14),
            bg=self.card_color,
            fg=self.text_color
        )

        self.user_choice_label.pack(pady=(25, 8))

        # Computer Choice Display
        self.computer_choice_label = tk.Label(
            game_frame,
            text="Computer Choice: Waiting...",
            font=("Arial", 14),
            bg=self.card_color,
            fg=self.text_color
        )

        self.computer_choice_label.pack(pady=8)

        # Result Label
        self.result_label = tk.Label(
            game_frame,
            text="Make your move to start the game!",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        )

        self.result_label.pack(pady=20)

        # Restart Button
        restart_button = tk.Button(
            game_frame,
            text="RESET GAME",
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg=self.text_color,
            activebackground=self.primary_color,
            activeforeground="black",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.reset_game
        )

        restart_button.pack(pady=5)

        # Footer
        tk.Label(
            self.root,
            text="Python Tkinter Project | Rock Paper Scissors",
            font=("Arial", 9),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack(pady=10)

    # ==========================================
    # CREATE CHOICE BUTTON
    # ==========================================

    def create_choice_button(
        self,
        parent,
        text,
        column,
        color
    ):

        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="black",
            relief="flat",
            padx=25,
            pady=18,
            width=12,
            cursor="hand2",
            command=lambda: self.play_game(text.title())
        )

        button.grid(
            row=0,
            column=column,
            padx=10
        )

    # ==========================================
    # GAME LOGIC
    # ==========================================

    def play_game(self, user_choice):

        # Computer randomly chooses
        computer_choice = random.choice(
            ["Rock", "Paper", "Scissors"]
        )

        # Display choices
        self.user_choice_label.config(
            text=f"Your Choice: {user_choice}"
        )

        self.computer_choice_label.config(
            text=f"Computer Choice: {computer_choice}"
        )

        # Determine winner
        if user_choice == computer_choice:

            result = "IT'S A TIE!"
            result_color = self.primary_color

            self.tie_score += 1

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or
            (user_choice == "Paper" and computer_choice == "Rock")
            or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):

            result = "YOU WIN!"
            result_color = self.green_color

            self.user_score += 1

        else:

            result = "COMPUTER WINS!"
            result_color = self.red_color

            self.computer_score += 1

        # Update result
        self.result_label.config(
            text=result,
            fg=result_color
        )

        # Update scoreboard
        self.update_scoreboard()

    # ==========================================
    # UPDATE SCOREBOARD
    # ==========================================

    def update_scoreboard(self):

        self.user_score_label.config(
            text=f"YOU\n{self.user_score}"
        )

        self.tie_score_label.config(
            text=f"TIES\n{self.tie_score}"
        )

        self.computer_score_label.config(
            text=f"COMPUTER\n{self.computer_score}"
        )

    # ==========================================
    # RESET GAME
    # ==========================================

    def reset_game(self):

        # Reset scores
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0

        # Update scoreboard
        self.update_scoreboard()

        # Reset text
        self.user_choice_label.config(
            text="Your Choice: Waiting..."
        )

        self.computer_choice_label.config(
            text="Computer Choice: Waiting..."
        )

        self.result_label.config(
            text="Make your move to start the game!",
            fg=self.primary_color
        )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    game = RockPaperScissors(root)

    root.mainloop()