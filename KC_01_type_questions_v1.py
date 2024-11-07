from tkinter import *
from tkinter import messagebox

class Converter:

    def __init__(self):
        # Initialise variables
        self.min_questions = 5
        self.max_questions = 10

        # Set up GUI Frame
        self.root = Tk()
        self.root.title("Connection Quiz")

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Connection Quiz",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        self.temp_instructions = Label(self.temp_frame,
                                       text="To begin, you must enter the number of questions you want the quiz to give you. \n\n" \
                                            "Then, you will be prompted to answer each question. Good luck!", \
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.space_label = Label(self.temp_frame, text="", font=("Arial", "8"))
        self.space_label.grid(row=2)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=3, padx=10, pady=5)

        self.error_label = Label(self.temp_frame, text="", fg="#9C0000")
        self.error_label.grid(row=4, columnspan=2)

        self.button_frame = Frame(self.temp_frame, pady=5)  # Adjusting padding here
        self.button_frame.grid(row=5)

        self.start_button = Button(self.button_frame,
                                  text="Start",
                                  bg="#97D077", fg="#FFFFFF",
                                  font=("Arial", "12", "bold"),
                                  width=12, height=2,
                                  command=self.dummy_function)  # Dummy function assigned
        self.start_button.grid(row=0, column=0, padx=5)

        self.cancel_button = Button(self.button_frame,
                                    text="Cancel",
                                    bg="#FF3333", fg="#FFFFFF",
                                    font=("Arial", "12", "bold"),
                                    width=12, height=2,
                                    command=self.root.destroy)
        self.cancel_button.grid(row=0, column=1, padx=5)

        self.root.mainloop()

    def dummy_function(self):
        # This function does nothing
        pass

    def start_conversion(self):
        num_questions = self.temp_entry.get()
        if not num_questions.isdigit():
            self.error_label.config(text="Please enter a valid number.")
            return

        num_questions = int(num_questions)
        if num_questions < self.min_questions or num_questions > self.max_questions:
            self.error_label.config(text="Number of questions must be between {} and {}.".format(self.min_questions, self.max_questions))
            return

        self.error_label.config(text="")
        messagebox.showinfo("Start Conversion", "Starting quiz with {} questions.".format(num_questions))
        # Add functionality to start the quiz with the desired number of questions here

# main routine
if __name__ == "__main__":
    Converter()
