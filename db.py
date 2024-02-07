import sqlite3

conn = sqlite3.connect("image_comparison.sqlite")

# cursor = conn.cursor()
# sql_query = """ CREATE TABLE book (
#     id integer PRIMARY KEY,
#     author text NOT NULL,
#     language text NOT NULL,
#     title text NOT NULL
# )"""
# cursor.execute(sql_query)

# sql_query = """ CREATE TABLE IF NOT EXISTS "users" (
# 	"id"	INTEGER,
# 	"username"	TEXT,
# 	"password"	TEXT,
# 	"userRole"	TEXT,
# 	"emailConfirmed"	NUMERIC DEFAULT 0,
# 	"createdAt"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )"""
# cursor.execute(sql_query)
