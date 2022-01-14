from tkinter import messagebox
import tkinter as tk
import os
import re

class UserData():

    def __init__(self):
        self._filename = 'Database.txt'
        try:
            with open(self._filename, 'a+') as f:
                pass
        except:
            print("Unable to create backend file!")

    def insert_data(self, data):
        if not os.path.exists(self._filename):
            return False
        try:
            with open(self._filename, 'a+') as f:

                f.write(data[0])
                f.write("\n")
                f.write(data[1])
                f.write("\n")
                f.write(data[2])
                f.write("\n\n")
            return True
        except:
            return False
        return False

    def fetch_data(self):

        if not os.path.exists(self._filename):
            return False
        try:
            data = ""
            with open(self._filename) as f:
                data = f.read()

            user_data = data.split("\n\n")

            result = []

            for item in user_data[:-1]:
                record = item.split("\n")
                result.append((record[0], record[1], record[2]))
            return result
        except:
            return False

    def delete_data(self, id):
        if not self.fetch_data():
            return False
        data = self.fetch_data()
        del data[int(id) - 1]
        result_str = ''
        for item in data:
            tmp_str = '\n'.join(item)
            result_str += tmp_str
            result_str += '\n\n'
        try:
            with open(self._filename, 'w+') as f:
                f.write(result_str)

            return True
        except:
            return False

    def edit_data(self, id, name, email, passw):
        if not self.fetch_data():
            return False
        data = self.fetch_data()

        data_edited = (name, email, passw)
        data[int(id) - 1] = data_edited
        result_str = ''
        for item in data:
            tmp_str = '\n'.join(item)
            result_str += tmp_str
            result_str += '\n\n'
        try:
            with open(self._filename, 'w+') as f:
                f.write(result_str)

            return True
        except:
            return False

    def search_data(self, name, email):
        if not self.fetch_data():
            return False
        data = self.fetch_data()
        result = []
        idn = []
        index = 0
        for i in data:
            index += 1
            if len(name) != 0:
                if name in i[0]:
                    result.append(i)
                    idn.append(index)
            if len(email) != 0:
                if email in i[1]:
                    if i in result:
                        pass
                    else:
                        result.append(i)
                        idn.append(index)
        return idn, result

