
# The Cook Book

![Responsiveness](static/img/responsive.png)


The live website can be found [The Cook Book](https://recipes-list1-2-2.herokuapp.com/).

---
## Contents
1. About the Site
2. Strategy Plane
3. Scope Plane
4. Structure Plane
5. Skeleton Plane
6. Surface Plane
7. Design
8. Technologies Used
9. Testing
10. Deployment
11. Disclaimer


## About the Site: 
The Cook Book site was designed to give users a simple and easy way to view, save and create recipes. The user will have limited access to the site without signing up, but will have full view of the popular recipes. The idea of the site was to make all the content relevant to recipes and cooking for users who are interested in the theme.


## Strategy Plane
The site was created to showcase knowledge gained in HTML, CSS, JavaScript, Python and mongoDB and to provide an exciting user experience for those interested in cooking. The Website is easy to interact with and provides a seamless experience for the user. Key design decisions were made allowing the users to access the entire page, and all CRUD functionality (Create, Read, Update and Delete) within a few clicks as possible. The site was inspired by the Australian application [Sunee](https://www.sunee.com/).

Site Goals:
- Aim of the site is to showcase learning from the Milestone 1,2 and additional Python and MongoDB courses.
- To provide users with a simple and aesthetic interactive website to view, find recipes, save recipes and create their own recipes. 
- To create a user experience that makes the user want to return and store all recipes within it.

User Stories:
- As a user I want to find recipes for inspiration
- As a user I want to save my favourite recipes
- As a user I want to add and store my own recipes
- As a user I want to be able to update and edit the recipes I created
- As a user I want to delete any recipe I don’t find relevant anymore
- As a user I want to be able to search for recipes by cuisine and key words

## Scope Plane 

The website will include full recipes, inclusive of step by step instructions and images of the final product. Users will have the ability to view popular recipes on the site, as well as create their own recipes. Each user will securely store their recipes on their pages and keep them for later. The website will showcase the brand, and take a more aspirational approach to food and cooking. The website aims to be simple and very straight forward when it comes to functionality, making it easier for the user to navigate and utilize. 

### Features Planned

All for the site will be developed with dynamic user content including appropriate restrictions. Features like create, update, delete, approve are hidden behind a sign up portal.

Visitor: The features shown for visitors will assume the user has not yet signed up or signed into their account:

- Home Page with Sign up or sign in

Registered: This is for users who have an account and come to the website, after logging in a few new features appear
1. Popular Recipes
- Page to provide inspiration for home cooks
- Information Cards- highlight visuals and short description of the recipes
- Save recipe – provides the ability to save a recipe in a user’s “My recipes” page

2. Add Recipe/Edit Recipe 
- Form - Provides structure for creating recipe
- Save- Ability to save recipe 
- Edit – Ability to edit recipe from “My Recipes” or “Popular Recipes” Pages
- Date-  Ability to set the date the recipe was created 

3.  My Recipes
- Username – Personalized username to be shown in header
- Search – User will be able to search through recipes saved in section
- View- Users will be able to see full recipes 
- Edit- Users will be able to find and Edit a saved recipe
- Delete- User will be able to find and delete a saved recipe

4. Sign out
- User will be able to sign out of account and protect information

## Structure Plane

The website is going to have 1 page accessible to users who have not registered and 5 pages available to signed in users each with a distinctive aim and purpose:

- **Home:** Provides a simple landing page for users to take the next step.
- **Popular Recipes:** Provide inspiration for recipes a user can copy and replicate.  
- **My Recipes:** Stores user’s recipes and provides a search functionality allowing the user to find the recipes they are looking for easily.
- **Add Recipe:** Allows the user to create their own recipe that will be saved onto their “My Recipes” Page.
- **Sign in/ Sign Out:** Allows the user to sign in with a redirect to the “My Recipes” page and allows the user to sign out of their account and redirects to the home page. 

The 5 pages consist of different sections. A navigation bar which will be adapted accordingly for the mobile version, will be static on the top of the website. This will allow the user to move to any other section easily without scrolling or searching for the navigation. Links throughout the website will be responsive to the hover, on the navigation bar it will be highlighted with an overlay.

### Database:

This website has 2 databases, 1 for users and 1 for recipes, these are both connected to each other and are utilised to store various user details and recipe information. All information content on the website is derived from the 2 databases. 

User Database explained:
- Username: Stores the chosen username added by the user.
- Password: Is a hashed password, so there are no clear text passwords the database
Recipe Database explained:
- Category: is how the user chose to categorize the recipe
- Name: is how the user choose to name the recipe.
- Description: is where the user describes the recipe in short
- Duration: is how long the cook takes
- Ingredients: is stored as an array and stores all ingredients the user choose to use
- Recipe Steps: is stored as an array, and unpacks on the recipe page for user to identify steps for cooking the recipe
- Created Date: is the date the recipe as created and applies it to the details when viewing the recipe later.
. Last Updated: is the date the recipe was edited if the user chooses to update after initially saving.

### Features I want to implement

During the of development, I noticed a few features that the site would benefit from and create a stickier experience for the user. They are not however, necessary for the project to be completed and were left for later development.
- Interactive and real-time feed of all recipes being added to the site
- Provide user group feature, where a recipe can be co-owned by two or more users.
- Add Reset password for users in the user profile.
- Admin profile allowing for overview insights of users and recipes added to site.

## Skeleton Plane

The Cook book website will have a consistent pastel pink and grey theme, this will include consistent typography, sizing, colour and look/feel. 

![Wireframe](static/img/wireframe.jpg)
![Wireframe1](static/img/wireframe2.jpg)

## Surface Plane

### Testing 
The site has multiple features and in order to test effectively I broke down the testing phases into multiple sections seen below:
- Interaction 
- Security (URL Injection)
- Responsiveness 
- W3 HTML Validator
- W3 CSS Validator
- JSHint
- PEP8

#### 1. Interaction 

This testing phase was to ensure all the functionality for the site was working in two different scenarios not signed in and signed in.

**Not Signed in**
1. Home Page:
- Opening the site in full screen expecting to see all images, buttons, and labels displaying correctly.
- Clicking on sign in expecting it to redirect to sign in page correctly.
- Clicking on sign up expecting it to redirect to sign in page correctly.
- Hoovering over the navigation bar to experience grey overlay indication.

2. Sign up Page:
- Attempted putting in 1 letter into username, and left password blank and clicked confirm password blank expecting error.
- Attempted putting in 1 letter into username, and 1 letter into the password field expecting feedback on all input boxes.
- Fixed username to 5 letters, left password blank, Expecting error.
- Fixed username to 5 letters, submitted password less than 5 characters, Expecting error.
- Attempted username with 3 characters and fixed password to correct length, expected Error.
f Fixed username password, now all registration rules are correct, allowing user to register.

3. Sign in Page:
- Attempted to input username only and click log in, asked for password.
- Typed in username and wrong password, received expected feedback, and log in not processed.
- Inputted password only, and no username, was informed to input in username.
- Inputted in correct username and correct password, website allowed me to sign in.
- When logged in successfully, expecting the page to redirect user to my recipes page.

**Signed in**
1. Home Page:
- Expecting the navigation bar to no longer have sign in and signup, but popular recipes, my recipes, add recipe and sign out.
- Expecting to see change in buttons on hero image to popular recipes and add recipe.
- Clicked popular recipes button, getting redirected to popular recipes page.
- Clicked add recipe, getting redirected to add recipe page.

2. Popular Recipes page:
- Visiting Popular Recipe page that my user has not made, expect to not see edit or delete buttons. 
- Clicked recipe card to test interactive functionality of card. 
- Clicked “Save Recipe” redirected to add recipe page with pre filled fields.
- Clicked “The Cookbook” to redirect to the home page.

3. My Recipes:
- Visiting Popular Recipe page that my user has made, expect to see edit or delete buttons. 
- Clicked recipe card to test instructiveness of card, viewed recipe correctly.
- Clicked Edit recipe, changed recipe and tested save functionality.
- Test search function, viewed all cards with “Indian” in it.
- Test Reset function, viewed all recipes.
- Clicked Delete, successfully deleted.
- Clicked “The Cookbook” to redirect to the home page.

4. Add Recipe:
- Attempting to submit the form empty, expecting to receive error message across the whole form.
- Adding 1 letter in recipe name, expected an error as it's too short.
- Adding a category and recipe name, attempted to save, successfully saved.
- Click Edit Recipe, pushes the submission to my recipe.

#### 2. Security (URL Injection) 
This section will attempt to preform different URL injections to see if a malicious attacker can by-pass security. 

**View Popular Recipes page without being logged in**
- When using https://8080-gray-junglefowl-zpzloiig.ws-eu03.gitpod.io/popular_recipes I tried to view popular recipes and managed to see them.
- A security breach was found and fixed at this point. 

**Add a Recipe without being logged in**
- When using https://8080-gray-junglefowl-zpzloiig.ws-eu03.gitpod.io/add_recipe I tried to submit a new recipe to the site, I failed to receive the error message, however was redirected to an Error page from Werkzeug.
- A breach was found at this point. 

**Delete recipe without being logged in**
- When using https://8080-gray-junglefowl-zpzloiig.ws-eu03.gitpod.io/myrecipes/dkidanu I tried to delete an existing recipe. 
- I was redirected to a werkzeug error instead of an error message. 

**Update Recipe without being logged in**
- When using https://8080-gray-junglefowl-zpzloiig.ws-eu03.gitpod.io/myrecipes/dkidanu I tried to update a recipe, I was redirected to a werkzeug error page instead of an error message.

**Fixes for URL injection**

The above security features were mitigated by adding a werkzeug feature Login Required Decorator from flask (https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator). This prohibits users without a username to view the pages. This has ensured the website is secure and safe. The redirect was set up and will now direct the user to the sign in/sign up page where they are prompted to sign in or sign up to utilize the site.  

#### 3. Responsiveness 
In this test the website was tested to all default device sizes provided by chrome dev tools.

1.	360 x 640 Galaxy S5
2.	375 x 667 iPhone 6/7/8
3.	375 x 812 iPhone X
4.	411 x 731 Pixel 2
5.	411 x 823 Pixel 2 XL
6.	414 x 736 iPhone 6/7/8 Plus
7.	768 x 1024 iPad
8.	1024 x 1366 iPad Pro

**Design Testing for Mobile**

During testing of responsiveness a number of issues came out on the screen sizing. 

![Responsiveness](static/img/button.png)

At this point, spacing and sizing of the buttons was an issue. This was an issue fixed by utilization of marterialize columns. 

![Responsiveness](static/img/db.png)

At this point, the database call was not working and information was not being rendered into the accordion. This was a fixed solved with a few syntax adjustments. 

![Responsiveness](static/img/myrecipes.png)

At this point, spacing and sizing of the buttons was an issue. This was an issue fixed by utilization of marterialize columns.

![Responsiveness](static/img/homescreen.png)

At this point the sizing of the hero image was an issue. For this section width and css styling controls were utilized to adjust the image. 

**W3 HTML Validator**
- Erros in element positioning and syntax (Fixed)
- Error for Child element (Not Fixed)
- Missing Alt tag (Fixed)
- Warnings were noted and mostly addressed, project remains with 2

**W3 CSS Validator**
- CSS Style Sheet - Minor issues with symbols (fixed)

**JSHint**
The js test came back clear but included two version warnings that will be monitored:

Two warnings
- 19	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 20	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

**PEP8**
- Additional white space (Fixed)
- Error in indentation (Fixed)
- Had many lines above above 79 character in length (Fixed)
- Continuation line under-indented for visual indent (Not All Fixed)
  

**Design**

The design takes a minimalistic approach to display content and create a pleasing and simple user experience. The focus was on the dynamic user content, allowing the user to complete the identified tasks and walk through a delightful user journey.

![Color](static/img/colors.jpeg)

The Cook Book uses pastel colours to create designs that are easy on the eyes and evoke feelings of relaxation and calm. Minimalistic features compliment the colour scheme. The idea is to have a consistent feel throughout the site and throughout the user journey. 

Inline styling was used to override the materialize framework, majority of the styling is within the style sheet however, in some instances inline had to be implemented to get the desired effect. 

**Typography**

I chose to use Nunito Sans for majority of the text support by sans-serif due to readability and consistency with colors and theme. 

### Technologies Used

**Languages Used**

- HTML5 -  Created the foundation of the site
- CSS – Applied the styling across the pages
- Javascript – Added logic rules for forms 
- Python – Runs the backend server code including safety

**Libraries**
- Marterial Bootstrap – Styling site 
- jQuery – Simplifying some of the Javascript needs 
- Google Fonts – For fonts utilized on the site

**Python Libraries and Framework**
- Flask – Utilized to run route operations for code
- Os – Utilized to read environmental variables
- Time – Added to generate timestamp which it used in the database
- Flask_pymongo – For search operations on site 
- Bson – Utilized to get ObjectID of data sets
- Werkzeug.security – Utilized to operate hashing and safety measures to secure passwords

**Database**
- MongoBD- For storing content for the database of recipes and users

### Deployment 
The steps below will explain how you can get the website running on heroku and locally.

**Tools required to be installed**
- Python 3 (Pip 3 comes installed by default)
- Git
- Heroku CLI

How to Clone and set up the website locally:

**Clone website**
1. Go to [GitHub](https://github.com/dkidanu1).
2. Click Repositories.
3. Locate Milestone-3.
4. Open Milestone-3
5. Click the green button clone to download.
6.Or clone from URL using the following command in terminal: got clone https://github.com/dkidanu1/Milestone-3

**Installing Requirements**

Once you have cloned the project on your computer:

1. Open the Terminal and navigate to Milestone-3 folder on the computer.
2. Install the libraries from requirements.txt by typing pip3 install -r requirements.txt

**Setting up the database keys**
Once the project is cloned, and you have the libraries installed from requirements.txt, you can now set up the database.
1. Create a python file called env.py, and place it outside of the folder structure, next to app.py.
2. Inside the newly created env.py file, you need to add information to 2 variables and 1 import.
3. At the top of env.py add the following line import os.
4. Then add the following 2 lines below.
5. os.environ["Mongo_URI"] = "mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority".
6. os.environ["SECRET_KEY"] = "Can be anything you want".
7. Add os.environ["MONGO_DBNAME"] = 'Your database name'.

**Understand the Connection string**

mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority
1. MongoDB-Password, you need to provide the password for your MongoDB atlas account.
2. Cluster-Name is the name you create when setting up MongoDB for the first time, it is where your databases are stored, often shown at the top of the page.
3. Database-Name this is the name of the database you have created, can be found under the Collections tab inside MongoDB Atlas.


**Running the Project locally**
1. Run app.py
2. Paste http://127.0.0.1:5000/ into your browser URL to access.

**Deploy The Cook Book on Heroku**
Before beginning this step, you need to complete the above step 1. Clone Website.

**1. Setting up Heroku**
1. Create an account on Heroku.
2. Click New button, then Click Create new app.
3. Give it a name and choose your region.
4. Click Create App.
5. Find your App name on the dash board, and enter.
6. Click Settings, and locate Config Vars, and fill in like shown below (Just edit out the placeholder text).

| Key        | Value           | 
|:------------- |:-------------| 
|  IP  | 0.0.0.0 | 
|  PORT  | 5000 | 
|  MONGO_URI  | "mongodb+srv://myRoot:MONGODB-PASSWORD<span>@CLUSTER-NAME-96wib.mongodb.net</span>/DATABASE-NAME?retryWrites=true&w=majority" | 
|  MONGO_DBNAME  | Name of the database |
|  SECRET_KEY  | "Secret key you made for local" |

**2. Setting up our files**

At this stage, go back to your IDE, now set everything up for pushing to Heroku.
1. If the Procfile is missing, please preform the following command in your terminal echo web: python3 app.py > Procfile
2. If the requirements.txt is missing, please preform the following command in your terminal pip3 freeze > requirements.txt

**3. Deploy to Heroku**
1. In your Terminal type heroku login.
2. Then git push heroku master .
3. Open Heroku website.
Navigate to the app (The Cook Book), and click Open App, and now everything should be running.


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

### Disclaimer 
This project is for Educational purpose only