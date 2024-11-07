import csv
import re
from tkinter import *
from tkinter import messagebox
from functools import partial
import random
import os


class ConnectionQuiz:
    def __init__(self):
        self.all_quotes = []
        self.load_quotes()

        self.current_question_index = 0
        self.user_answers = []
        self.num_questions = 5  # Example number of questions
        self.past_scores = []

        self.root = Tk()
        self.root.title("Connection Quiz")

        self.temp_frame = Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        # Directly show results instead of starting the quiz
        self.show_results()

        self.root.mainloop()

    def load_quotes(self):
        try:
            with open("connections_quiz.csv", "r") as file:
                reader = csv.reader(file, delimiter=",")
                next(reader)  # skip the header
                for row in reader:
                    category = row[0]
                    words = row[1:5]
                    answer = row[5]
                    self.all_quotes.append({
                        "category": category,
                        "words": words,
                        "answer": answer
                    })
            self.questions = self.all_quotes
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'connections_quiz.csv' not found. Please ensure the file is in the correct directory.")
            self.root.destroy()

    def show_results(self):
        # Display hashtags as placeholders
        result_text = "You got # out of # questions correct."

        self.result_label = Label(self.temp_frame,
                                  text=result_text,
                                  font=("Arial", "14", "bold"), wrap=250, width=40, justify="center")
        self.result_label.grid(row=0, pady=20)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=1, pady=20)

        self.finish_button = Button(self.button_frame, text="Finish", bg="#6495ED", fg="#FFFFFF",
                                    font=("Arial", "12", "bold"), width=15, height=2, state=DISABLED)
        self.finish_button.grid(row=0, column=0, padx=5, pady=5)

        self.statistics_button = Button(self.button_frame, text="Statistics", bg="#97D077", fg="#FFFFFF",
                                        font=("Arial", "12", "bold"), width=15, height=2, state=DISABLED)
        self.statistics_button.grid(row=0, column=1, padx=5, pady=5)

        self.start_over_button = Button(self.button_frame, text="Start Over", bg="#FFA07A", fg="#FFFFFF",
                                        font=("Arial", "12", "bold"), width=15, height=2, state=DISABLED)
        self.start_over_button.grid(row=1, column=0, padx=5, pady=5)

        self.help_button = Button(self.button_frame, text="Help", bg="#EA6B66", fg="#FFFFFF",
                                  font=("Arial", "12", "bold"), width=15, height=2, command=self.show_help)
        self.help_button.grid(row=1, column=1, padx=5, pady=5)

    def show_help(self):
        DisplayHelp(self)


class DisplayHelp:
    def __init__(self, partner):
        background = "#F8CECC"
        self.help_box = Toplevel()

        partner.help_button.config(state=DISABLED)

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = ("During the quiz, you will be presented with incomplete compound words. "
                     "Your task is to select the correct word from four options to complete the given phrase.\n\n"
                     "After each answer, click the 'Next' button to proceed to the next question. "
                     "Once you've answered all the questions, the quiz will automatically close. "
                     "To exit at any point, you can press the 'Cancel' button on the main screen.")

        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#EA6B66",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    ConnectionQuiz()
