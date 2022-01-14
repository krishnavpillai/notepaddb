# Delete Data
from userdata import UserData
import tkinter as tk

root = tk.Tk()


def delete():
    ud = UserData()
    index = ent1.get()
    if ud.delete_data(index):
        text = 'Deleted Successfully'
    else:
        text = 'Some Error'

    lbl2 = tk.Label(root, fg='#000', text=text, font=("Courier", 10))  # or font=('Helvetica 17 bold')
    lbl2.grid(row=6, column=3)


root.title('Delete Data')
root.geometry('350x200+0+0')

lbl1 = tk.Label(root, fg='#000', text='S.No', font=("Courier", 10))  # or font=('Helvetica 17 bold')
lbl1.grid(row=3, column=2)
ent1 = tk.Entry(root)
ent1.grid(row=3, column=4)

btn1 = tk.Button(root, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10, command=lambda: insert())
btn1.grid(row=5, column=3, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()