import tkinter as tk

class ConnectionQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connection Quiz")

        # Main Frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid()

        # Question Number
        self.question_label = tk.Label(self.main_frame, text="Question # of #", font=("Arial", 16, "bold"))
        self.question_label.grid(row=0, pady=(0, 10))

        # Instructions
        self.instruction_label = tk.Label(
            self.main_frame,
            text="Select the correct word to complete each of the given compound ones. Each question has four options—choose carefully!",
            font=("Arial", 12), wrap=250, width=40, justify="center"
        )
        self.instruction_label.grid(row=1, pady=(0, 10))

        # Category Label
        self.category_label = tk.Label(self.main_frame, text="Category: before/after", font=("Arial", 14, "bold"))
        self.category_label.grid(row=2, pady=(0, 10))

        # Options Frame
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=3, pady=(0, 10))

        # Option Buttons with Colors from Final Code
        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]
        colors = ['#97D077', '#FFA07A', '#6495ED', '#FFD700']

        for i, text in enumerate(option_texts):
            button = tk.Button(
                self.options_frame, text=text, font=("Arial", 12, "bold"),
                width=15, height=2, bg=colors[i], fg="#000000"
            )
            # Arrange buttons in a 2x2 grid
            row = i // 2
            column = i % 2
            button.grid(row=row, column=column, padx=10, pady=5)
            self.option_buttons.append(button)

        self.root.mainloop()

if __name__ == "__main__":
    ConnectionQuiz()
