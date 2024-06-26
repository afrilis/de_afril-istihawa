import requests
import mysql.connector

# Mengambil data dari API
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
data = response.json()

# Mengkoneksikan ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="etl_db"
)

# Menyimpan data ke database
cursor = db.cursor()
for post in data:
    cursor.execute("""
        INSERT INTO posts (user_id, title, body)
        VALUES (%s, %s, %s)
    """, (post["userId"], post["title"], post["body"]))

db.commit()
cursor.close()
db.close()

print("Data berhasil disimpan ke database!")
