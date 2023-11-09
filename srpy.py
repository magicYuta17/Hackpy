import sqlite3


def create():
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, quantity INTEGER) """)
    conn.commit()
    conn.close()


def add_product():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    name = input("name=")
    price = input("price=")
    quantity = input("quantity=")
    cursor.execute('INSERT INTO product (name, price,quantity) VALUES (?,?,?)', (name, price, quantity))
    conn.commit()
    conn.close()


def get_data():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM product''')

    end = cursor.fetchone()
    print(end)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create()
add_product()
get_data()
