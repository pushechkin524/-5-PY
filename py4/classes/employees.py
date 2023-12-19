from py4.database import Database
from py4.services import inp


class Employee:

    def __init__(self, db: Database):
        self.__db = db

    def create_product(self):
        print("Давайте добавим новый продукт!")
        productName = inp("Введите название товара: ", "str", constraint=20)
        price = inp("Какова цена на товар: ", "int")
        quantity = inp("Какое количество товара: ", "int")
        args = {
            "productName": productName,
            "price": price,
            "quantity": quantity
        }
        self.__db.insertData("stock", args)
        print("Успешное добавление")

    def delete_product(self):
        print("Все продукты:")
        products = self.__db.readData("stock", ["*"])
        productsId = []
        if products:
            for product in products:
                productsId.append(product[0])
                print(f"ID: {product[0]}\n"
                      f"Товар: {product[1]}\n"
                      f"Цена: {product[2]}\n"
                      f"Количество: {product[3]}\n"
                      f"//////////////////////////\n")
            id = inp("Введитеid  товара: ", "int", productsId)
            self.__db.deleteData("stock", {"id": id})
            print("Успешное удаление")
        else:
            print("Пока что нет ни одного товара(")

    def update_product(self):
        print("Все продукты:")
        products = self.__db.readData("stock", ["*"])
        productsId = []
        if products:
            for product in products:
                productsId.append(product[0])
                print(f"ID: {product[0]}\n"
                      f"Товар: {product[1]}\n"
                      f"Цена: {product[2]}\n"
                      f"Количество: {product[3]}\n"
                      f"//////////////////////////\n")
            id = inp("Введитеid  товара: ", "int", productsId)
            action = inp("1 - название\n"
                         "2 - цена\n"
                         "3 - количество\n"
                         "Ваш выбор: ", "int", choices=[1, 2, 3])
            args = {}
            if action == 1:
                name = inp("Введите название: ", "str", constraint=20)
                args["productName"] = name
            elif action == 2:
                price = inp("Какова цена на товар: ", "int")
                args["price"] = price
            else:
                quantity = inp("Какое количество товара: ", "int")
                args["quantity"] = quantity
            self.__db.updateData("stock", args, id)
            print("Успешное изменение")
        else:
            print("Пока что нет ни одного товара(")



