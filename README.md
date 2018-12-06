# [Project Amphora](https://https:/ci-vero-datacentric.herokuapp.com)
### Data Centric Development Milestone Project
**If you are fascinated by impossible stories or want to share a spooky legend, this is your space!**
Amphora is a repository of knowledge allowing readers to discover **myths, legends and fantastic creatures**.
You can easily browse through the available entries using their categories, or you can track the posts of 
specific users, should they happen to have the best stories.
This online space is reserved to the endlessly curious minds of the web who want to keep track of their favourite mysteries and add some more to the collection.

## Features
- #### Home and Navigation

  Visitors can access the home page by clicking on the navigation bar's brand name ('Amphora') at all times.
  The navigation bar is responsive and is displayed according to the viewer's screen size (collapsible side menu or top menu.)

- #### Repository
    - There are two different types of entries in Amphora's repository:
        - Stories
        - Beings
        
    Both type of entries allow a logged in visitor to share information about a relevant story or being. The entry can then be recorded
    against one of the multiple categories that can be added or edited by visitors. Once submitted, the posts are clearly listed and displayed, up to 3 per page at once. 
    Pagination ensure that visitors do not have to scroll down should there be many entries.
    
    - Visitors can view all entries posted without login in. They can also look up the entries by their category directly.
    
    - Moreover, it is possible to leave comments on posts authored by others.
    
- #### About
    
    The project's purpose and general information relevant to the website's functions is available via the About page.
    
- #### Contact
    
    A contact form is available on the contact page. It allows visitors to send in comments and reach the webmaster directly.
    An alert is displayed when the form is submitted and the visitor, by providing his/her own email address, 
    will receive an auto-reply confirming the webmaster's reception of the message issued.
    
- #### Search

    Visitors have access to a search option with an overall scope of the website's database (lookup against entries, comments, users  and categories).
    The search results are displayed in a clear and organised manner, with a direct link to the element retrieved.

- #### User identification (profile, login, logout and register)
    
    Visitors can browse Amphora without login in or registering, however most features remain unavailable. Categories can be created and edited by anonymous visitors, and Amphora's visitors are invited to do in good faith.
    Visitors, once registered and logged in, are able to view their own profile; access their own entries easily; submit and edit entries in the repository; add comments to entries authored by other visitors.
    Additionally, visitors who have trouble remembering their password can request a password reset via the login page. An external email will be sent with a link allowing them to set up a new password.

## UX
- [Planning board](./amphora/planning/database_model_planning.xlsx)
- [Database structure](./amphora/planning/database_model_planning.pdf)

