# Fetch:
from userdata import UserData
import tkinter as tk
root = tk.Tk()

def fetch():
    ud = UserData()
    if ud.fetch_data():
        data = ud.fetch_data()

        print('\nAll user Record\n')
        for index,item in enumerate(data):
            print('SL No: ' +str(index+1))
            print('Name :' + item[0])
            print('Email'+item[1])
            print('Email'+item[2])
            print()

root.title('Fetch Data')
root.geometry('900x300+0+0')

btn1 = tk.Button(root, bg='#00FFFF',fg='#A77D74',text='Fetch Data',width=10, command= lambda:insert())
btn1.grid(row=1,column=3,padx=5,pady=5,ipadx=5,ipady=5)


root.mainloop()