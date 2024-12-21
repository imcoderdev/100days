from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_Label=Label(text="score:0",fg="white",bg=THEME_COLOR,font=("Arial",14,"bold"))
        self.score_Label.grid(row=0,column=1)

        self.canvas= Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,text="some question will be displayed",width=280,fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan =2,pady=50)


        #buttons

        false_img = PhotoImage(file="images/false.png")
        self.button_false=Button(image=false_img,highlightthickness=0,command=self.false_pressed)
        self.button_false.grid(row=2,column=0)
        true_img = PhotoImage(file="images/true.png")
        self.button_true=Button(image=true_img,highlightthickness=0,command=self.true_pressed)
        self.button_true.grid(row=2,column=1)
        self.get_next_question()
        # self.give_feedback(self,is_right)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_Label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="your reached to the last of the quiz thanks for playing the quiz")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


