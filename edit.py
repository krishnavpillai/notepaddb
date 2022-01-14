# Edit Data
from userdata import UserData
import tkinter as tk
root = tk.Tk()

root.title('Insert Data')
root.geometry('350x200+0+0')

def edit():
    ud = UserData()
    index = ent1.get()
    name  = ent2.get()
    email = ent3.get()
    passw = ent4.get()
    if ud.edit_data(index,name,email,passw):
        print('Edited Succefully')
    else:
        print('OOPS')

lbl1 = tk.Label(root,fg='#000',text= 'S.No Data',font=("Courier", 10)) # or font=('Helvetica 17 bold')
lbl1.grid(row=3,column=2)
ent1 = tk.Entry(root)
ent1.grid(row=3,column=4)

lbl2 = tk.Label(root,fg='#000',text= 'Name',font=("Courier", 10)) # or font=('Helvetica 17 bold')
lbl2.grid(row=5,column=2)
ent2 = tk.Entry(root)
ent2.grid(row=5,column=4)

lbl3 = tk.Label(root,fg='#000',text= 'Email',font=("Courier", 10)) # or font=('Helvetica 17 bold')
lbl3.grid(row=7,column=2)
ent3 = tk.Entry(root)
ent3.grid(row=7,column=4)

lbl4 = tk.Label(root,fg='#000',text= 'Password',font=("Courier", 10)) # or font=('Helvetica 17 bold')
lbl4.grid(row=9,column=2)
ent4 = tk.Entry(root)
ent4.grid(row=9,column=4)

btn5 = tk.Button(root, bg='#00FFFF',fg='#A77D74',text='Edit Data',width=10, command= lambda:insert())
btn5.grid(row=11,column=3,padx=5,pady=5,ipadx=5,ipady=5)

root.mainloop()