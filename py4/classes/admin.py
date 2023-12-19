from py4.database import Database
from py4.services import inp


class Admin:

    def __init__(self, db: Database):
        self.__db = db

    def create_employee(self):
        print("Давайте добавим нового сотрудника")
        name = inp("Введите имя: ", "str", constraint=20)
        surname = inp("Введите фамилию: ", "str", constraint=20)
        patronymic = input("Введите отчество(при наличии)").strip()
        args = {
            "name": name,
            "surname": surname,
            "patronymic": patronymic,
        }
        self.__db.insertData("employees", args)
        print("Теперь установим данные для входа работника")
        userId = None
        while userId == None:
            login = inp("Придумайте логин: ", "str")
            password = inp("Придумайте пароль: ", "str")
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
                    "role": "employee"
                }
                self.__db.insertData("users", data)
                print('Успешная регистрация')
                userArgs = {
                    "login": login
                }
                user = self.__db.readData("users", ["id"], userArgs)
                userId = user[0][0]
                break
        employee = self.__db.readData("employees", ["id"], {"name": name})
        self.__db.updateData("employees", {"userId": userId}, employee[0][0])
        print("Успешное добавление сотрудника")

    def delete_employee(self):
        print("Все работники:")
        employees = self.__db.readData("employees", ["*"])
        employeesId = []
        if employees:
            for employee in employees:
                employeesId.append(employee[0])
                print(f"ID: {employee[0]}\n"
                      f"Имя: {employee[1]}\n"
                      f"Фамилия: {employee[2]}\n"
                      f"Отчество: {employee[3]}\n"
                      f"userId: {employee[4]}\n"
                      f"////////////////////")
            id = inp("Введите id: ", "int", choices=employeesId)
            user = self.__db.readData("employees", ["userId"], {"id": id})
            self.__db.deleteData("users", {"id": user[0][0]})
            self.__db.deleteData("employees", {"id": id})
            print("Успешное удаление")
        else:
            print("Пока что нет ни одного работника")

    def update_employee(self):
        print("Все работники:")
        employees = self.__db.readData("employees", ["*"])
        employeesId = []
        if employees:
            for employee in employees:
                employeesId.append(employee[0])
                print(f"ID: {employee[0]}\n"
                      f"Имя: {employee[1]}\n"
                      f"Фамилия: {employee[2]}\n"
                      f"Отчество: {employee[3]}\n"
                      f"userId: {employee[4]}\n"
                      f"////////////////////")
            id = inp("Введите id: ", "int", choices=employeesId)
            action = inp("1 - имя\n"
                         "2 - фамилия\n"
                         "3 - отчество\n"
                         "Ваш выбор: ", "int", choices=[1, 2, 3])
            args = {}
            if action == 1:
                name = inp("Введите имя: ", "str", constraint=20)
                args["name"] = name
            elif action == 2:
                surname = inp("Введите фамилию: ", "str", constraint=20)
                args["surname"] = surname
            else:
                patronymic = input("Введите отчество(при наличии)").strip()
                args["patronymic"] = patronymic
            self.__db.updateData("employees", args, id)
            print("Успешное изменение")
        else:
            print("Пока что нет ни одного работника")

