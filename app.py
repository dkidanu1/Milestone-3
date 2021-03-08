import os
import datetime
import time
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
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
                
    return render_template("myrecipes.html", recipes =search_list)


@app.route("/popular_recipes")
def popular_recipes():
    recipes = list(mongo.db.tasks.find())
    return render_template("popular_recipes.html", recipes=recipes)
    


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


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format
                        (request.form.get("username")))
                    return redirect(url_for(
                        "myrecipes", username=session["user"])) 
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")

@app.route("/myrecipes/<username>", methods=["GET", "POST"])
def myrecipes(username):
    # Pulling the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes = list(mongo.db.tasks.find({'created_by': username}))


    if session["user"]: 
        return render_template("myrecipes.html", username=username, recipes=recipes)

    return redirect(url_for("signin"))


@app.route("/signout")
def signout():
    # remove user from session cookies
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "duration_cook": request.form.get("duration_cook"),
            "ingredients": request.form.get("ingredients"),
            "recipe_steps": request.form.get("recipe_steps"),
            "createdDate": request.form.get("createdDate"),
            "lastUpdated": request.form.get("lastUpdated"),
            "imageUrl": request.form.get("imageUrl"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for('myrecipes', username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    recipeId = request.args.get("recipe")
    print(recipeId, "Random letters")
    if recipeId != "":
        recipe = mongo.db.tasks.find_one({"_id": ObjectId(recipeId)})
        print(recipe, "Random letters")
        return render_template("add_recipe.html", 
            recipe=recipe, category=categories)

    
    return render_template("add_recipe.html", category=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "recipe_name": request.form.get("recipe_name"),
                "recipe_description": request.form.get("recipe_description"),
                "duration_cook": request.form.get("duration_cook"),
                "ingredients": request.form.get("ingredients"),
                "recipe_steps": request.form.get("recipe_steps"),
                "createdDate": request.form.get("createdDate"),
                "lastUpdated": datetime.datetime.now().strftime('%d %b,%Y'),
                "imageUrl": request.form.get("imageUrl"),
                "created_by": session["user"]
            }
            mongo.db.tasks.update({"_id":ObjectId(recipe_id)}, submit)
            flash("Recipe Successfully Updated")
    recipe = mongo.db.tasks.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.tasks.remove({"_id": ObjectId(recipe_id)})
    flash("Task successfully Deleted")
    return redirect(url_for('myrecipes', username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)