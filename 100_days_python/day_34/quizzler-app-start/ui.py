from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz:QuizBrain):
        self.quiz_list = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_label = Label(text="Score : 0")
        self.score_label.config( fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Hello", font=("Arial", 20, "italic"), width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # self.canvas.config(padx=50, pady=50)

        self.file_path = "D:/python/100_days_python/day_34/quizzler-app-start/images" 
        self.true_file_path = PhotoImage(file=f"{self.file_path}/true.png")
        self. wrong_image_path = PhotoImage(file=f"{self.file_path}/false.png")

        self.green_btn = Button(image=self.true_file_path, highlightthickness=0, command=self.right_ans)
        # self.green_btn.config(pady=40,bg=THEME_COLOR)
        self.green_btn.grid(row=2, column=0)

        self.wrong_btn = Button(image=self.wrong_image_path, highlightthickness=0, command=self.wrong_ans)
        self.wrong_btn.grid(row=2, column=1)
        
        self.get_quiz()
        self.canvas.config(bg="white")
        self.window.mainloop()

    def get_quiz(self):
        self.canvas.config(bg="white")
        if self.quiz_list.still_has_questions():            
            self.score_label.config(text=f"Score : {self.quiz_list.score}")
            quiz_text = self.quiz_list.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the list.")
            self.green_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def right_ans(self):
        result = self.quiz_list.check_answer("True")
        self.give_feedback(result)

    def wrong_ans(self):
        result = self.quiz_list.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red") 
        self.window.after(1000,self.get_quiz)
           