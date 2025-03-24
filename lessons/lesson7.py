import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users.db')

# Рука, в которой есть ручка
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

connect.commit()

# CRUD операции: Create, Read, Update, Delete

'''CREATE'''
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# add_user('ARZYBEK', 23, 'Плавать')
# add_user('OLEG', 23, 'Плавать')
# add_user('VIKA', 23, 'Плавать')
# add_user('IGOR', 23, 'Плавать')


'''READ'''
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей")
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print("Пользователей нет!")

# get_all_users()

def get_user_by_id(rowid):
    cursor.execute('SELECT name, age, hobby FROM users WHERE rowid = ?', (rowid,))
    user = cursor.fetchone()

    if user:
        print(f"NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"Пользователь с ID {rowid} не найден!")

get_user_by_id(3)


'''UPDATE'''


def update_users(rowid, name=None, age=None, hobby=None):
    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if hobby is not None:
        fields.append("hobby = ?")
        values.append(hobby)

    if fields:
        values.append(rowid)
        query = f"UPDATE users SET {', '.join(fields)} WHERE rowid = ?"
        cursor.execute(query, values)
        connect.commit()
        print(f"Пользователь с rowid: {rowid} обновлён: {', '.join(fields)}")
    else:
        print("Нет данных для обновления!")

update_users(3, "Dmitry")


'''DELETE'''
def delete_user(name):
    cursor.execute('DELETE FROM users WHERE name = ?',
                   (name,))
    connect.commit()
    print('Пользователь удалён!')


# delete_user('VIKA')

get_all_users()
