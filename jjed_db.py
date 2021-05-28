import sqlite3

connection = sqlite3.connect("jjed.db")
cursor = connection.cursor()

try:
    create_intern_table = """CREATE TABLE IF NOT EXISTS interns(
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_name TEXT NOT NULL, 
	intern_school TEXT NOT NULL,
	intern_level TEXT NOT NULL,
	intern_contact TEXT NOT NULL,
	intern_email TEXT NOT NULL
    )"""

    create_admin_table = """CREATE TABLE IF NOT EXISTS admins(
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        admin_name TEXT NOT NULL, 
        admin_email TEXT NOT NULL,
        admin_password TEXT NOT NULL
    )"""

    create_activity_table = """CREATE TABLE IF NOT EXISTS activities(
        activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_title TEXT NOT NULL,
        activity_content TEXT NOT NULL,
        activity_datetime DATETIME GETDATE
    )"""

    create_attendance_table = """CREATE TABLE IF NOT EXISTS attandance(
        attendance_bool TEXT NOT NULL,
        attendance_datetime DATETIME GETDATE,
        intern_id INTEGER PRIMARY KEY,
        FOREIGN KEY (intern_id)
        REFERENCES interns (intern_id) 
        ON UPDATE CASCADE
        ON DELETE CASCADE
    )"""
    cursor.execute(create_intern_table)
    connection.commit()
    cursor.execute(create_admin_table)
    connection.commit()
    cursor.execute(create_activity_table)
    connection.commit()
    cursor.execute(create_attendance_table)
    connection.commit()
except connection.Error as error:
    print("debug print",error)
finally:
    if connection:
        connection.close()


sql = """ INSERT INTO interns(intern_name, intern_school,intern_level,intern_contact,intern_email)VALUES(?,?,?,?,?)"""

def insert_list_data(mlist,sql):
    connection = sqlite3.connect("jjed.db")
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, mlist)
        connection.commit()
        print("commited")
    except connection.Error as error:
        print(error)
    finally:
        connection.close()

        
intern = [("mery", "University of Cape Coast", "Level 300", "0558027244", "maryakua3@gmail.com"),
         ("joshuA", "Accra Technical University", "Level 200", "0245553697", "joshua.goat19@gmail.com"),
          ("sem", "University of Cape Coast", "Level 300", "0569775844", "enochsem@gmail.com"),
          ("Eem", "University of Cape k", "Level 300", "0569765844", "jojosem@gmail.com"),
          ("Jojo", "Ashesi University", "Level 300", "0558027244", "jojo@gmail.com")
           ]

admin = [("admin", "email@admin.com", "1234"),
         ("admin1", "email@admin1.com", "12345"),
           ]
#insert_list_data(intern,sql)
sql1 = """ INSERT INTO admins(admin_name, admin_email,admin_password)VALUES(?,?,?)"""
insert_list_data(admin,sql1)