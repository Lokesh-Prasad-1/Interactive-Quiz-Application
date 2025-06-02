from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: ", padx=5, pady=5, fg="white", bg=THEME_COLOR,
                                 font=("Helvetica", 15, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Hello",
                                                     fill=THEME_COLOR,
                                                     font=("Helvetica", 15, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        True_Image = PhotoImage(file="images/true.png")
        False_Image = PhotoImage(file="images/false.png")

        self.True_button = Button(image=True_Image, highlightthickness=0, command=self.true_pressed)
        self.True_button.grid(row=2, column=0)

        self.False_button = Button(image=False_Image, highlightthickness=0, command=self.false_pressed)
        self.False_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="THANK YOU FOR PLAYING")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)