- Use of relevant colors for the project [(link here)](https://uxplanet.org/how-color-can-effect-emotion-ccab0431b1d) and [(link here)](https://www.toptal.com/designers/ux/color-in-ux)

*Update*: After receiving comments from visitors and friends alike, breadcrumbs for an easier browsing experience. 
    As the repository can be accessed from different pages, it is nice to see quickly where someone can return or where the page is nested within the website itself.

 [Meet our Users!](./amphora/static/stories/USERS_STORIES.jpg?raw=true)
#### User stories
 
| As a [persona] | I want to [do something]                                            | so that I can [realize a reward]                                                               |
|----------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Persona        | Goal                                                                | Result   /   Motivation  / Usability                                                           |
|                |                                                                     |                                                                                                |
| :woman: Camille        | wants to learn more about other cultures                    | so she can have more interesting topics of conversation.                                       |
|                | wants to give her two cents and comment                             | so she can interact with other people online with the same interests.                          |
|                | wants to use her smartphone to go on the internet                   | so she can access websites on the go.                                                          |
|                | wants to use a nickname online                                      | so she can have a personalised browsing experience.                                            |
|                |                                                                     |                                                                                                |
| :older_man: Harry          | wants to access information easily                                  | so he can help his son with his assignments.                                                   |
|                | wants to browse online without having to log in                     | so he does not have to remember a password or username.                                        |
|                | wants to visit the website by browsing categories                   | so he can find a story he can't quite remember, but knows is related to the Chinese mythology. |
|                | wants to send messages to the webmaster without leaving the website | so he does not forget the purpose of his message and stay focused.                             |
|                | wants to be able to access a website on his iMac                    | so he can browse from his computer at home.                                                    |
|                |                                                                     |                                                                                                |
| :boy: Mike           | wants to find specific information using a search function    | so he can access them directly.                                                                |
|                | wants a reset password option                                       | so he can retrieve and update his login details.                                               |
|                | wants to find original stories                                      | so he can get inspiration for his creative and school-related projects.                        |
|                | wants to browse the content of a website for free                   | so he can afford using all the features and recommend them to his friends.                     |
|                |                                                                     |                                                                                                |
| :man: Lou            | wants to discover more stories                                | so he can have more fun things to tell his daughters at bedtime.                               |
|                | wants to avoid going on big commercial websites                     | because he does not like ads and popups distracting him in his browsing.                       |
|                | wants to track information he likes                                 | so he can return to it more easily.                                                            |
|                | wants to see what other people think about the stories              | so he can decide if they are interesting or not, and if he wants to read further.              |
|                | wants to know the source of his information                         | so he can find reliability in the credit given on articles and posts.                               |

## Installation & Deployment

This project has been deployed using Heroku.
- This project can be deployed again using the below button.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    
    This option is available since I provide an app.json file as per the guidelines found [here](https://devcenter.heroku.com/articles/heroku-button).
*******

- I created the web app using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
The secret key and other config variables were stored in an environment file during development. These variables are relevant to the Flask project and the issuance of email via the reset password option.

- I then logged in my Heroku account and created an app (ci-vero-datacentric). A Heroku-hosted remote that’s associated with my app was created at the same time.
I linked my "nuagesdencre/ci-datacentric" Github repository to the Heroku app for deployment from its master branch.

- On the Heroku website, using the dashboard, I entered the IP and PORT into the Heroku Config Vars fields (0.0.0.0 and 5000), along with my environment file's other variables.

- I also created a PostgreSQL database using the heroku command **"heroku addons:create heroku-postgresql:hobby-dev"**.

     I had to change from SQLite database (file based) to PostgreSQL on Heroku for my database to retain its contents once the website is deployed online. I commented out my local database and include the
link to the Heroku generated PostgreSQL database instead. I intialized the PostgreSQL database and pushed the migrations.

- According to the guidelines provided on Heroku [(link here)](https://devcenter.heroku.com/articles/deploying-python), I prepared the Heroku required files (Procfile and requirements.txt).
These documents indicate the language of the app to be deployed, along with its dependencies.
Procfile used in production:  **web: flask db upgrade; gunicorn -w 1 amphora:app**
  
Moreover, I changed the app environment to production and removed the debugging option.

- I manually requested the deployment from the master branch.
 I reviewed the logs via the Heroku dashboard once the deployment confirmed and opened the app using my web browser to ensure everything was working properly.
 
- There is no difference between the development and the live version of this project.

## Technologies Used
- [Materialize](https://materializecss.com/)
    
    I reference both js and css files; I used the library to make this project as pretty and clean as possible.
    
- [JQuery](https://jquery.com)
     
     The project uses JQuery to simplify DOM manipulation.
    
- [EmailJS](https://www.emailjs.com/)
    
    A Javascript library using client-side code to connect to supported email services. I used this service to generate the contact form template and connect to my existing Gmail account.

    
- [Python 3.6.5](https://www.python.org/)
    
    Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java. Most of this project's elements are built using Python via Jinja2.
    
- [Flask](http://flask.pocoo.org/docs/1.0/)

    This project relies entirely on the Flask framework.
    - [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) A Blueprint is a way to organize a group of related views and other code. 
    Rather than registering views and other code directly with an application, they are registered with a blueprint. I used blueprints to organise my modules' views within my project.
    - [Flask-SQLAlchemy ](http://flask-sqlalchemy.pocoo.org) I used Flask-SQLAlchemy to develop my application locally and test my database relationships (SQLite).
    - [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. It was used for the maintenance and update of my database in the current project.
    - [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.     
    - [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA. I used Flask-WTF to generate the forms of the current project.
    
- [Gravatar](https://en.gravatar.com/site/implement/images) 

    I used Gravatar to provide every registered visitor with a randomized profile picture.

- [Jinja2]()
    
    Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed. This was used for the dynamic elements of the website, along with the forms management.

- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    
    Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. 
    CSS was used in this project for the user interface and overall website look - button sizing, background image, etc.

- [HTML](https://simple.wikipedia.org/wiki/HTML)
    
    HyperText Markup Language (HTML) is a markup language for creating a webpage.  They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly.
    HTML was essential to this project as it builds up the views and DOM elements of the web app, structured by Flask.

- [Heroku](https://www.heroku.com/)

    Heroku is a cloud platform based on a managed container system, with integrated data services and a powerful ecosystem, for deploying and running modern apps. This project was deployed on the Heroku cloud platform.
    
     - [Heroku Postgres](https://www.heroku.com/postgres)
        
        PostgreSQL is one of the world's most popular relational database management systems. I transitioned by database from SQLAlchemy (SQLite) to PostgreSQL.
        
I used Git & GitHub for version control.
I used branches for major changes, features and enhancement elements.

## [Testing](testing.md)
 Due to the length of my tests' description, I have included my breakdown in another file referenced [here](testing.md).
 
## Hurdles
- Search functionality

    - It took me a while to understand I need to use ILIKE operator in order to make the search in my database case-insensitive. [(reference)](https://docs.sqlalchemy.org/en/latest/orm/internals.html?highlight=ilike#sqlalchemy.orm.attributes.QueryableAttribute.ilike)
    - I also consulted this StackOverflow article [here](https://stackoverflow.com/questions/20336665/lower-like-vs-ilike?noredirect=1&lq=1)

- Transition from SQLAlchemy to PostgreSQL
    I had to look up different approaches before figuring out how to proceed. I t turned out to be much simpler than expected, thanks to Heroku Postgres.
    - [Making a Flask app using a PostgreSQL database and deploying to Heroku](http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/)
    -[Heroku Postgres](https://www.heroku.com/postgres)
    
## Credits

- Disclosure

    I consulted the following websites and articles while working on this project.
    They were extremely helpful resources, especially while I attempted to transition the database type from SQLite to PostgreSQL to set up pagination, and to implement a reset password feature.
    As per usual, Stack Overflow was a regular source of information whenever I encountered a hurdle.
    - [Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
    - [Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
    - [Flask - SQLAlchemy full text search](https://stackoverflow.com/questions/41000855/flask-sqlalchemy-full-text-search)
    - [Making a Flask app using a PostgreSQL database and deploying to Heroku](http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/)
    - [Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
    
- Amphora's Content
    - Amphora's many entries have content sourced from various websites. In order to give credit where it is due, the posts include an URL field where the source of the content is listed.
- Media
    - The background pattern was found on [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/).
    - All original pictures were found on Pixabay. Images and Videos on Pixabay are released under Creative Commons CC0.
    
    |Image 1|Image 2|Image 3|
    |:-----:|:-----:|:-----:|
    |[Amphoras](https://pixabay.com/en/amphora-historically-jugs-3700525/)|[Amphora](https://pixabay.com/en/amphora-poppy-still-life-2780802/)|[Amphora](https://pixabay.com/en/greece-santorini-amphora-2116470/)|


## Acknowledgements

I thank my friends and family who visited Amphora, posted entries, tried to 'break' the website and gave me feedback.
Once again, my mentor provided pointers, constructive criticism and advice that led me in the right direction.
 #### Thank you!
 ###
 
Please get in touch if you have any comments or questions.

vero@nuagesdencre.com