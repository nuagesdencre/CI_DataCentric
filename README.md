# [Amphora Project](https://https:/ci-vero-datacentric.herokuapp.com)
[![Build Status](https://travis-ci.org/nuagesdencre/CI_DataCentric.svg?branch=master)](https://travis-ci.org/nuagesdencre/CI_DataCentric)
### Data Centric Development Milestone Project

**selling pitch!!**
- Repository of knowledge
- Discover Myths, Legends and fantastic creatures
A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Features
At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. 
**description should match the one for app.json (heroku deployment button)**

## UX
 [Meet our Users!](./static/stories/USERS_STORIES.jpg?raw=true)
- User stories 

- [Planning board](./planning/database_model_planning.xlsx)

- Use of relevant colors for the project [(link here)](https://uxplanet.org/how-color-can-effect-emotion-ccab0431b1d) and [(link here)](https://www.toptal.com/designers/ux/color-in-ux)


## Installation & Deployment

This project has been deployed using Heroku.
- This project can be deployed again using the below button.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    
    This option is available since I provide an app.json file as per the guidelines found [here](https://devcenter.heroku.com/articles/heroku-button).
    
**How did you do it**

- I created the web app using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
Due to the limited scope of this project, the secret key was randomised and left into the app.py file.
- I prepared the Heroku required files (Procfile and requirements.txt) according to the guidelines provided on Heroku [(link here)](https://devcenter.heroku.com/articles/deploying-python).
These documents indicate the language of the app to be deployed, along with its dependencies. I changed the app environment to production and removed the debugging option.
- I then logged in my Heroku account and created an app (ci-vero-datacentric). A Heroku-hosted remote that’s associated with my app was created at the same time.
- On my PyCharm terminal, I provided my Heroku credentials, logged in and linked my existing github repository to the associated git remote hosted by Heroku.
- I used the "git push heroku master" to bring my project into the Heroku remote git repository.
- I entered the IP and PORT into the Heroku Config Vars fields (0.0.0.0 and 5000).
- Once done, I opened the app to ensure everything was working properly.
- I also created a PostgreSQL database using the heroku command "heroku addons:create heroku-postgresql:hobby-dev"
    I had to change from SQLite database (file based) to PostgreSQL on Heroku.



## Technologies Used
> In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Python version 3]()
    - Lorem.
- [Flask]()
    - [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/)
    - [Flask-SQLAlchemy ](http://flask-sqlalchemy.pocoo.org)
    - [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. 
    - [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.     
    - [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
    - [Gravatar](https://en.gravatar.com/site/implement/images) For profile pictures.

- [Jinja2]()
    - Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed. This was used for the game logic and the dynamic elements of the website, along with the forms management.
- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    - Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. 
    CSS was used in this project for the user interface and overall website look - button sizing, background image, etc.
- [HTML](https://simple.wikipedia.org/wiki/HTML)
    - HyperText Markup Language (HTML) is a markup language for creating a webpage.  They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly.
    HTML was essential to this project as it builds up the views and DOM elements of the web app, structured by Flask.
    
- [EmailJS](https://www.emailjs.com/)

    A Javascript library using client-side code to connect to supported email services. I used this service to generate the contact form template and connect to my existing Gmail account.
- [Materialize](https://materializecss.com/)
    Both js and css files.
    
-[SQLite](https://sqlite.org/) 
    - SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
    
-[Heroku]()
    -[PostgreSQL]()
    
I used Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
I used branches for major changes, features and enhancement elements.


## Tests

#### Python and Flask
   I ran the app in development mode by setting the FLASK_ENV=development environment variable in my evironment file.
   I used the [Werkzeug Javascript's in-browser debugger](http://werkzeug.pocoo.org/) at length during this project and tackled the bugs uncovered one by one.
   It was most useful especially when I worked on the final page template.
   
   PyCharm was a wonderful tool to keep track of indentation and typos as well.

#### Javascript, CSS & HTML Validation

To the best of my ability, I conducted and documented tests to ensure that all of my website's functionality work well, while taking in account the user stories.

- [CSS Validation Service](http://jigsaw.w3.org/css-validator/)

    - I ensured my CSS had no typos, errors or incorrect uses using The CSS Validation service.
    - I made sure all DOM elements were readable and easily accessible (i.e. no small links or buttons) on all viewports.

- [JSHINT](https://jshint.com/about/)
    
    - I used JSHINT to pinpoint any bug or typo in my scripts.

- [Nu Html Checker](https://validator.w3.org/nu/about.html)

    - I used the Nu checker to catch unintended mistakes in my Html documents.      


1. Responsiveness and browser compatibility

    - [Browserling](www.browserling.com/)
    
        This website has been tested on multiple devices and browsers to ensure utmost responsiveness.
        I have also used the website 'Browserling' for that purpose.

2. Form Validation
    
## Hurdles
- Search functionality
    - using ILIKE operator [(reference)](https://docs.sqlalchemy.org/en/latest/orm/internals.html?highlight=ilike#sqlalchemy.orm.attributes.QueryableAttribute.ilike)
    - this StackOverflow article [here](https://stackoverflow.com/questions/20336665/lower-like-vs-ilike?noredirect=1&lq=1)
- From SQLite to Postgresql

- UX
User experience: adding breadcrumbs for an easier browsing experience

## Credits

- Disclosure
    - [Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination), which was an extremely helpful reference, especially while trying to set up a reset password feature.
- Content
- Media
    - The background pattern was found on [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/).
    - All original pictures were found on Pixabay. Images and Videos on Pixabay are released under Creative Commons CC0.
    
|item1|item2|item3|
|:-----:|:-----:|:-----:|
|[Amphoras](https://pixabay.com/en/amphora-historically-jugs-3700525/)|[Amphora](https://pixabay.com/en/amphora-poppy-still-life-2780802/)|[Amphora](https://pixabay.com/en/greece-santorini-amphora-2116470/)|


## Acknowledgements

I thank my friends and family who have taken time to play the game and give me feedback.
 A huge thank you to my mentor for constructive criticism and an eagle eye for any typo and/or weak code.
 #### Thank you!
 ###
 
Feel free to get in touch if you have any comments or questions.

vero@nuagesdencre.com