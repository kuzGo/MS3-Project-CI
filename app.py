import os
from flask import (
    Flask, flash, redirect,
    render_template, request, url_for, session)
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_login import login_required, login_user, logout_user
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
        return redirect(url_for(
            "welcome", username=session["client"]))

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
                flash("Welcome, {},you are logged in.".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "welcome", username=session["client"]))

            else:
                flash("Password and/or username you entered is inncorect")
                return redirect(url_for("login"))
        else:
            flash("Password and/or username you entered is inncorect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/welcome/<username>", methods=["GET", "POST"])
def welcome(username):

    username = mongo.db.users.find_one(
        {"username": session["client"]})

    return render_template("welcome.html", username=username)


@app.route("/logout")
def logout():
    flash("You're sucessfully logged out")
    session.pop('client')
    return redirect(url_for("login"))


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        activity = {
            "category_type": request.form.get("category_type"),
            "activity_name": request.form.get("activity_name"),
            "activity_outcome": request.form.get("activity_outcome"),
            "description": request.form.get("description"),
            "necessities": request.form.get("necessities"),
            "image_url": request.form.get("image_url"),
            "uploaded_by": session["client"]
        }
        mongo.db.activities.insert_one(activity)
        flash("Activity has been uploaded.")
        return redirect(url_for("get_activities"))
    categories = mongo.db.catogories.find().sort('category_type', 1)
    return render_template("upload.html", categories=categories)


@app.route("/update_activity/<activity_id>", methods=["GET", "POST"])
def update_activity(activity_id):
    if request.method == 'POST':
        update = {
            "category_type": request.form.get("category_type"),
            "activity_name": request.form.get("activity_name"),
            "activity_outcome": request.form.get("activity_outcome"),
            "description": request.form.get("description"),
            "necessities": request.form.get("necessities"),
            "image_url": request.form.get("image_url"),
            "uploaded_by": session["client"]
        }
        mongo.db.activities.update({"_id": ObjectId(activity_id)}, update)
        flash("Activity has been updated.")

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    categories = mongo.db.catogories.find().sort('category_type', 1)
    return render_template(
        "update.html", activity=activity, categories=categories)


@app.route("/remove_activity/<activity_id>")
def remove_activity(activity_id):
    mongo.db.activities.remove({"_id": ObjectId(activity_id)})
    flash("Activity has been deleted.")
    return redirect(url_for("get_activities"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # As a reminder , change debug to False before submission
            debug=True)
