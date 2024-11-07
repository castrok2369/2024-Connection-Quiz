import csv
import tkinter as tk
import random
from tkinter import messagebox


class ConnectionQuiz:
    def __init__(self):
        self.questions = []
        self.load_questions()

        self.current_question_index = 0
        self.num_questions = 10  # Limit to 10 questions, as specified
        self.selected_answer = None

        self.root = tk.Tk()
        self.root.title("Connection Quiz")

        # Main frame setup
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid()

        # Question heading
        self.question_label = tk.Label(self.main_frame,
                                       text=f"Question {self.current_question_index + 1} of {self.num_questions}",
                                       font=("Arial", 16, "bold"))
        self.question_label.grid(row=0, pady=(0, 10))

        # Instructions
        self.instruction_label = tk.Label(self.main_frame,
                                          text="Select the correct word to complete each of the given compound ones. Each question has four options—choose carefully!",
                                          font=("Arial", 12), wrap=250, width=40, justify="center")
        self.instruction_label.grid(row=1, pady=(0, 10))

        # Category display
        self.category_label = tk.Label(self.main_frame, text="", font=("Arial", 14, "bold"))
        self.category_label.grid(row=2, pady=(0, 10))

        # Words frame with bordered boxes
        self.words_frame = tk.Frame(self.main_frame)
        self.words_frame.grid(row=3, pady=10)

        # Options frame for answer buttons
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=4, pady=10)

        # Option buttons setup with colors from final code
        self.option_buttons = []
        colors = ['#97D077', '#FFA07A', '#6495ED', '#FFD700']
        for i in range(4):
            button = tk.Button(self.options_frame, font=("Arial", 12, "bold"), width=15, height=2,
                               bg=colors[i], fg="#000000", command=lambda idx=i: self.select_answer(idx))
            button.grid(row=i // 2, column=i % 2, padx=10, pady=5)
            self.option_buttons.append(button)

        # Next button, initially hidden and styled to match final code
        self.next_button = tk.Button(self.main_frame, text="Next", font=("Arial", 10, "bold"), bg="#686D76",
                                     fg="#FFFFFF", width=10, height=1, command=self.next_question)
        self.next_button.grid(row=5, pady=10)
        self.next_button.grid_remove()  # Hide until an option is selected

        self.load_question()
        self.root.mainloop()

    def load_questions(self):
        """Load questions and answers from CSV."""
        try:
            with open("connections_quiz.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    category = row[0]
                    words = row[1:5]
                    answer = row[5]
                    self.questions.append({"category": category, "words": words, "answer": answer})
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'connections_quiz.csv' not found.")
            self.root.destroy()

    def load_question(self):
        """Display the current question, options, and category."""
        question_data = self.questions[self.current_question_index]
        self.category_label.config(text=f"Category: {question_data['category']}")

        # Display words in bordered boxes
        for widget in self.words_frame.winfo_children():
            widget.destroy()

        for word in question_data["words"]:
            word_frame = tk.Frame(self.words_frame, highlightbackground="#000000", highlightthickness=1, padx=5, pady=5)
            word_frame.pack(side=tk.LEFT, padx=5)
            word_label = tk.Label(word_frame, text=word, font=("Arial", 14))
            word_label.pack()

        # Generate and display options
        options = [question_data["answer"]] + random.sample(
            [q["answer"] for q in self.questions if q["answer"] != question_data["answer"]], 3
        )
        random.shuffle(options)

        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option, state="normal", relief="raised")

        # Update question header and reset next button
        self.question_label.config(text=f"Question {self.current_question_index + 1} of {self.num_questions}")
        self.next_button.grid_remove()
        self.selected_answer = None

    def select_answer(self, index):
        """Handle answer selection."""
        self.selected_answer = self.option_buttons[index].cget("text")

        # Highlight selected button
        for button in self.option_buttons:
            button.config(relief="raised")
        self.option_buttons[index].config(relief="sunken")

        # Show Next button
        self.next_button.grid()

    def next_question(self):
        """Proceed to the next question or end the quiz."""
        self.current_question_index += 1
        if self.current_question_index < self.num_questions:
            self.load_question()
        else:
            self.root.destroy()  # Close application upon reaching the last question


if __name__ == "__main__":
    ConnectionQuiz()
