import os
from flask import (
    Flask, flash, redirect,
    render_template, request, url_for, session)
from flask_pymongo import PyMongo
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_activities")
def get_activities():
    activities = mongo.db.activities.find()
    return render_template("activities.html", activities=activities)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            flash(
                "This username is already exists,try different username")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get(
                    "password"), method='pbkdf2:sha256', salt_length=16)
        }

        mongo.db.users.insert_one(register)

        session["client"] = request.form.get("username").lower()
        flash("You're sucessfuly registered")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if registered_user:
            if check_password_hash(
                    registered_user["password"], request.form.get("password")):
                session["client"] = request.form.get("username")
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_activities"))

            else:
                flash("Password and/or username you entered is inncorect")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You're sucessfully logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/upload")
def upload():
    categories = mongo.db.catogories.find().sort('category_type',1)
    return render_template("upload.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # As a reminder , change debug to False before submission
            debug=True)
