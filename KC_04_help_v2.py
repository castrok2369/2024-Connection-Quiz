from tkinter import *
from functools import partial
import csv
import random


class ChooseRounds:

    def __init__(self):
        # invoke play class with three rounds for testing purposes
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (ie: hide rounds choice windows).
        root.withdraw()


class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#EA6B66", "Help", "get help"],
            ["#97D077", "Results", "get stats"],  # Updated from "Statistics" to "Results"
            ["#FFA07A", "Start Over", "start over"]  # "Start Over" button will be visually enabled but non-functional
        ]

        # list to hold references for control buttons
        # so that the text of the 'start over' button
        # can easily be configured when the game is over
        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame,
                                              fg="#FFFFFF",
                                              bg=control_buttons[item][0],
                                              text=control_buttons[item][1],
                                              width=11, font=("Arial", "12", "bold"),
                                              command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

            # Add buttons to control list
            self.control_button_ref.append(self.make_control_button)

            self.to_help_btn = self.control_button_ref[0]

    def to_do(self, action):
        if action == "get help":
            DisplayHelp(self)
        elif action == "get stats":
            # You can implement functionality here for "Results" if needed
            pass
        elif action == "start over":
            # Intentionally do nothing to keep "Start Over" non-functional
            pass
        else:
            self.close_play()

    # DON'T USE THIS FUNCTION IN BASE AS IT KILLS THE ROOT
    def close_play(self):
        root.destroy()


# Show user help / game tips
class DisplayHelp:
    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#F8CECC"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_btn.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = ("During the quiz, you will be presented with incomplete compound words. "
                     "Your task is to select the correct word from four options to complete the given phrase.\n\n"
                     "After each answer, click the 'Next' button to proceed to the next question. "
                     "Once you've answered all the questions, the quiz will automatically close. "
                     "To exit at any point, you can press the 'Cancel' button on the main screen.")
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#EA6B66",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top pf dialogue)
    def close_help(self, partner):
        # Put help button back to normal...

        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Connection Quiz")
    ChooseRounds()
    root.mainloop()
