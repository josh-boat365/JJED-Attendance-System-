"""main function """

from flask import Flask, render_template, url_for,  request, redirect

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("intern_login.html")

@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html")

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/intern_home")
def intern_home():
        
    return render_template("intern_home.html")


if __name__ == "__main__":
    app.run(debug=True)

