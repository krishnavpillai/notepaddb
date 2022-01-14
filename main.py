def main():
    ud = UserData()
    print('\n1. Insert a Data: ')
    print('2. View all record: ')
    print('3. Delete Specific record: ')
    print('4. Edit Specific record: ')
    print('5. Search Record: ')
    ch = input('\nEnter your Choice: ')
    if ch == '1':
        name = input('\nEnter the Name: ')
        email = input('\nEnter email: ')
        passw = input('\nEnter Password')

        if ud.insert_data([name, email, passw]):
            print('\nRecord Inserted')
        else:
            print('oops')

    elif ch == '2':

        if ud.fetch_data():
            data = ud.fetch_data()

            print('\nAll user Record\n')
            for index, item in enumerate(data):
                print('SL No: ' + str(index + 1))
                print('Name :' + item[0])
                print('Email' + item[1])
                print('Email' + item[2])
                print()
    elif ch == '3':
        index = (input('Enter S.No'))
        if ud.delete_data(index):
            print('Deleted Succesfully')

    elif ch == '4':
        index = (input('Enter S.No'))
        if ud.edit_data(index):
            print('Edited Succefully')
        else:
            print('OOPS')

    elif ch == '5':
        string = input("Enter String to be Searched: ")
        idn, data = ud.search_data(string)
        for index, item in zip(idn, data):
            print('SL No: ' + str(index))
            print('Name :' + item[0])
            print('Email' + item[1])
            print('Email' + item[2])
            print()


main()