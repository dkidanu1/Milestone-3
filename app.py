import os
import datetime
import time
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for,)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('signin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    for a in session.keys():
        return render_template("recipes.html", recipes=recipes)

# Seach function
@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    search_list = []
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    query = request.form.get("query")
    recipes2 = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    for item in recipes2:
        try:
            item['popular']
        except:
            if session["user"]:
                search_list.append(item)

    return render_template("myrecipes.html", recipes=search_list)

# Popular recipes renering function
@app.route("/popular_recipes")
@login_required
def popular_recipes():
    recipes = list(mongo.db.tasks.find())
    return render_template("popular_recipes.html", recipes=recipes)

# Sign up function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("myrecipes", username=session["user"]))

    return render_template("signup.html")

# Sign in function
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "myrecipes", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")

# Display user recipes function
@app.route("/myrecipes/<username>", methods=["GET", "POST"])

def myrecipes(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes = list(mongo.db.tasks.find({'created_by': username}))

    if session["user"]:
        return render_template(
            "myrecipes.html", username=username, recipes=recipes)

    return redirect(url_for("signin"))

# Signout function
@app.route("/signout")
def signout():
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))

# Add & Save Recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "duration_cook": request.form.get("duration_cook"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_steps": request.form.get("recipe_steps"),
            "created_Date": request.form.get("created_Date"),
            "last_Updated": request.form.get("last_Updated"),
            "image_Url": request.form.get("image_Url"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for('myrecipes', username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    recipeId = request.args.get("recipe")
    if recipeId != "":
        recipe = mongo.db.tasks.find_one({"_id": ObjectId(recipeId)})
        return render_template("add_recipe.html",
            recipe=recipe, category=categories)

    return render_template("add_recipe.html", category=categories)


# Edit & Save Recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "recipe_name": request.form.get("recipe_name"),
                "recipe_description": request.form.get("recipe_description"),
                "duration_cook": request.form.get("duration_cook"),
                "recipe_ingredients": request.form.get("recipe_ingredients"),
                "recipe_steps": request.form.get("recipe_steps"),
                "created_Date": request.form.get("created_Date"),
                "last_Updated": datetime.datetime.now().strftime('%d %b,%Y'),
                "image_Url": request.form.get("image_Url"),
                "created_by": session["user"]
            }
            mongo.db.tasks.update({"_id": ObjectId(recipe_id)}, submit)
            flash("Recipe Successfully Updated")
    recipe = mongo.db.tasks.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html",
        recipe=recipe, categories=categories)


# Delete Recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.tasks.remove({"_id": ObjectId(recipe_id)})
    flash("Task successfully Deleted")
    return redirect(url_for('myrecipes', username=session["user"]))

# 404 error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500 error handling
#@app.errorhandler(500)
#def server_error(e):
 #   return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
