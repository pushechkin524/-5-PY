import sqlite3


class Database:
    def __init__(self):
        self.connect = sqlite3.connect("shop.sql")
        self.cursor = self.connect.cursor()
        self.create_table()
        self.add_admin()

    def executeQuerry(self, query, value=None, read=None):
        try:
            with self.connect:
                if value:
                    if read:
                        return self.cursor.execute(query, value).fetchall()
                    self.cursor.execute(query, value)
                else:
                    if read:
                        return self.cursor.execute(query).fetchall()
                    self.cursor.execute(query)
        except Exception as e:
          pass
    def insertData(self, table, data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        querry = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.executeQuerry(querry, list(data.values()))

    def updateData(self, table, data, id):
        columns = ", ".join(f"{column} = ?" for column in data.keys())
        querry = f"UPDATE {table} SET {columns} WHERE id = ?"
        datalist = list(data.values())
        datalist.append(id)
        self.executeQuerry(querry, datalist)

    def deleteData(self, table, data):
        columns = ", ".join(f"{column} = ?" for column in data.keys())
        querry = f"DELETE FROM {table} WHERE {columns}"
        self.executeQuerry(querry, list(data.values()))

    def readData(self, table, data, data1=None):
        columns = ", ".join(data)
        query = ""
        if data1:
            args = ", ".join(f"{column} = ?" for column in data1)
            query = f"SELECT {columns} FROM {table} WHERE {args}"
            return self.executeQuerry(query, list(data1.values()), read=True)
        else:
            query = f"SELECT {columns} FROM {table}"
            return self.executeQuerry(query, read=True)

    def create_table(self):
        users = """Create table if not exists users(
        id integer not null primary key autoincrement,
        login varchar(20) not null unique,
        password varchar(20) not null,
        role varchar(20) not null
        );"""

        employess = """
        Create table if not exists employees(
        id integer not null primary key autoincrement,
        name varchar(20) not null,
        surname varchar(20) not null,
        patronymic varchar(20),
        userId integer,
        foreign key (userId) references users(id)
        );"""
        stock = """
        Create table if not exists stock(
        id integer not null primary key autoincrement,
        productName varchar(20) not null,
        price integer not null,
        quantity integer not null
        );"""
        transactions = """
        Create table if not exists transactions(
        id integer not null primary key autoincrement,
        productId integer not null,
        buyerId integer not null,
        sum integer not null,
        foreign key (productId) references stock(id),
        foreign key (buyerId) references buyers(id)
        ); 
        """

        buyers = """
        Create table if not exists buyers(
        id integer not null primary key autoincrement,
        userId integer not null,
        cash integer not null,
        foreign key (userId) references users(id)
        );
        """
        script = [users, employess, stock, buyers, transactions]
        with self.connect:
            for table in script:
                self.cursor.execute(table)

    def add_admin(self):
        self.insertData("users", {"login": "a", "password": "a", "role": "admin"})

