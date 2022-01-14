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

    def edit_data(self, id,name,email,passw):
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