class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome to File Handling!')
        self.master.geometry('650x300+0+0')
        self.frame = tk.Frame(self.master)

        self.btn1 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10,
                      command=self.insert)
        self.btn1.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn2 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Fetch All Data', width=10,
                      command=self.fetch)
        self.btn2.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn3 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10,
                      command=self.delete)
        self.btn3.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn4 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Edit Data', width=10,
                      command=self.edit)
        self.btn4.grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn5 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Search Data', width=10,
                      command=self.search)
        self.btn5.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        ###################################################3
        # self.lbl1 = tk.Label(self.frame, fg='#000', text='Insert Data',
        #                      font=("Helvetica", 16))  # or font=('Helvetica 17 bold')
        # self.lbl1.grid(row=3, column=3)

        self.lbl2 = tk.Label(self.frame, fg='#000', text='Name', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl2.grid(row=3, column=2)
        self.ent2 = tk.Entry(self.frame)
        self.ent2.grid(row=3, column=3)

        self.lbl3 = tk.Label(self.frame, fg='#000', text='Email', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl3.grid(row=3, column=4)
        self.ent3 = tk.Entry(self.frame)
        self.ent3.grid(row=3, column=5)

        self.lbl4 = tk.Label(self.frame, fg='#000', text='Password',font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl4.grid(row=3, column=6)
        self.ent4 = tk.Entry(self.frame)
        self.ent4.grid(row=3, column=7)

        self.sb1 = tk.Scrollbar(self.frame, orient='vertical')
        self.sb1.grid(row=5, column=8, sticky='ns', rowspan=3)

        self.list1 = tk.Listbox(self.frame,  yscrollcommand=self.sb1.set,exportselection=False)
        self.list1.grid(row=5, column=2, rowspan=3, columnspan=6, sticky='nsew',padx=5, pady=5, ipadx=5, ipady=5)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)
        ######################################################

        self.frame.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    def get_selected_row(self,event):
        global selected_tuple
        index = self.list1.curselection()[0]
        selected_tuple = self.list1.get(index)
        matchobj = re.search('Name :(.+)\s+Email :(.+)\s+Password :(.+)', selected_tuple)
        iname = (matchobj.group(1))
        iemail = (matchobj.group(2))
        ipassw = (matchobj.group(3))
        self.ent2.delete(0, tk.END)
        self.ent2.insert(tk.END, iname)
        self.ent3.delete(0, tk.END)
        self.ent3.insert(tk.END, iemail)
        self.ent4.delete(0, tk.END)
        self.ent4.insert(tk.END, ipassw)
        #END, LEFT, and BOTH all reside in the tkinter namespace. Thus, they need to be qualified by placing tk. before them:

    def insert(self):
        try:
            self.lbl5.destroy()
            self.lbl6.destroy()
            self.lbl7.destroy()
        except:
            pass
        ud = UserData()
        dict1 = {}
        name = dict1['name'] = self.ent2.get().strip()
        email = dict1['email'] = self.ent3.get().strip()
        passw = dict1['passw'] = self.ent4.get().strip()
        list2 = []
        if len(dict1['name']) == 0 or len(dict1['email']) == 0 or len(dict1['passw']) == 0 :
            for i in dict1:
                if len(dict1[i]) == 0:
                    list2.append(i)
            messagebox.showinfo("Caution", f"Box should not be empty {list2} ")
        else:
            if __name__=='__main__':

                if ud.insert_data([name, email, passw]):
                    #         print('\nRecord Inserted')

                    # self.btn6 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Close Window', width=10,
                    #                       command=self.close_windows)
                    # self.btn6.grid(row=11, column=5, padx=5, pady=5, ipadx=5, ipady=5)
                    self.ent2.delete(0, tk.END)
                    self.ent3.delete(0, tk.END)
                    self.ent4.delete(0, tk.END)
                    self.ent2.focus_set()
                    self.fetch()
                    self.lbl5 = tk.Label(self.frame, fg='#000', text='Inserted',
                                 font=("Courier", 10))  # or font=('Helvetica 17 bold')
                    self.lbl5.grid(row=8, column=2)
                else:
                    print('oops')
            else:
                pass

    def fetch(self):
        try:
            self.lbl5.destroy()
            self.lbl6.destroy()
            self.lbl7.destroy()
        except:
            pass
        ud = UserData()
        data = ud.fetch_data()
        self.list1.delete(0, tk.END)
        for index, item in enumerate(data):
            string = 'SL No: ' + str(index + 1) + '   Name :' + item[0] + '   Email :' + item[1] + '   Password :' + item[2]
            self.list1.insert(tk.END,string )
        self.lbl5 = tk.Label(self.frame, fg='#000', text='Fetched',
                             font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl5.grid(row=8, column=2)


    def delete(self):
        ud = UserData()
        try:
            self.lbl5.destroy()
            self.lbl6.destroy()
            self.lbl7.destroy()
        except:
            pass
        try:
            index = int(self.list1.curselection()[0]) + 1
            if ud.delete_data(index):

                self.ent2.delete(0, tk.END)
                self.ent3.delete(0, tk.END)
                self.ent4.delete(0, tk.END)
                self.fetch()
                self.lbl5 = tk.Label(self.frame, fg='#000', text='Deleted',
                                     font=("Courier", 10))  # or font=('Helvetica 17 bold')
                self.lbl5.grid(row=8, column=2)
                self.ent2.focus_set()
        except:
            messagebox.showinfo('Caution', "Select The Cursor ")



    def edit(self):
        ud = UserData()
        dict1 = {}
        try:
            self.lbl5.destroy()
            self.lbl6.destroy()
            self.lbl7.destroy()
        except:
            pass

        try:
            index = int(self.list1.curselection()[0]) + 1
        except:
            messagebox.showinfo('Caution',"Select The Cursor ")
        name = dict1['name'] = self.ent2.get().strip()
        email = dict1['email'] = self.ent3.get().strip()
        passw = dict1['passw'] = self.ent4.get().strip()
        list2 = []
        if len(dict1['name']) == 0 or len(dict1['email']) == 0 or len(dict1['passw']) == 0 :
            for i in dict1:
                if len(dict1[i]) == 0:
                    list2.append(i)
            messagebox.showinfo("Caution", f"Box should not be empty {list2} ")
        else:
                if ud.edit_data(index,name, email, passw):
                    #         print('\nRecord Inserted')

                    # self.btn6 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Close Window', width=10,
                    #                       command=self.close_windows)
                    # self.btn6.grid(row=11, column=5, padx=5, pady=5, ipadx=5, ipady=5)
                    self.ent2.delete(0, tk.END)
                    self.ent3.delete(0, tk.END)
                    self.ent4.delete(0, tk.END)
                    self.fetch()
                    self.lbl5 = tk.Label(self.frame, fg='#000', text='Edited',
                                 font=("Courier", 10))  # or font=('Helvetica 17 bold')
                    self.lbl5.grid(row=8, column=2)
                    self.ent2.focus_set()
                else:
                    print('oops')


    def search(self):
        try:
            self.lbl5.destroy()
            self.lbl6.destroy()
            self.lbl7.destroy()
        except:
            pass
        ud = UserData()
        dict1 = {}
        list2 = []
        name = dict1['name'] = self.ent2.get().strip()
        email = dict1['email'] = self.ent3.get().strip()
        idn, data = ud.search_data(name,email)
        if len(dict1['name']) == 0 and len(dict1['email']) == 0 :
            messagebox.showinfo("Caution", f"Box should not be empty Name or Email ")

        else:
            self.list1.delete(0, tk.END)

            for index, item in zip(idn, data):
                string = 'SL No: ' + str(index + 1) + '   Name :' + item[0] + '   Email :' + item[1] + '   Password :' +item[2]
                self.list1.insert(tk.END, string)
            self.lbl5 = tk.Label(self.frame, fg='#000', text='Searched',
                                 font=("Courier", 10))  # or font=('Helvetica 17 bold')
            self.lbl5.grid(row=8, column=2)
            if len(name) != 0:
                self.lbl6 = tk.Label(self.frame, fg='#000', text='Name :'+str(name),
                                     font=("Courier", 10))  # or font=('Helvetica 17 bold')
                self.lbl6.grid(row=8, column=3)
            if len(email) != 0:
                self.lbl7 = tk.Label(self.frame, fg='#000', text='Email :'+str(email),
                                     font=("Courier", 10))  # or font=('Helvetica 17 bold')
                self.lbl7.grid(row=8, column=4)


def main():
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()