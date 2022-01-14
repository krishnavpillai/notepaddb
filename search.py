# Search Data
from userdata import UserData
import tkinter as tk
root = tk.Tk()

def search(index):
    ud = UserData()
    string = ent1.get()
    idn, data = ud.search_data(string)
    for index, item in zip(idn, data):
        print('SL No: ' + str(index))
        print('Name :' + item[0])
        print('Email' + item[1])
        print('Email' + item[2])
        print()


root.title('Search Data')
root.geometry('350x200+0+0')

lbl1 = tk.Label(root,fg='#000',text= 'Keyword',font=("Courier", 10)) # or font=('Helvetica 17 bold')
lbl1.grid(row=3,column=2)
ent1 = tk.Entry(root)
ent1.grid(row=3,column=4)


btn1 = tk.Button(root, bg='#00FFFF',fg='#A77D74',text='Search Data',width=10, command= lambda:insert())
btn1.grid(row=3,column=6,padx=5,pady=5,ipadx=5,ipady=5)

root.mainloop()