"""main function """

from flask import Flask, render_template, url_for,  request, redirect
import sqlite3



app = Flask(__name__)



def insert_list_data(mlist):
    connection = sqlite3.connect("jjed.db")
    cursor = connection.cursor()
    try:
        sql = """ INSERT INTO interns(intern_name, intern_school,intern_level,intern_contact,intern_email)VALUES(?,?,?,?,?)"""
        cursor.executemany(sql, mlist)
        connection.commit()
        print("commited")
    except connection.Error as error:
        print(error)
    finally:
        connection.close()

intern = [("Mary Dufie Afrane", "University of Cape Coast", "Level 300", "0558027244", "maryakua3@gmail.com"),
         ("Joshua Nyarko Boateng", "Accra Technical University", "Level 200", "0245553697", "joshua.goat19@gmail.com"),
          ("Enoch Sem", "University of Cape Coast", "Level 300", "0569775844", "enochsem@gmail.com"),
          ("jojo Sem", "University of Cape k", "Level 300", "0569765844", "jojosem@gmail.com"),
          ("Jojo ", "Ashesi University", "Level 300", "0558027244", "jojo@gmail.com")

           ]
# insert_list_data(intern)

def update_db():
    pass
# form_data = request.form()
# insert_list_data(form_data)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        connection = sqlite3.connect("jjed.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM interns WHERE intern_name=?", (name,))
        # cursor.execute(query)
        if cursor.fetchall():
            return redirect(url_for('intern_home'))
        else:
            return redirect(url_for('index'))
    return render_template("intern_login.html")


@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html")


@app.route("/admin_login", methods=["POST","GET"])
def admin_login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        connection = sqlite3.connect("jjed.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admins WHERE admin_name=? AND admin_password=?", (name,password,))
        # cursor.execute(query)
        if cursor.fetchall():
            return redirect(url_for('admin_home'))
        else:
            return redirect(url_for('admin_login'))

    return render_template("admin_login.html")

@app.route("/intern_home")
def intern_home():
        
    return render_template("intern_home.html")


if __name__ == "__main__":
    app.run(debug=True)

