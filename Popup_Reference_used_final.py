import tkinter as tk
import os

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

    def search_data(self, string):
        if not self.fetch_data():
            return False
        data = self.fetch_data()
        result = []
        idn = []
        index = 0
        for i in data:
            index += 1
            if string in i:
                result.append(i)
                idn.append(index)
            else:
                for j in i:
                    if string in j:
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
        self.master.geometry('350x400+0+0')
        self.frame = tk.Frame(self.master)

        self.btn1 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10,
                      command=self.insert)
        self.btn1.grid(row=3, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn2 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Fetch All Data', width=10,
                      command=self.fetch)
        self.btn2.grid(row=5, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn3 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10,
                      command=self.delete)
        self.btn3.grid(row=7, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn4 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Edit Data', width=10,
                      command=self.edit)
        self.btn4.grid(row=9, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        self.btn5 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Search Data', width=10,
                      command=self.search)
        self.btn5.grid(row=11, column=4, padx=5, pady=5, ipadx=5, ipady=5)

        self.frame.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    def insert(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = InsertPage(self.newWindow)

    def fetch(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = FetchPage(self.newWindow)

    def delete(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = DeletePage(self.newWindow)

    def edit(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = EditPage(self.newWindow)

    def search(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SearchPage(self.newWindow)

class InsertPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Insert Data')
        # self.master.geometry('350x200+0+0')
        self.frame = tk.Frame(self.master)

        self.lbl1 = tk.Label(self.frame, fg='#000', text='Insert Data', font=("Helvetica", 16))  # or font=('Helvetica 17 bold')
        self.lbl1.grid(row=3, column=3)

        self.lbl2 = tk.Label(self.frame, fg='#000', text='Name', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl2.grid(row=5, column=2)
        self.ent2 = tk.Entry(self.frame)
        self.ent2.grid(row=5, column=4)

        self.lbl3 = tk.Label(self.frame, fg='#000', text='Email', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl3.grid(row=7, column=2)
        self.ent3 = tk.Entry(self.frame)
        self.ent3.grid(row=7, column=4)

        self.lbl4 = tk.Label(self.frame, fg='#000', text='Password', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        self.lbl4.grid(row=9, column=2)
        self.ent4 = tk.Entry(self.frame)
        self.ent4.grid(row=9, column=4)

        self.btn5 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10, command=self.insert)
        self.btn5.grid(row=11, column=3, padx=5, pady=5, ipadx=5, ipady=5)



        self.frame.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)



    def insert(self):
        ud = UserData()

        name = self.ent2.get()
        email = self.ent3.get()
        passw = self.ent4.get()
        if ud.insert_data([name, email, passw]):
            #         print('\nRecord Inserted')
            self.lbl2 = tk.Label(self.frame, fg='#000', text='Data Inserted Succesfully',
                         font=("Courier", 10))  # or font=('Helvetica 17 bold')
            self.lbl2.grid(row=12, column=3)
            self.btn6 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='Close Window', width=10,
                                  command=self.close_windows)
            self.btn6.grid(row=11, column=5, padx=5, pady=5, ipadx=5, ipady=5)
            self.ent2.delete(0, 50)
            self.ent3.delete(0, 50)
            self.ent4.delete(0, 50)
            self.ent2.focus_set()

        else:
            print('oops')


    def close_windows(self):
        self.master.destroy()

class FetchPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Insert Data')
        # self.master.geometry('350x200+0+0')
        self.frame = tk.Frame(self.master)
        self.btn6 = tk.Button(self.frame, bg='#00FFFF', fg='#A77D74', text='View All', width=10,
                      command=self.view_command)
        self.btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.listbox.bind('<<ListboxSelect>>', get_selected_row)
        self.frame.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        # sb1 = tk.Scrollbar(self, orient='vertical')
        # sb1.grid(row=4, column=4, sticky='ns', rowspan=6)
        #
        # list1 = tk.Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        # list1.grid(row=4, column=0, rowspan=6, columnspan=4, sticky='nsew')
        #
        # list1.configure(yscrollcommand=sb1.set)
        # sb1.configure(command=list1.yview)

    def view_command(self):
        ud = UserData()
        data = ud.fetch_data()
        for index, item in enumerate(data):
            # print('SL No: ' + str(index + 1))
            # print('Name :' + item[0])
            # print('Email' + item[1])
            # print('Email' + item[2])
            # print()
            self.listbox.insert(tk.END, 'SL No: ' + str(index + 1))
            self.listbox.insert(tk.END, 'Name :' + item[0])
            self.listbox.insert(tk.END, 'Email :' + item[1])
            self.listbox.insert(tk.END, 'Password :' + item[2])


    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()