from tkinter import *

class ConnectionQuiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connection Quiz")

        # Frame for the results display
        self.temp_frame = Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        # Call the display_results method to show a blank template
        self.display_results()

        self.root.mainloop()

    def display_results(self):
        # Display placeholders instead of actual questions and answers
        for i in range(5):  # Example loop for 5 questions
            question_text = "Q{}: (Sample question text) - Your answer: ____ (_____)".format(i + 1)
            result_label = Label(self.temp_frame,
                                 text=question_text,
                                 font=("Arial", "12"), bg="#E0E0E0", fg="#000000", anchor="w", justify="left")
            result_label.grid(row=i, sticky="w", pady=2)

        # Styled "Back to Quiz" button to close the application
        back_button = Button(self.temp_frame, text="Back to Quiz", bg="#97D077", fg="#FFFFFF",
                             font=("Arial", "12", "bold"), command=self.root.destroy)
        back_button.grid(row=5, pady=10)

if __name__ == "__main__":
    ConnectionQuiz()
