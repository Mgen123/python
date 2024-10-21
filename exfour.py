import pyinputplus as pyip
import sqlite3
from datetime import datetime

print("\n\t\t\t\t Welcome to Gen'z Slambook! >V<")

def connect_db():
    return sqlite3.connect('example.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')  # Drop the table if it exists
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        birthday DATE NOT NULL,
        nickname TEXT NOT NULL,
        favorite_color TEXT,
        hobbies TEXT,
        favorite_food TEXT,
        favorite_movie TEXT,
        dream_destination TEXT,
        best_memory TEXT,
        one_wish TEXT,
        message_to_friends TEXT
    )
    ''')
    conn.commit()
    conn.close()

def create_user(firstname, lastname, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends):
    try:
        birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (firstname, lastname, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (firstname, lastname, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends))
    conn.commit()
    conn.close()

def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(user_id, firstname, lastname, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends):
    try:
        birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE users 
        SET firstname = ?, lastname = ?, birthday = ?, nickname = ?, favorite_color = ?, hobbies = ?, favorite_food = ?, favorite_movie = ?, dream_destination = ?, best_memory = ?, one_wish = ?, message_to_friends = ? 
        WHERE id = ?''', 
        (firstname, lastname, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def validate_name(name):
    if not name.isalpha():
        print("Invalid input. Please enter letters only.")
        return False
    return True

def get_valid_name(prompt):
    while True:
        name = pyip.inputStr(prompt)
        if validate_name(name):
            return name

def validate_birthday(birthday):
    try:
        datetime.strptime(birthday, '%Y-%m-%d')
        return True
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return False

def get_valid_birthday(prompt):
    while True:
        birthday = pyip.inputStr(prompt)
        if validate_birthday(birthday):
            return birthday

def validate_color(color):
    valid_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']
    return color.lower() in valid_colors

def get_valid_color(prompt):
    while True:
        color = pyip.inputStr(prompt)
        if validate_color(color):
            return color
        else:
            print("Invalid color. Please choose from the following options:", ', '.join(['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', 'White']))

def display_menu():
    print("\nWOULD YOU LIKE TO:")
    print("\t\t\t\t[1.] Add Record")
    print("\t\t\t\t[2.] Read Records")
    print("\t\t\t\t[3.] Update Record")
    print("\t\t\t\t[4.] Delete Record")
    print("\t\t\t\t[5.] Exit")

create_table()

while True:
    display_menu()
    choice = pyip.inputInt(prompt='Choose an option (1-5): ', min=1, max=5)

    if choice == 1:
        first_name = get_valid_name(prompt='First name: ')    
        last_name = get_valid_name(prompt='Last name: ')
        nickname = get_valid_name(prompt='Nickname: ')
        birthday = get_valid_birthday(prompt='Birthday (YYYY-MM-DD): ')
        
        favorite_color = get_valid_color(prompt='Favorite Color: ')
        
        hobbies = pyip.inputStr(prompt='Hobbies: ')
        favorite_food = pyip.inputStr(prompt='Favorite Food: ')
        favorite_movie = pyip.inputStr(prompt='Favorite Movie/Show: ')
        dream_destination = pyip.inputStr(prompt='Dream Destination: ')
        best_memory = pyip.inputStr(prompt='Best Memory: ')
        one_wish = pyip.inputStr(prompt='One Wish: ')
        message_to_friends = pyip.inputStr(prompt='Message to Friends: ')

        create_user(first_name, last_name, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends)
        print("Record has been added.")

    elif choice == 2:
        users = read_users()
        if users:
            print("\nCurrent Records:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]} {user[2]}, Nickname: {user[3]}, Birthday: {user[4]}, Favorite Color: {user[5]}, Hobbies: {user[6]}, Favorite Food: {user[7]}, Favorite Movie: {user[8]}, Dream Destination: {user[9]}, Best Memory: {user[10]}, One Wish: {user[11]}, Message to Friends: {user[12]}")
        else:
            print("No records found.")

    elif choice == 3:
        user_id = pyip.inputInt(prompt='Enter the ID of the record to update: ')
        users = read_users()
        if not any(user[0] == user_id for user in users):
            print("User not found.")
            continue
        
        first_name = get_valid_name(prompt='New First name: ')
        last_name = get_valid_name(prompt='New Last name: ') 
        nickname = get_valid_name(prompt='New Nickname: ')
        birthday = get_valid_birthday(prompt='New Birthday (YYYY-MM-DD): ')
        
        favorite_color = get_valid_color(prompt='New Favorite Color: ')
        
        hobbies = pyip.inputStr(prompt='New Hobbies: ')
        favorite_food = pyip.inputStr(prompt='New Favorite Food: ')
        favorite_movie = pyip.inputStr(prompt='New Favorite Movie/Show: ')
        dream_destination = pyip.inputStr(prompt='New Dream Destination: ')
        best_memory = pyip.inputStr(prompt='New Best Memory: ')
        one_wish = pyip.inputStr(prompt='New One Wish: ')
        message_to_friends = pyip.inputStr(prompt='New Message to Friends: ')

        update_user(user_id, first_name, last_name, birthday, nickname, favorite_color, hobbies, favorite_food, favorite_movie, dream_destination, best_memory, one_wish, message_to_friends)
        print("Record has been updated.")

    elif choice == 4:
        user_id = pyip.inputInt(prompt='Enter the ID of the record to delete: ')
        users = read_users()
        if not any(user[0] == user_id for user in users):
            print("User not found.")
            continue
        
        delete_user(user_id)
        print("Record has been deleted.")

    elif choice == 5:
        print("Exiting the program.")
        break
