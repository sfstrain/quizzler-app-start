import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(300, 250)
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR,
            highlightthickness=0,
        )
        self.score_label = tk.Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.config(font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question Text",
            font=("Arial", 20, "italic"),
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(
            image=true_image,
            highlightthickness=0,
            width=96,
            height=94,
            relief="flat",
            command=self.true_clicked,
        )
        self.false_button = tk.Button(
            image=false_image,
            highlightthickness=0,
            width=96,
            height=94,
            relief="flat",
            command=self.false_clicked,
        )
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.display_question()

        self.window.mainloop()

    def update_score(self, new_score):
        self.score_label.config(text=f"Score: {new_score}")

    def display_question(self):
        self.canvas.config(bg="white")
        self.quiz_brain.next_question()
        if self.quiz_brain.current_question:
            q_number = self.quiz_brain.question_number
            q_text = f"Q{q_number}: {self.quiz_brain.current_question.text}"
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Final Score: {self.quiz_brain.score} / {self.quiz_brain.num_questions()}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        is_correct = self.quiz_brain.is_correct("true")
        if is_correct:
            self.update_score(self.quiz_brain.score)
        self.give_feedback(is_correct)

    def false_clicked(self):
        is_correct = self.quiz_brain.is_correct("false")
        if is_correct:
            self.update_score(self.quiz_brain.score)
        self.give_feedback(is_correct)

    def give_feedback(self, _correct):
        color = "green" if _correct else "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.display_question)
