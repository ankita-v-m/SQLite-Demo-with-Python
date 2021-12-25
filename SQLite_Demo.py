import sqlite3                  

# 1. Connect to a database
# 2. Create a cursor object     - Cursor object is like a pointer to actually access rows from a table for database
# 3. Apply an SQL query
# 4. Commit your changes to the database
# 5. Close the connection

def create_table():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows                 # rows is returned as a list

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()               # Commit changes to database
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()               # Commit changes to database
    conn.close()


# delete("Wine Glass")

# update(20,10,"Water Glass")

print(view())
# insert("Coffee Glass",17,9)





