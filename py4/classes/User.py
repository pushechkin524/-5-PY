from py4.database import Database
from py4.services import inp


class User:

    def __init__(self, db: Database):
        self.__id = ""
        self.__login = ""
        self.__password = ""
        self.__role = ""
        self.__db = db

    def authorize(self):
        work = True
        while work:
            login = inp("Логин: ", "str")
            password = inp("Пароль: ", "str")
            users = self.__db.readData("users", ["*"])
            logins = []
            for user in users:
                logins.append(user[1])
            if login in logins:
                index = logins.index(login)
                if users[index][2] == password:
                    self.__id = users[index][0]
                    self.__login = users[index][1]
                    self.__password = users[index][2]
                    self.__role = users[index][3]
                    break
                else:
                    print("Неправильный пароль")
            else:
                print("Неправильный логин")

    def registr(self):
        work = True
        print("Давайте зарегистрируемся")
        while work:
            login = inp("Логин: ", "str")
            password = inp("Пароль: ", "str")
            users = self.__db.readData("users", ["*"])
            logins = []
            for user in users:
                logins.append(user[1])
            if login in logins:
                print("Такой пользователь уже сущетсвует")
            else:
                data = {
                    "login": login,
                    "password": password,
                    "role": "buyer"
                }
                self.__db.insertData("users", data)
                print('Успешная регистрация')
                cash = inp("Введите Ваше количество денег для совершения покупок",
                           "int")
                args = {
                    "login": login
                }
                user = self.__db.readData("users", ["id"], args)
                self.__db.insertData("buyers", {"userId": user[0][0], "cash": cash})
                self.__id = user[0][0]
                self.__login = login
                self.__password = password
                self.__role = "buyer"
                break

    def get_role(self):
        return self.__role

    def get_id(self):
        return self.__id


