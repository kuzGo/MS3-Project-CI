# [Growapps](http://ms3-project-ci.herokuapp.com/home)
<a name="totop"/>

## <p><img src="static/docs/amiresponsive.PNG" style="min-width:100%" height="500" alt="Photo of website on devices"></p>
---
<p> <img src="static/images/logo.png" width="80" height="80" alt="Company logo"></p>

- Link to live website : [Growapps](http://ms3-project-ci.herokuapp.com/home)
---
Growapps is aimed towards those interested in looking for a  place where they can find or share ideas about child development. The initial idea to create this project as a third milestone project with the Code Institute, appeared during the times of lockdowns,where movements and interaction with others was limited. To help those who were in search of a source to help them continually develop their child skills with limited resources Growapps was created. Welcome to Growapps!

##### Table of Contents  
- [UX](#ux)  
- [The Site owner Goals](#usergoals)  
- [Existing Features](#existing)
- [Features Left to Implement](#leftfeatures)
- [Database Design](#dbdesign)
- [Project Requirements](#prequrements)
- [Wireframes](#wireframe)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#ack)

## UX
<a name="ux"/>

### User Stories

- User 1 : As a user I want to find a source of ideas of how to keep my kids entertained.
- User 2 : As a user I want to share my ideas with others.
- User 3 : As a user I want to be able to edit my activities should I need to.
- User 4 : As a user I want to be able to delete activities should I need to.
- User 5 : As a user I want to have convenient access to the data provided by all other members.
- User 6 : As a user I want to be able to register as a regular user.
- User 7 : As a user I want to be able to login to my account as a registered user.

### The Site owner Goals
<a name="usergoals"/>

- As a site owner I want to benefit from the collection of the dataset.
- As a site owner I want to promote other brands whose business involves child development.

## Existing features
<a name="existing"/>

### Unregistered users
- Landing Page

- Navigation bar
    * Company Logo
    * Home Button
    * Login Button
    * Register Button

- Mobile sidenav for mobile devices
    * Company Logo
    * Home Button
    * Login Button
    * Register Button

- Image slides with text content describing purpose of the website.

- Three card panels inviting users to register.
- Web site footer
    * Company logo
    * Copyright 
    * Useful liks
- Login page
- Register page
- Error 404 page
    * Will appear in case of when the server can't find the requested resource.
- Error 500 page
    * Will appear in case if the server encountered an unexpected condition.


### Registered users

- Registered users have access to most of the features apart from the admin's page.
In case that registered user attempts to access the admin page, they will not be able to and will  be notified that they need admin rights.
- Activities page
    * Search bar
        * Search button
        * Reset Search button
        * Add activity button
- Activity card panels
    * Ability to read all activities;       
    * Ability to edit your own activities;  
    * Ability to delete your own activities;  
    * Ability to view all activities on a single page.
- Modal popup
    * Will appear in case if the user tries to edit or remove activity, asking for confirmation.
- Logout button
- My Profile button
    * List of all activities created by the user.
- Admin page
    * Restricted to admin only.
## Admin
- Admin page  consists of the card panels with all current activity categories. Admin has a right to edit and/or remove activities from all users.
    * Ability to remove and update existing categories.
- Add category button
    * Ability to add a new activity category.

- Color scheme
    * Color palette for the website has been generated using [Colormind](http://colormind.io).
    Carefully selected color scheme with the idea in mind to create harmonious and aesthetically pleasing website where users would want to remain longer.

 <p><img src="static/docs/color-scheme-ms3.PNG" style="min-width:100%" height="200" alt="Color scheme"></p>


- Typography
    * The website fonts used are Google fonts [Indie Flower](https://fonts.google.com/specimen/Indie+Flower#standard-styles) for headers.The header's  are sized quite large for easier readability and at the same time to create personal looking, almost handwriting effect  .Google fonts [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=Open+Sans) font is used where a more formal way of expressing was required , such as instructions or login/register pages.

## Features Left to Implement
<a name="leftfeatures"/>

## Database Design
<a name="dbdesign"/>

### Database Schema

[MongoDB](https://www.mongodb.com/) is used as a project's database.The project consists of one MongoDB Atlas database and   three  collections : users , activities and categories. 

<p><img src="static/docs/mongodb.PNG" style="min-width:80%" height="200" alt="MongoDB Schema"></p>

## Project Requirements
<a name="prequrements"/>

Create a fully CRUD compliant app where users have ability to create, read, update and delete records.

### Main Technologies:

- HTML5, CSS3, JavaScript, Python+Flask, MongoDB



## Frameworks and libraries:
<a name="flibs"/>


- [**Jinja**](https://jinja.palletsprojects.com/en/3.0.x/) used as a templating engine to render backend data in html.
- [**Flask**](https://flask.palletsprojects.com/en/2.0.x/) used as a web framework for routing and rendering templates.
- [**Materialize**](https://materializecss.com/) used as a framework to increase page responsiveness .
- [**jQuery**](https://jquery.com/) used as a JavaScript library and for Materialize components  initialization.

## Other Technologies used:
- [**Werkzeug**](https://werkzeug.palletsprojects.com/en/2.0.x/) used for authentication and password security.
- [**PyMongo**](https://pymongo.readthedocs.io/en/stable/) used for interacting with MongoDB database from Python.
- [**dnspython**](https://www.dnspython.org/) used as a DNS toolkit for Python.
- [**functools**](https://docs.python.org/3/library/functools.html) used to create wraps and function decorator.
- [**MongoDB**](https://www.mongodb.com/) used as a project's database.
- [**Heroku**](https://www.heroku.com/)  used for hosting deployed website.
- [**RandomKeygen**](https://randomkeygen.com/)  used for creating Fort Knox Passwords.
- [**Google Dev Tools**](https://developer.chrome.com/docs/devtools/) used for developing and testing webpage.
- [**Firefox Dev Tools**](https://developer.mozilla.org/en-US/docs/Tools) used for developing and testing webpage.
- [**Get Waves**](https://getwaves.io/) used to generate SVG banner.
- [**Balsamiq**](https://balsamiq.com) used for creating a wireframe.
- [**Resize Pixel**](https://www.resizepixel.com/) Free online image editor used to resize images format.
- [**Google Fonts**](https://fonts.google.com) used for project fonts.
- [**Google Icons**](https://fonts.google.com/icons) used for project icons.
- [**Gitpod**](https://gitpod.io) used as a development environment.
- [**Gitpod Chrome Extension**](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) used to open Github repo in Gitpod.
- [**GitHub**](https://github.com/) used for storing repository. 
- [**Canva**](https://www.canva.com) used for logo creation.
- [**Autoprefixer**](https://autoprefixer.github.io/) used to add CSS prefixes and ensure cross-browser compatibility.
- [**Youtube**](https://www.youtube.com/) used as a general source of information.
- [**W3School**](https://www.w3schools.com/) used as a general source of information.
- [**Pexel**](https://www.pexels.com/) used to download the website's images.
- [**Pixabay**](https://pixabay.com/) used to download the website's images.
- [**Stackoverflow**](https://stackoverflow.com/) used as a general source of information.
- [**W3C Markup Validator**](https://validator.w3.org/) Used to test HTML code validation.
- [**W3C CSS Validator - Jigsaw**](https://jigsaw.w3.org/css-validator/) Used to test CSS code validation.
- [**PEP8 online**](http://pep8online.com/) used during post deployment testing stage to ensure PEP8 requirement.
- [**Am I Responsive**](http://ami.responsivedesign.is/) used during post deployment testing stage.
- [**Pixlr**](https://pixlr.com) used to remove background and editing photographs.

## Project Wireframe Link :
<a name="wireframe"/>

To see Project Wireframes please click the link: 
<a href="https://github.com/kuzGo/MS3-Project-CI/tree/main/static/wireframes">Wireframes</a>

## Testing :
<a name="testing"/>

- Click here to see testing in a separate file: [Testing](https://github.com/kuzGo/MS3-Project-CI/blob/main/TESTING.md) 

## Deployment
<a name="deployment"/>

### Version control 

- The project's website code was written using Gitpod IDE. In order for code to be pushed to GitHub,it had to be added to stage for commit using `git add `command in GitPod's CLI .Once changes have been successfully added, it is required to commit these entering `git commit -m` into CLI. After committing it then can be pushed to GitHub by entering `git push` command in CLI.

### GitHub

- How to fork a repository: Forking a repository allows you to make changes to the code without affecting the project. To fork a repository follow the next steps:
1. If you do not have one,create a [GitHub](https://github.com/) account and remain logged in.
2. Navigate to [kuzGo/MS3-Project-CI](https://github.com/kuzGo/MS3-Project-CI);
3. In the top right corner find the "Fork" icon.
4. Click the Fork icon to fork the repository.

- How to clone repository: Cloning repository allows you to pull down a full copy of the repository and work on it locally on your machine. To clone a repository follow these steps:
1. If you do not have one,create a [GitHub](https://github.com/) account and remain logged in.
2. Navigate to [kuzGo/MS3-Project-CI](https://github.com/kuzGo/MS3-Project-CI);
3. On the repository main page navigate to the "Code" drop down menu button and click on it.
4. Ensure to select HTTPS and click on the clipboard icon to copy the URL.
5. In the IDE you chose to work, open the new terminal.
6. Change the current working directory location where you want the cloned directory.
7. Enter command git clone and paste the URL you copied.
8. Click Enter.



### Heroku

- The website is deployed to [Heroku](https://www.heroku.com/) due to GitHub's ability to only host static pages. To successfully  deploy the website to Heroku please follow these steps.

### Prerequisite
In order to successfully  run the app on Heroku,there are a few applications and dependencies required.
1. In the IDE terminal enter command `pip3 freeze--local > requirements.txt`.
2. Create Procfile using CLI command `echo web: python app.py > Procfile`. Delete a blank line to avoid any possible issues with the app.
- Heroku Deployment

1. If you do not have one,create a free [Heroku](https://www.heroku.com/) account and remain logged in.
2. For this particular project Python needs to be selected as a Primary Development Language.
3. Navigate to "Create New App" button.
4. Create a unique app name using hyphens instead of spaces.
5. Choose a region closest to you. I selected my region Europe.
6. Click Create App button.
7. In the Deploy section, as Deployment method select GitHub,this option will automatically deploy from GutHub repository.
8. In the Connect to GitHub section ensure that your GitHub profile is displayed.
9. Enter repository name and click Search button.
10. Once repository is found click Connect button.
11. Navigate to settings and click Reveal Config Vars.
<p><img src="static/docs/configvars.PNG" style="min-width:30%" height="100" alt="Heroku App snip"></p>

12. Enter variables from `env.py` file : IP , MONGODB_NAME, MONGO_URI, PORT and SECRET_KEY. This is required step since Heroku will not be able to find these secured in `gitignore` folder.
<p><img src="static/docs/vars.PNG" style="min-width:30%" height="100" alt="Heroku App snip"></p>

13. Prior to enabling automatic deployment, make sure that requirements.txt and Procfile are pushed (`git push`)to GitHub.
14. Click Deploy Branch button.


## Credits :
<a name="credits"/>

### Code snippets :

For the purpose of this project I refered to and used authentication from the Code Institute Tim Nelson's [Task Manager Mini Project](https://github.com/Code-Institute-Solutions/TaskManager).
All code snnipets used from this project have been refactored to make them my own and suit more my project's needs.

[Materialize](https://materializecss.com/) has been used as project's framework. Components used for the front end such as navbar, cards, image slider and modal popup  have been customised and code has been refatored to suit project needs.

I found the code for Materialize's select validation [here](http://jsfiddle.net/b8frk03m/6/).



### Photographers :
- Pexels
- [Yan Kurkov](https://www.pexels.com/photo/children-doing-arts-and-crafts-at-school-8612992/)
- [Yan Kurkov](https://www.pexels.com/photo/boy-in-blue-long-sleeve-shirt-and-denim-shorts-playing-with-wooden-toy-cars-8612955/)
- [Kindel Media](https://www.pexels.com/photo/sea-sunny-beach-vacation-7862529/)
- [Pexels](https://images.pexels.com/photos/311268/pexels-photo-311268.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
- [Pexels](https://images.pexels.com/photos/8435803/pexels-photo-8435803.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Pexels](https://images.pexels.com/photos/1107911/pexels-photo-1107911.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Pexels](https://images.pexels.com/photos/4484878/pexels-photo-4484878.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Pexels](https://images.pexels.com/photos/3662670/pexels-photo-3662670.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Pexels](https://images.pexels.com/photos/168866/pexels-photo-168866.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)
- Photo by RODNAE Productions from Pexels
- pexels-elina-fairytale-4008773 
- Photo by Ketut Subiyanto from Pexels 

- Pixabay
- [Pixabay](https://pixabay.com/illustrations/illustration-child-clipart-graphics-2814002/)


## Acknowledgements
<a name="ack"/>
- I wanted to thank[ Nishant Kumar(https://github.com/nishant8BITS)], for all the support and pieces of advice during mentoring sessions on how to improve the project.
- Code Institute for equipping me with the skills and knowledge to complete this project.
- Friends and family for support,motivation and creating activity datasets.
- Some parts of the README.md file have been used in my previous project.
- Amy O'Shea, Slack channel lead who helped me with Jinja `for loop` bugs.
- Yigit who tested my app and pointed out a few issues on Slack's peer-code-review channel.

### Site is for educational purposes

[Back To Top](#totop)

