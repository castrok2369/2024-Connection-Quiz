import csv
from tkinter import *
from tkinter import messagebox
from functools import partial
import random


class ConnectionQuiz:
    def __init__(self):
        self.all_quotes = []
        self.load_quotes()

        self.current_question_index = 0
        self.user_answers = []
        self.num_questions = 0
        self.past_scores = []
        self.choice_states = []  # Store the state of choices and their order

        self.current_score = 0  # Track the current score

        self.root = Tk()
        self.root.title("Connection Quiz")

        self.temp_frame = Frame(self.root, padx=10, pady=10)
        self.temp_frame.grid()

        self.setup_start_screen()

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

    def setup_start_screen(self):
        # Clear the frame
        self.clear_frame()

        # Set up the initial screen to enter the number of questions
        self.temp_heading = Label(self.temp_frame, text="Connection Quiz", font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        self.temp_instructions = Label(self.temp_frame,
                                       text="To begin, you must enter the number of questions you want the quiz to give you. \n\n"
                                            "Then, you will be prompted to answer each question. Good luck!",
                                       wrap=250, width=40, justify="left")
        self.temp_instructions.grid(row=1)

        self.space_label = Label(self.temp_frame, text="", font=("Arial", "8"))
        self.space_label.grid(row=2)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"), highlightthickness=2)
        self.temp_entry.grid(row=3, padx=10, pady=5)

        self.error_label = Label(self.temp_frame, text="", fg="#9C0000")
        self.error_label.grid(row=4, columnspan=2)

        self.button_frame = Frame(self.temp_frame, pady=5)
        self.button_frame.grid(row=5)

        self.start_button = Button(self.button_frame, text="Start", bg="#97D077", fg="#FFFFFF",
                                   font=("Arial", "12", "bold"), width=12, height=2, command=self.start_quiz)
        self.start_button.grid(row=0, column=0, padx=5)

        self.cancel_button = Button(self.button_frame, text="Cancel", bg="#FF3333", fg="#FFFFFF",
                                    font=("Arial", "12", "bold"), width=12, height=2, command=self.root.destroy)
        self.cancel_button.grid(row=0, column=1, padx=5)

        # Bind the Enter key to start the quiz
        self.temp_entry.bind('<Return>', lambda event: self.start_quiz())

    def start_quiz(self):
        num_questions = self.temp_entry.get()
        if not num_questions.isdigit():
            self.error_label.config(text="Please enter a natural number.")
            self.temp_entry.config(highlightbackground="#FF3333", highlightcolor="#FF3333")
            return
        num_questions = int(num_questions)
        if num_questions < 5 or num_questions > 10:
            self.error_label.config(text=f"Number of questions must be between 5 and 10.")
            self.temp_entry.config(highlightbackground="#FF3333", highlightcolor="#FF3333")
            return

        self.num_questions = num_questions
        self.error_label.config(text="")
        self.temp_entry.config(highlightbackground="#97D077", highlightcolor="#97D077")
        random.shuffle(self.questions)
        self.questions = self.questions[:self.num_questions]
        self.current_question_index = 0
        self.user_answers = []
        self.choice_states = []  # Reset choice states for new quiz
        self.current_score = 0  # Reset score at the start
        self.show_question()

    def show_question(self):
        if self.current_question_index < self.num_questions:
            self.clear_frame()

            # Question heading
            self.question_heading = Label(self.temp_frame,
                                          text=f"Question {self.current_question_index + 1} of {self.num_questions}",
                                          font=("Arial", "14", "bold"))
            self.question_heading.grid(row=0, pady=10)

            # Scoring label with enhanced visibility
            self.score_label = Label(self.temp_frame, text=f"Score: {self.current_score}",
                                     font=("Arial", "14", "bold"), bg="#BB9AB1", fg="#000000", padx=10, pady=5)
            self.score_label.grid(row=1, pady=10)

            # Instructions
            self.instructions_label = Label(self.temp_frame,
                                            text="Select the correct word to complete each of the given compound ones. Each question has four options—choose carefully!",
                                            font=("Arial", "12"), wrap=250, width=40, justify="center")
            self.instructions_label.grid(row=2, pady=(10, 20))

            # Category label placed above the words
            question_data = self.questions[self.current_question_index]
            category = question_data['category']

            self.category_label = Label(self.temp_frame, text=f"Category: {category}", font=("Arial", "14", "bold"), justify="center")
            self.category_label.grid(row=3, pady=(5, 10))

            # Display each word in its own box
            words_frame = Frame(self.temp_frame)
            words_frame.grid(row=4, pady=10)

            for word in question_data['words']:
                word_frame = Frame(words_frame, highlightbackground="#000000", highlightthickness=1, padx=5, pady=5)
                word_frame.pack(side=LEFT, padx=5)
                word_label = Label(word_frame, text=word, font=("Arial", "14"), justify="center")
                word_label.pack()

            # Generate and display options
            options = self.generate_options(question_data['answer'])

            # Store the current state of choices (before shuffling)
            if len(self.choice_states) <= self.current_question_index:
                self.choice_states.append(options.copy())

            # Shuffle options if it's a new question and not coming back from results
            if len(self.user_answers) <= self.current_question_index:
                random.shuffle(options)
                self.choice_states[self.current_question_index] = options.copy()

            self.answer_var = StringVar()

            # Options frame for buttons, arranged in a 2x2 grid
            self.options_frame = Frame(self.temp_frame)
            self.options_frame.grid(row=5, pady=10)

            self.option_buttons = []
            colors = ['#97D077', '#FFA07A', '#6495ED', '#FFD700']
            for i, option in enumerate(self.choice_states[self.current_question_index]):
                option_button = Button(self.options_frame, text=option, font=("Arial", "12", "bold"), width=15,
                                       height=2, command=lambda opt=option: self.check_answer(opt),
                                       bg=colors[i], fg="#000000", relief="raised", bd=2)
                # Arrange buttons in a 2x2 grid
                row = i // 2
                column = i % 2
                option_button.grid(row=row, column=column, padx=10, pady=5)
                option_button.config(cursor="hand2", borderwidth=1, highlightthickness=0)
                option_button.config(borderwidth=2, relief="groove")
                self.option_buttons.append(option_button)

            # If the user already answered this question, show the result
            if len(self.user_answers) > self.current_question_index:
                self.show_selected_answer()

        else:
            self.clear_frame()
            self.show_end_dialogue()

    def generate_options(self, correct_answer):
        all_answers = [q['answer'] for q in self.questions]
        all_answers.remove(correct_answer)
        options = random.sample(all_answers, 3) + [correct_answer]
        return options

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question_index]['answer']

        if selected_answer == correct_answer:
            self.current_score += 1  # Increase score if the answer is correct
            for button in self.option_buttons:
                if button['text'] == selected_answer:
                    button.config(bg="#86AB89", fg="#FFFFFF")  # Solid green with white text
                else:
                    button.config(state=DISABLED, bg="#D3D3D3", fg="#FFFFFF")  # Disable and grey out other buttons
        else:
            for button in self.option_buttons:
                if button['text'] == selected_answer:
                    button.config(bg="#C5705D", fg="#FFFFFF")  # Solid red with white text
                elif button['text'] == correct_answer:
                    button.config(bg="#86AB89", fg="#FFFFFF")  # Solid green with white text
                else:
                    button.config(state=DISABLED, bg="#D3D3D3", fg="#FFFFFF")  # Disable and grey out other buttons

        # Disable all buttons after an answer is selected
        for button in self.option_buttons:
            button.config(state=DISABLED)

        # Store the user's answer
        if len(self.user_answers) <= self.current_question_index:
            self.user_answers.append(selected_answer)
        else:
            self.user_answers[self.current_question_index] = selected_answer

        # Update the score label after each question
        self.score_label.config(text=f"Score: {self.current_score}")

        # Show the "Next" button after selecting an answer
        self.show_next_button()

        # Show the "Finish" and "Results" buttons during the quiz
        self.show_quiz_controls()

    def show_selected_answer(self):
        selected_answer = self.user_answers[self.current_question_index]
        correct_answer = self.questions[self.current_question_index]['answer']

        for button in self.option_buttons:
            if button['text'] == selected_answer:
                if selected_answer == correct_answer:
                    button.config(bg="#86AB89", fg="#FFFFFF")  # Solid green with white text
                else:
                    button.config(bg="#C5705D", fg="#FFFFFF")  # Solid red with white text
            elif button['text'] == correct_answer:
                button.config(bg="#86AB89", fg="#FFFFFF")  # Solid green with white text
            else:
                button.config(state=DISABLED, bg="#D3D3D3", fg="#FFFFFF")  # Disable and grey out other buttons

        # Disable all buttons after returning to the quiz
        for button in self.option_buttons:
            button.config(state=DISABLED)

    def show_next_button(self):
        next_button = Button(self.temp_frame, text="Next", bg="#686D76", fg="#FFFFFF",
                             font=("Arial", "10", "bold"), width=10, height=1, command=self.next_question)
        next_button.grid(row=6, pady=10)

    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def show_quiz_controls(self):
        # Frame for Finish and Results buttons
        quiz_controls_frame = Frame(self.temp_frame)
        quiz_controls_frame.grid(row=7, pady=10)

        # Finish button to end the quiz early
        self.finish_button = Button(quiz_controls_frame, text="Finish", bg="#6495ED", fg="#FFFFFF",
                                    font=("Arial", "12", "bold"), width=12, height=2, command=self.show_end_dialogue)
        self.finish_button.grid(row=0, column=0, padx=5)

        # Results button to show the results at any time
        self.results_button = Button(quiz_controls_frame, text="Results", bg="#97D077", fg="#FFFFFF",
                                     font=("Arial", "12", "bold"), width=12, height=2, command=self.display_results)
        self.results_button.grid(row=0, column=1, padx=5)

    def display_results(self):
        self.clear_frame()

        # Display each question and whether the user got it right or wrong
        for i, question in enumerate(self.questions[:len(self.user_answers)]):  # Display only answered questions
            question_text = ' '.join(question['words'])
            correct_answer = question['answer']
            user_answer = self.user_answers[i]

            if user_answer.lower() == correct_answer.lower():
                result = "Correct"
                color = "#86AB89"  # Solid green color
                fg_color = "#FFFFFF"  # White text
            else:
                result = "Incorrect"
                color = "#C5705D"  # Solid red color
                fg_color = "#FFFFFF"  # White text

            result_label = Label(self.temp_frame,
                                 text=f"Q{i+1}: {question_text} - Your answer: {user_answer} ({result})",
                                 font=("Arial", "12"), fg=fg_color, bg=color, anchor="w", justify="left")
            result_label.grid(row=i, sticky="w", pady=2)

        # Add a button to go back to the quiz
        back_button = Button(self.temp_frame, text="Back to Quiz", bg="#97D077", fg="#FFFFFF",
                             font=("Arial", "12", "bold"), command=self.back_to_quiz)
        back_button.grid(row=len(self.questions[:len(self.user_answers)]) + 1, pady=10)

    def back_to_quiz(self):
        self.clear_frame()
        self.show_current_question_results()  # Show current question result but prevent answer changes
        self.show_next_button()  # Ensure the "Next" button appears
        self.show_quiz_controls()  # Ensure the "Finish" and "Results" buttons reappear

    def show_current_question_results(self):
        # Re-display the question with the previous answer highlighted, and only allow proceeding to the next question
        self.show_question()

    def show_end_dialogue(self):
        self.clear_frame()

        end_message = Label(self.temp_frame,
                            text="Thank you for playing the Connection Quiz!",
                            font=("Arial", "16", "bold"), wrap=250, justify="center")
        end_message.grid(row=0, pady=20)

        # Frame for Start Over and Help buttons
        end_button_frame = Frame(self.temp_frame)
        end_button_frame.grid(row=1, pady=10)

        self.start_over_button = Button(end_button_frame, text="Start Over", bg="#FFA07A", fg="#FFFFFF",
                                        font=("Arial", "12", "bold"), width=15, height=2, command=self.restart_quiz)
        self.start_over_button.grid(row=0, column=0, padx=5)

        self.help_button = Button(end_button_frame, text="Help", bg="#EA6B66", fg="#FFFFFF",
                                  font=("Arial", "12", "bold"), width=15, height=2, command=self.show_help)
        self.help_button.grid(row=0, column=1, padx=5)

    def restart_quiz(self):
        self.clear_frame()
        self.reset_quiz()
        self.setup_start_screen()  # Return to the initial screen instead of starting the quiz directly

    def reset_quiz(self):
        self.current_question_index = 0
        self.user_answers = []
        self.choice_states = []  # Reset choice states
        self.num_questions = 0
        self.current_score = 0

    def clear_frame(self):
        for widget in self.temp_frame.winfo_children():
            widget.destroy()

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

        # Updated help text
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
