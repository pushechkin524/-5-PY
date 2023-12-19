from py4.services import inp
from py4.database import Database


class Buyer:
    def __init__(self, id, db: Database):
        self.__id = id
        self.__db = db

    def buy(self):
        print("Все продукты:")
        products = self.__db.readData("stock", ["*"])
        productsQuantity = {}
        productsPrices = {}
        if products:
            for product in products:
                productsQuantity[product[0]] = product[3]
                productsPrices[product[0]] = product[2]
                print(f"ID: {product[0]}\n"
                      f"Товар: {product[1]}\n"
                      f"Цена: {product[2]}\n"
                      f"//////////////////////////\n")
            id = inp("Введитеid  товарадля покупки: ", "int", list(productsQuantity.keys()))
            quantity = None
            while quantity == None:
                try:
                    amount = int(input("Введите количество товара: ").strip())
                    if amount > productsQuantity[id]:
                        print(f"К сожалению у нас только {productsQuantity[id]} шт."
                              f"данного товара(")
                    else:
                        quantity = amount
                except:
                    print("Укажите числовое значение")
            sum = productsPrices[id] * quantity
            print(f"Общая сумма покупки: {sum}")
            print("Вы согласны?")
            action = inp("1 - да\n"
                         "2 - нет\n"
                         "Выбор: ", "int", choices=[1, 2])
            if action == 1:
                record = self.__db.readData("buyers", ["id, cash"], {"userId": self.__id})
                if record[0][1] > sum:
                    buyerCash = record[0][1] - sum
                    self.__db.updateData("buyers", {"cash": buyerCash}, record[0][0])
                    transaction = {
                        "productId": id,
                        "sum": sum,
                        "buyerId": record[0][0]
                    }
                    self.__db.insertData("transactions", transaction)
                    print("Успешная покупка")
                else:
                    print("Вам не хватает денег\n"
                          f"Ваши деньги: {record[0][1]}\n"
                          f"Сумма покупки: {sum}")

        else:
            print("Пока что в нашем магазине пусто(")

    def add_cash(self):
        cash = inp("Какое количество денег Вы хотите добавить: ", "int")
        buyer = self.__db.readData("buyers", ["id", "cash"], {"userId": self.__id})
        cash += buyer[0][1]
        self.__db.updateData("buyers", {"cash": cash}, buyer[0][0])

    def get_cash(self):
        return self.__db.readData("buyers", ["cash"], {"userId": self.__id})[0][0]