import tkinter as tk

class ConnectionQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connection Quiz")

        # Define the total number of questions and initialize current question index
        self.current_question = 1
        self.total_questions = 10

        # Main Frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid()

        # Question Heading
        self.question_label = tk.Label(
            self.main_frame,
            text=f"Question {self.current_question} of {self.total_questions}",
            font=("Arial", 16, "bold")
        )
        self.question_label.grid(row=0, pady=(0, 10))

        # Instructions
        self.instruction_label = tk.Label(
            self.main_frame,
            text="Select the correct word to complete each of the given compound ones. Each question has four options—choose carefully!",
            font=("Arial", 12), wrap=250, width=40, justify="center"
        )
        self.instruction_label.grid(row=1, pady=(0, 10))

        # Options Frame
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=2, pady=(0, 10))

        # Option Buttons with Colors from Final Code
        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]
        colors = ['#97D077', '#FFA07A', '#6495ED', '#FFD700']

        for i, text in enumerate(option_texts):
            button = tk.Button(
                self.options_frame, text=text, font=("Arial", 12, "bold"),
                width=15, height=2, bg=colors[i], fg="#000000",
                command=self.show_next_button
            )
            # Arrange buttons in a 2x2 grid
            row = i // 2
            column = i % 2
            button.grid(row=row, column=column, padx=10, pady=5)
            self.option_buttons.append(button)

        # Placeholder for the Next Button (initially hidden)
        self.next_button = tk.Button(
            self.main_frame, text="Next", font=("Arial", 10, "bold"),
            bg="#686D76", fg="#FFFFFF", width=10, height=1,
            command=self.next_question
        )

        self.root.mainloop()

    def show_next_button(self):
        # Display the "Next" button after an option is selected
        self.next_button.grid(row=3, pady=20)

    def next_question(self):
        # Check if this is the last question
        if self.current_question < self.total_questions:
            self.current_question += 1
            self.question_label.config(
                text=f"Question {self.current_question} of {self.total_questions}"
            )
            # Hide the "Next" button again for the next question
            self.next_button.grid_forget()
        else:
            # Close the app if it’s the last question
            self.root.destroy()

if __name__ == "__main__":
    ConnectionQuiz()
