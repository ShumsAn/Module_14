import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    );
    ''')
    connection.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products

def is_included(username):
    """Проверка пользователя на присутствие в базе"""
    check_user = cursor.execute('SELECT username FROM Users WHERE username = ?',(f'{username}',))
    if check_user.fetchone() is None:
        return False
    else:
        return True
def add_user(username, email, age):
    """Функция Добавления пользователя"""
    if is_included(username):
        print("Пользователь Существует")
    else:
        cursor.execute("INSERT INTO Users (username, email,age,balance) VALUES (?,?,?,?)",
                       (username, email, age,1000))
        connection.commit()

def add_product(title,description,price):
    """Функция добавления продуктов"""
    cursor.execute("INSERT INTO Products (title, description,price) VALUES (?,?,?)",
                   (title, description,price))

    connection.commit()



