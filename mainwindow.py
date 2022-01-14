# main window
import tkinter as tk
import insert
root = tk.Tk()


def insertwindow():
    newwin = tk.Toplevel(root)
    insert.Insert(newwin)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top",fill='both', expand='True')
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}
        for F in (StartPage,PageOne,PageTwo,PageThree):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column =0, sticky="nsew")
        self.show_frame(StartPage)
        self.title("Jumbo Jack Financial Consultants")

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


root.title('File Handling')
root.geometry('600x400+0+0')

btn1 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10, command=lambda: insertwindow)
btn1.grid(row=3, column=4, padx=5, pady=5, ipadx=5, ipady=5)
btn2 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Fetch All Data', width=10, command=lambda: fetchall())
btn2.grid(row=5, column=4, padx=5, pady=5, ipadx=5, ipady=5)
btn3 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10, command=lambda: delete())
btn3.grid(row=7, column=4, padx=5, pady=5, ipadx=5, ipady=5)
btn4 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Edit Data', width=10, command=lambda: edit())
btn4.grid(row=9, column=4, padx=5, pady=5, ipadx=5, ipady=5)
btn5 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Search Data', width=10, command=lambda: search())
btn5.grid(row=11, column=4, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()