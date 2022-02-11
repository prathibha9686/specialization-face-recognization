import sqlite3  
  
con = sqlite3.connect("emp.db")  
print("Database opened successfully")  
  
con.execute("create table Employees(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,gender TEXT NOT NULL, department TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  
