import tkinter as tk
from tkinter import messagebox


questions = ["Hello! Can you please tell me your name?", "Do you live in America? If so, type yes!", "Are you anteater by the chance?", "Hm, I see! What do you prefer more sunflower seeds or corn?"]



class Application(tk.Frame):
    answers = []
    currentIndex = 0
        
    def __init__(self, master=None):
        
        
        super().__init__(master)
        self.pack()

        self.question = tk.Label(self, text=questions[0])
        self.question.pack(side="top")

        self.answer = tk.Entry(self)
        self.answer.pack(side="top")

        self.next = tk.Button(self, text="yas", command=self.nextQuestion)
        self.next.pack(side="bottom")

 

    def nextQuestion(self):
        self.answers.append(self.answer.get())
        self.currentIndex += 1
        if self.currentIndex == len(questions):
            for index, question in enumerate(questions):
                self.ending()
                root.quit()
        else:
            self.question["text"] = questions[self.currentIndex]
            self.answer.delete(0, tk.END)

    def ending(self):
        tk.messagebox.showinfo("Goodbye", "I reviewed all your answers, it seems like you are faggot!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

