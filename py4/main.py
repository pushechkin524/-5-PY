from database import Database
from classes import User
from py4.classes import Employee, Buyer, Admin
from services import inp


def main():
    db = Database()
    user = User(db)
    employee = Employee(db)
    admin = Admin(db)
    while True:
        print("Приветствуем в нашем магазине!")
        action = inp("1 - войти\n"
                     "2 - зарегистрироваться\n"
                     "3 - выйти\n"
                     "Действие: ", "int", choices=[1, 2, 3])
        if action == 1:
            user.authorize()
        elif action == 2:
            user.registr()
        else:
            break
        role = user.get_role()
        if role == "admin":
            while True:
                query = ("1 - действия с работниками\n"
                         "2 - действия с товарами\n"
                         "3 - выйти\n"
                         "Действие: ")
                response  = inp(query, "int", [1, 2, 3])
                if response == 1:
                    query = ("1 - добавить работника\n"
                             "2 - изменить работника\n"
                             "3 - удалить работника\n"
                             "Действие: ")
                    response = inp(query, "int", [1, 2, 3])
                    if response == 1:
                        admin.create_employee()
                    elif response == 2:
                        admin.update_employee()
                    else:
                        admin.delete_employee()
                elif response == 2:
                    query = ("1 - добавить товар\n"
                             "2 - изменить товар\n"
                             "3 - удалить товар\n"
                             "Действие: ")
                    response = inp(query, "int", [1, 2, 3])
                    if response == 1:
                        employee.create_product()
                    elif response == 2:
                        employee.update_product()
                    else:
                        employee.delete_product()
                else:
                    break
        elif role == "employee":
            while True:
                query = ("1 - добавить товар\n"
                         "2 - изменить товар\n"
                         "3 - удалить товар\n"
                         "4 - выйти\n"
                         "Действие: ")
                response = inp(query, "int", [1, 2, 3, 4])
                if response == 1:
                    employee.create_product()
                elif response == 2:
                    employee.update_product()
                elif response == 3:
                    employee.delete_product()
                else:
                    break
        else:
            buyer = Buyer(user.get_id(), db)
            while True:
                print(f"Ваши деньги: {buyer.get_cash()}")
                query = ("1 - купить товар\n"
                         "2 - добавить денег в кошелек\n"
                         "3 - выйти\n"
                         "Действие: ")
                response = inp(query, "int", [1, 2, 3])
                if response == 1:
                    buyer.buy()
                elif response == 2:
                    buyer.add_cash()
                else:
                    break



if __name__ == "__main__":
    main()