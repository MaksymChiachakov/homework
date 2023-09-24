import sqlite3
import random

# Підключаємось до нашої DB
conn = sqlite3.connect('DB.db')

# cursor - працює з запитами у DB
cursor = conn.cursor()

# Посилаємо -запит у DB
# score - потрібно нам для безпечного надсилання запитів
cursor.execute('''SELECT * FROM games''')

# Перетворення даних у список
data = cursor.fetchall()

# Виводимо рандомний елемент з нашого списку даних. Version 1:
random_game = random.choice(data)
print('Сьогодні пропонуємо вас зіграти у цю гру:', random_game)

# Виводимо рандомний елемент з нашого списку даних. Version 2:
random_index = random.randint(0, len(data) - 1)
print('Сьогодні пропонуємо вас зіграти у цю гру:', data[random_index])

# Виключаємо підключення до нашої DB, після цього, ми не зможемо надсилати запити до неї
conn.commit()