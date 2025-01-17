import sqlite3


def create_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')


def create_inx_db():
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_age ON Users (age)")


def add_users(user_list):
    cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?);", user_list)


def update_balance():
    for i in range(10):
        if (i + 1) % 2 != 0:
            cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{i + 1}"))


def del_records():
    step = 1
    while step <= 10:
        cursor.execute("DELETE FROM Users WHERE id = ?", (f"{step}",))
        step += 3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
customers = [(f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", 1000) for i in range(10)]
create_db()
create_inx_db()
add_users(customers)
update_balance()
del_records()

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


cursor.execute("DELETE FROM Users WHERE id='6';")


cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]


print(all_balances / total_users)

connection.commit()
connection.close()