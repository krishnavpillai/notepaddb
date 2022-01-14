import os
from tkinter import *
from tkinter import messagebox


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


class AllPages(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill='both', expand='True')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, InsertPage, DeletePage, EditPage, ViewAllPage,SearchPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        self.title("Jumbo Jack Financial Consultants")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # title('File Handling')
        # geometry('600x400+0+0')

        btn1 = Button(self, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10,
                      command=lambda: controller.show_frame(InsertPage))
        btn1.grid(row=3, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        btn2 = Button(self, bg='#00FFFF', fg='#A77D74', text='Fetch All Data', width=10,
                      command=lambda: controller.show_frame(ViewAllPage))
        btn2.grid(row=5, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        btn3 = Button(self, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10,
                      command=lambda: controller.show_frame(DeletePage))
        btn3.grid(row=7, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        btn4 = Button(self, bg='#00FFFF', fg='#A77D74', text='Edit Data', width=10,
                      command=lambda: controller.show_frame(EditPage))
        btn4.grid(row=9, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        btn5 = Button(self, bg='#00FFFF', fg='#A77D74', text='Search Data', width=10,
                      command=lambda: controller.show_frame(SearchPage))
        btn5.grid(row=11, column=4, padx=5, pady=5, ipadx=5, ipady=5)

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4)

        # list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.bind('<<ListboxSelect>>', get_selected_row)

        def get_selected_row(event):
            global selected_tuple
            index = list1.curselection()[0]
            selected_tuple = list1.get(index)
            e1.delete(0, END)
            e1.insert(END, selected_tuple[1])
            e2.delete(0, END)
            e2.insert(END, selected_tuple[2])
            # e3.delete(0, END)
            # e3.insert(END, selected_tuple[3])
            e4.delete(0, END)
            e4.insert(END, selected_tuple[4])
            e5.delete(0, END)
            e5.insert(END, selected_tuple[5])
            e6.delete(0, END)
            e6.insert(END, selected_tuple[6])


class InsertPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # title('Insert Data')
        # geometry('350x200+0+0')

        lbl1 = Label(self, fg='#000', text='Insert Data', font=("Helvetica", 16))  # or font=('Helvetica 17 bold')
        lbl1.grid(row=3, column=3)

        lbl2 = Label(self, fg='#000', text='Name', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl2.grid(row=5, column=2)
        ent2 = Entry(self)
        ent2.grid(row=5, column=4)

        lbl3 = Label(self, fg='#000', text='Email', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl3.grid(row=7, column=2)
        ent3 = Entry(self)
        ent3.grid(row=7, column=4)

        lbl4 = Label(self, fg='#000', text='Password', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl4.grid(row=9, column=2)
        ent4 = Entry(self)
        ent4.grid(row=9, column=4)

        btn5 = Button(self, bg='#00FFFF', fg='#A77D74', text='Insert Data', width=10, command=lambda: insert())
        btn5.grid(row=11, column=3, padx=5, pady=5, ipadx=5, ipady=5)

        btn6 = Button(self, bg='#00FFFF', fg='#A77D74', text='Home', width=10,
                      command=lambda: controller.show_frame(StartPage))
        btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        def insert():
            ud = UserData()

            name = ent2.get()
            email = ent3.get()
            passw = ent4.get()
            if ud.insert_data([name, email, passw]):
                #         print('\nRecord Inserted')
                lbl2 = Label(self, fg='#000', text='Data Inserted Succesfully',
                             font=("Courier", 10))  # or font=('Helvetica 17 bold')
                lbl2.grid(row=12, column=3)
            else:
                print('oops')


class DeletePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        lbl1 = Label(self, fg='#000', text='S.No', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl1.grid(row=3, column=2)
        ent1 = Entry(self)
        ent1.grid(row=3, column=4)

        btn1 = Button(self, bg='#00FFFF', fg='#A77D74', text='Delete Data', width=10, command=lambda: delete())
        btn1.grid(row=5, column=4, padx=5, pady=5, ipadx=5, ipady=5)

        btn6 = Button(self, bg='#00FFFF', fg='#A77D74', text='Home', width=10,
                      command=lambda: controller.show_frame(StartPage))
        btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)


class EditPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        lbl1 = Label(self, fg='#000', text='S.No Data', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl1.grid(row=3, column=2)
        ent1 = Entry(self)
        ent1.grid(row=3, column=4)

        lbl2 = Label(self, fg='#000', text='Name', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl2.grid(row=5, column=2)
        ent2 = Entry(self)
        ent2.grid(row=5, column=4)

        lbl3 = Label(self, fg='#000', text='Email', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl3.grid(row=7, column=2)
        ent3 = Entry(self)
        ent3.grid(row=7, column=4)

        lbl4 = Label(self, fg='#000', text='Password', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl4.grid(row=9, column=2)
        ent4 = Entry(self)
        ent4.grid(row=9, column=4)

        btn5 = Button(self, bg='#00FFFF', fg='#A77D74', text='Edit Data', width=10, command=lambda: insert())
        btn5.grid(row=11, column=3, padx=5, pady=5, ipadx=5, ipady=5)

        btn6 = Button(self, bg='#00FFFF', fg='#A77D74', text='Home', width=10,
                      command=lambda: controller.show_frame(StartPage))
        btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)


class ViewAllPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        btn6 = Button(self, bg='#00FFFF', fg='#A77D74', text='Home', width=10,
                      command=lambda: controller.show_frame(StartPage))
        btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4, sticky='nsew')

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)


class SearchPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        btn6 = Button(self, bg='#00FFFF', fg='#A77D74', text='Home', width=10,
                      command=lambda: controller.show_frame(StartPage))
        btn6.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        lbl1 = Label(self, fg='#000', text='Keyword', font=("Courier", 10))  # or font=('Helvetica 17 bold')
        lbl1.grid(row=3, column=2)
        ent1 = Entry(self)
        ent1.grid(row=3, column=4)

        btn1 = Button(self, bg='#00FFFF', fg='#A77D74', text='Search Data', width=10,
                      command=lambda: search(ent1.get()))
        btn1.grid(row=3, column=6, padx=5, pady=5, ipadx=5, ipady=5)

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


app = AllPages()
app.mainloop()
