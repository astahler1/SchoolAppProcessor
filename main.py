import tkinter as tk

class SchoolAppProcessor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('School App Processor')
        self.geometry('400x200')
        label = tk.Label(self, text='Welcome to SchoolAppProcessor!')
        label.pack(pady=40)

if __name__ == '__main__':
    app = SchoolAppProcessor()
    app.mainloop()
