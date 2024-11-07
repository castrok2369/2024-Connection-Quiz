from tkinter import *
from functools import partial

class ConnectionQuiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connection Quiz")

        # Frame for the end message and buttons
        self.end_frame = Frame(self.root, padx=10, pady=10)
        self.end_frame.grid()

        # End message
        self.end_message = Label(self.end_frame, text="Thank you for playing the Connection Quiz!",
                                 font=("Arial", "16", "bold"), wrap=250, justify="center")
        self.end_message.grid(row=0, pady=20)

        # Frame for the control buttons
        self.control_frame = Frame(self.end_frame)
        self.control_frame.grid(row=1, pady=10)

        # Start Over button (non-functional for this example)
        self.start_over_button = Button(self.control_frame, text="Start Over", bg="#FFA07A", fg="#FFFFFF",
                                        font=("Arial", "12", "bold"), width=15, height=2)
        self.start_over_button.grid(row=0, column=0, padx=5)

        # Help button (functional)
        self.help_button = Button(self.control_frame, text="Help", bg="#EA6B66", fg="#FFFFFF",
                                  font=("Arial", "12", "bold"), width=15, height=2, command=self.show_help)
        self.help_button.grid(row=0, column=1, padx=5)

        self.root.mainloop()

    def show_help(self):
        # Display the help window
        background = "#F8CECC"
        self.help_box = Toplevel()

        # Disable help button while help window is open
        self.help_button.config(state=DISABLED)

        # Re-enable help button when help window is closed
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help))

        # Help window frame
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        # Help window title
        self.help_heading_label = Label(self.help_frame, text="Help / Info", font=("Arial", "14", "bold"), bg=background)
        self.help_heading_label.grid(row=0, pady=(10, 5))

        # Help text
        help_text = (
            "During the quiz, you will be presented with incomplete compound words. "
            "Your task is to select the correct word from four options to complete the given phrase.\n\n"
            "After each answer, click the 'Next' button to proceed to the next question. "
            "Once you've answered all the questions, the quiz will automatically close. "
            "To exit at any point, you can press the 'Cancel' button on the main screen."
        )
        self.help_text_label = Label(self.help_frame, text=help_text, wraplength=350, justify="left", bg=background)
        self.help_text_label.grid(row=1, padx=10, pady=10)

        # Dismiss button to close the help window
        self.dismiss_button = Button(self.help_frame, text="Dismiss", font=("Arial", "12", "bold"), bg="#EA6B66",
                                     fg="#FFFFFF", command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self):
        # Re-enable the Help button and close the help window
        self.help_button.config(state=NORMAL)
        self.help_box.destroy()

if __name__ == "__main__":
    ConnectionQuiz()
