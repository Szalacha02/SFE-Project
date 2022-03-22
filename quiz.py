from tkinter import *
from tkinter import messagebox as mb
import json
class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.q_number = len(question)
        self.right = 0
    def display_result(self):
        wrong_count = self.q_number - self.right
        correct = f"Correct: {self.right}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.right / self.q_number * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True
    def next_btn(self):
        if self.check_ans(self.q_no):
            self.right += 1
        self.q_no += 1
        if self.q_no == self.q_number:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
    def prev_btn(self):
        self.q_no -= 1
        if self.q_no == self.q_number:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=20, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=1000, y=850)
        previous_button = Button(gui, text = "Previous", command=self.prev_btn,
                            width = 20, bg="blue", fg="white", font=("ariel", 16, "bold"))
        previous_button.place(x = 450, y= 850)
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=1800, y=50)
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1
    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=100,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(gui, text="QuizMaster",
                      width=120, bg="red", fg="white", font=("ariel", 24, "bold"))
        title.place(x=-265, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list
gui = Tk()
gui.geometry("1920x1080")
gui.title("QuizMaster")
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()
gui.mainloop()
