from tkinter import *

class ConnectionQuiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connection Quiz")

        # Frame for the results display
        self.temp_frame = Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        # Call the display_results method to show results with colored text
        self.display_results()

        self.root.mainloop()

    def display_results(self):
        # Display each question with "Correct" or "Incorrect" in colored text
        for i in range(5):  # Example loop for 5 question placeholders
            if i % 2 == 0:
                fg_color = "#86AB89"  # Green text for "Correct"
                result_text = "(Correct)"
            else:
                fg_color = "#C5705D"  # Red text for "Incorrect"
                result_text = "(Incorrect)"

            question_text = f"Q{i + 1}: (Sample question text) - Your answer: ____ {result_text}"
            result_label = Label(self.temp_frame,
                                 text=question_text,
                                 font=("Arial", "12"), fg=fg_color, anchor="w", justify="left")
            result_label.grid(row=i, sticky="w", pady=2)

        # Styled "Back to Main Menu" button
        back_button = Button(self.temp_frame, text="Back to Main Menu", bg="#97D077", fg="#FFFFFF",
                             font=("Arial", "12", "bold"), command=self.root.destroy)
        back_button.grid(row=5, pady=10)

if __name__ == "__main__":
    ConnectionQuiz()
