import os
from flask import (
    Flask, flash, redirect,
    render_template, request, url_for, session)
from flask_pymongo import PyMongo
from bson import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'client' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to be logged in to proceed.")
            return redirect(url_for("login"))
    return wrap


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_activities")
@login_required
def get_activities():
    activities = list(mongo.db.activities.find())
    return render_template("activities.html", activities=activities)


@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    query = request.form.get("query")
    activities = list(mongo.db.activities.find({"$text": {"$search": query}}))
    return render_template("activities.html", activities=activities)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            flash(
                "This username is already in use.Try different username")
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
                session["client"] = request.form.get("username").lower()
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
        {"username": session["client"]})['username']

    if session['client']:
        uploads = list(mongo.db.activities.find().sort("_id", 1))
        return render_template(
            "welcome.html", username=username, uploads=uploads)

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    flash("You're sucessfully logged out")
    session.pop('client')
    return redirect(url_for("login"))


@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        existing_activity = mongo.db.activities.find_one(
            {"activity_name": request.form.get("activity_name").lower()})

        if existing_activity is None:
            activtivity = {
                "category_type": request.form.get("category_type"),
                "activity_name": request.form.get("activity_name"),
                "activity_outcome": request.form.get("activity_outcome"),
                "description": request.form.get("description"),
                "necessities": request.form.get("necessities"),
                "image_url": request.form.get("image_url"),
                "uploaded_by": session["client"]
            }
            mongo.db.activities.insert_one(activtivity)
            flash("Activity has been uploaded.")
            return redirect(url_for("get_activities"))

    categories = mongo.db.catogories.find().sort('category_type', 1)
    return render_template("upload.html", categories=categories)


@app.route("/update_activity/<activity_id>", methods=["GET", "POST"])
def update_activity(activity_id):
    """
    Updating activities is restricted to user currently logged in,
    or Admin user.
    """
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    current_user = session["client"] == activity["uploaded_by"]

    if session["client"] == 'admin' or current_user:

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
        activity = mongo.db.activities.find_one(
            {"_id": ObjectId(activity_id)})
        categories = mongo.db.catogories.find().sort('category_type', 1)
        return render_template(
            "update.html", activity=activity, categories=categories)
    else:
        flash("Updating others activities is not allowed.")
        return redirect(url_for("get_activities"))


@app.route("/remove_activity/<activity_id>")
def remove_activity(activity_id):
    """
    Deleting activities is restricted to user currently logged in,
    or Admin user.
    """

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    current_user = session["client"] == activity["uploaded_by"]

    if session["client"] == 'admin' or current_user:

        mongo.db.activities.remove({"_id": ObjectId(activity_id)})
        flash("Activity has been deleted.")
        return redirect(url_for("get_activities"))
    else:
        flash("Deleting activities is not allowed.")
        return redirect(url_for("get_activities"))


@app.route("/admin_page")
@login_required
def admin_page():
    if session["client"] == 'admin':
        categories = list(
            mongo.db.catogories.find().sort("category_type", 1))
        return render_template("admin.html", categories=categories)
    else:
        flash("Sorry, you don't have admin rights.")
        return redirect(url_for("get_activities"))


@app.route("/new_category", methods=["GET", "POST"])
@login_required
def new_category():
    if session["client"] == 'admin':

        if request.method == 'POST':
            current_category = mongo.db.catogories.find_one(
                {"category_type": request.form.get("category_name")})
            new_categories = {
                'category_type': request.form.get("category_name")
            }
            if current_category:
                flash("This category already exists,try different.")
                return redirect("new_category")
            mongo.db.catogories.insert_one(new_categories)
            flash("New category added.")
            return redirect(url_for("admin_page"))

    return render_template("category.html")


@app.route("/category_edit/<category_id>", methods=["GET", "POST"])
@login_required
def category_edit(category_id):
    if session["client"] == 'admin':
        if request.method == "POST":
            edit = {
                "category_type": request.form.get("category_name")
            }
            mongo.db.catogories.update({"_id": ObjectId(category_id)}, edit)
            flash("Activity category updated successfully.")
            return redirect(url_for("admin_page"))
        category = mongo.db.catogories.find_one({"_id": ObjectId(category_id)})
    return render_template("category_edit.html", category=category)


@app.route("/remove_category/<category_id>")
@login_required
def remove_category(category_id):
    if session["client"] == 'admin':

        mongo.db.catogories.remove({"_id": ObjectId(category_id)})
        flash("Activity category deleted successfully.")
        return redirect(url_for("admin_page"))
    else:
        flash("Sorry, you don't have admin rights.")
        return redirect(url_for("get_activities"))


@app.route("/activity_page/<activity_id>", methods=["GET"])
@login_required
def activity_page(activity_id):
    pages = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    return render_template("activity_page.html", pages=pages)


@app.errorhandler(404)
def error404(error):
    return render_template("error404.html"), 404


@app.errorhandler(500)
def error500(error):
    return render_template("error500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # As a reminder , change debug to False before submission
            debug=True)
