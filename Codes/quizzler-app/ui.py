import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text='smt',
                                                     font=("Arial", 15, "italic"),
                                                     fill=THEME_COLOR)
        # To add padding around the canvas, include padx and/or pady arguments in the canvas.grid() method.
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = tk.Label(text="Score: 0",fg='white',bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        true_image = tk.PhotoImage(file='images/true.png')
        self.true_button = tk.Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.press_true)
        self.true_button.grid(row=3, column=0)

        false_img = tk.PhotoImage(file='images/false.png')
        self.false_button = tk.Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.press_false)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Fin\nCheck the Score", font=("Arial", 25, "bold"))
            self.true_button.config(state=tk.DISABLED)
            self.false_button.config(state=tk.DISABLED)

    def press_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def press_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question)
