from tkinter import *

class ConnectionQuiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connection Quiz")

        # Frame for the results display
        self.temp_frame = Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        # Display basic placeholder results with no color coding
        self.display_results()

        self.root.mainloop()

    def display_results(self):
        for i in range(5):  # Example placeholder for 5 questions
            question_text = f"Q{i+1}: (Sample question text) - Your answer: ____"
            result_label = Label(self.temp_frame,
                                 text=question_text,
                                 font=("Arial", "12"), anchor="w", justify="left")
            result_label.grid(row=i, sticky="w", pady=2)

        # Simple "Back" button
        back_button = Button(self.temp_frame, text="Back to Quiz", font=("Arial", "12", "bold"), command=self.root.destroy)
        back_button.grid(row=5, pady=10)

if __name__ == "__main__":
    ConnectionQuiz()
