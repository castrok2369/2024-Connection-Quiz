import tkinter as tk
from tkinter import messagebox


class SimpleEntryApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connection Quiz")

        self.temp_frame = tk.Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        self.setup_start_screen()

        self.root.mainloop()

    def setup_start_screen(self):
        # Clear the frame
        self.clear_frame()

        # Set up the initial screen to enter the number of questions
        self.temp_heading = tk.Label(self.temp_frame, text="Connection Quiz", font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        self.temp_instructions = tk.Label(
            self.temp_frame,
            text="To begin, you must enter the number of questions you want the quiz to give you. \n\n"
                 "Then, you will be prompted to answer each question. Good luck!",
            wrap=250, width=40, justify="left"
        )
        self.temp_instructions.grid(row=1)

        self.space_label = tk.Label(self.temp_frame, text="", font=("Arial", "8"))
        self.space_label.grid(row=2)

        self.temp_entry = tk.Entry(self.temp_frame, font=("Arial", "14"), highlightthickness=2)
        self.temp_entry.grid(row=3, padx=10, pady=5)

        self.error_label = tk.Label(self.temp_frame, text="", fg="#9C0000")
        self.error_label.grid(row=4, columnspan=2)

        self.button_frame = tk.Frame(self.temp_frame, pady=5)
        self.button_frame.grid(row=5)

        self.start_button = tk.Button(
            self.button_frame, text="Start", bg="#97D077", fg="#FFFFFF",
            font=("Arial", "12", "bold"), width=12, height=2, command=self.start_quiz
        )
        self.start_button.grid(row=0, column=0, padx=5)

        self.cancel_button = tk.Button(
            self.button_frame, text="Cancel", bg="#FF3333", fg="#FFFFFF",
            font=("Arial", "12", "bold"), width=12, height=2, command=self.root.destroy
        )
        self.cancel_button.grid(row=0, column=1, padx=5)

        # Bind the Enter key to start the quiz
        self.temp_entry.bind('<Return>', lambda event: self.start_quiz())

    def start_quiz(self):
        num_questions = self.temp_entry.get()

        # Check if the input is a natural number
        if not num_questions.isdigit():
            self.error_label.config(text="Please enter a natural number.")
            self.temp_entry.config(highlightbackground="#FF3333", highlightcolor="#FF3333")
            return

        # Convert the input to an integer and check if it's in range
        num_questions = int(num_questions)
        if num_questions < 5 or num_questions > 10:
            self.error_label.config(text=f"Number of questions must be between 5 and 10.")
            self.temp_entry.config(highlightbackground="#FF3333", highlightcolor="#FF3333")
            return

        # If the input is valid, reset the error label and highlight color
        self.error_label.config(text="")
        self.temp_entry.config(highlightbackground="#97D077", highlightcolor="#97D077")

        # Print the entered number of questions in the PyCharm console
        print(f"You have set {num_questions} questions for this quiz.")

    def clear_frame(self):
        for widget in self.temp_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    SimpleEntryApp()
