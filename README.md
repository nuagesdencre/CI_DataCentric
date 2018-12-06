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
|                | wants to know the source of his information                         | and finds reliability in the credit given on articles and posts.                               |

## Installation & Deployment

This project has been deployed using Heroku.
- This project can be deployed again using the below button.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    
    This option is available since I provide an app.json file as per the guidelines found [here](https://devcenter.heroku.com/articles/heroku-button).
*******

- I created the web app using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
The secret key and other config variables were stored in an environment file during development. These variables are relevant to the Flask project and the issuance of email via the reset password option.

- On the Heroku website, using the dashboard, I entered the IP and PORT into the Heroku Config Vars fields (0.0.0.0 and 5000), along with my environment file's other variables.

- I also created a PostgreSQL database using the heroku command **"heroku addons:create heroku-postgresql:hobby-dev"**.

     I had to change from SQLite database (file based) to PostgreSQL on Heroku for my database to retain its contents once the website is deployed online. I commented out my local database and include the
link to the Heroku generated PostgreSQL database instead. I intialized the PostgreSQL database and pushed the migrations.

- According to the guidelines provided on Heroku [(link here)](https://devcenter.heroku.com/articles/deploying-python), I prepared the Heroku required files (Procfile and requirements.txt).
These documents indicate the language of the app to be deployed, along with its dependencies.
 **web: flask db upgrade; gunicorn -w 1 amphora:app**
  
    I changed the app environment to production and removed the debugging option.

- I then logged in my Heroku account and created an app (ci-vero-datacentric). A Heroku-hosted remote that’s associated with my app was created at the same time.
I linked my "nuagesdencre/ci-datacentric" Github repository to the Heroku app for deployment from its master branch. 

- I manually requested the deployment from the master branch.
 I reviewed the logs via the Heroku dashboard once the deployment confirmed and opened the app using my web browser to ensure everything was working properly.

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


## Testing
- #### Website Responsiveness
    - Overall Responsiveness and browser compatibility
    
        - [Browserling](www.browserling.com/)
        
            This website has been tested on multiple devices and browsers to ensure utmost responsiveness.
            I have also used the website 'Browserling' for that purpose.
    
- #### Home and Navigation

    **Navigation Bar**
    
    I. The navigation bar at the top of the screen displays the name 'Amphora' and if I click on it at any point while I am browsing, I am brought back to the home page.
    
    - I.I. When I visit the page using a large viewport, the navigation bar is at the top of the screen and displays the options available. An user icon indicates where I have to click for user-relevant options (login or register during my first visit).
    
    - I.II. While visiting using my smartphone, the navigation bar is triggered when I click on the hamburger menu at the top-left of the screen. The user-related options are highlighted in the menu.
    
    ##### Elements affected by user status
    II. If I am logged in, the user options available in the navigation bar change: 'Login' and 'Register' are replaced by 'Profile' and 'Logout'.
    If I click on 'Log Out', an alert message advises me that I successfully logged out and I am brought back to the home page, from wherever I was on the website. The user-relevant are defaulted to 'Login' and 'Register'.
    
    **Information displayed**
    
    I. The home page displays an introductory paragraph along with two pictures and quotes. The website is responsive, so the position of these elements change according to the size of the viewport used.
    
    **Footer**
    
    I. The footer remains identical on all pages of the website. It includes the Github logo and if I click on it, a new window brings me to the Github profile of **nuagesdencre**. 
    
- #### Repository

    ##### While a visitor is anonymous:
    
    **Repository main page**
    
    I. The page displays a definition of repository, buttons and a list of the available entries split by type. These lists are paginated.
    
    II. Clicking on the button 'New Entry' gives two options to select from: "Add Entry: Story" and "Add Entry: Being". 
    Regardless of my choice, as I am not logged in, proceeding with the creation of an entry is not permitted. I am redirected to the login page.
    
    III. Clicking on the button "All Categories" leads me to the Category page.
    
    IV. Clicking on the button "Search All" brings me to the search query page.
    
    V. I can use the pagination to explore the repository and see further entries.
    
    VI. I can click on the link "Read more" of an entry to access the entry's detailed view.
    
    **Entries (Story and Being)**
    
    I. When I access an entry detail page, it display the subject of the entry (name or title); the name and avatar of the post's author; 
    the entry's meaning and associated values; the entry's category; the entry's source (external link); 
    the entry's content;  existing comments; the possibility to log in the leave a comment on the entry. There is also a button at the bottom of the page letting me return to the repository's main page.
    
    - I.I. At the top of the entry page, I can see breadcrumbs allowing me to know where exactly is the page within the repository. I can click on the active link part of the breadcrumb to go back to the entry's parent page.

    II. I can click on the post author's name to access his/her profile page and view what this person has contributed to the website.
    
    III. I can click on the entry's category to see the category's page, where all associated entries are listed.
    
    IV. I can click on the external link given as the source of the entry. A new browser window opens and bring me to the url provided by the post author.
    
    **Categories**
    
    I. I can access the main category page ('Categories') by clicking on the Repository's 'All Categories' button.
        
    - I.I. If I click on a category via an entry, I am led to that specific category's page. I can access all categories via the breadcrumb path listed at the top of that page.
    
    II. The main category page lists all categories available using their name and an option to 'Read more' for each. A 'New Category' button is displayed at the top of the list.
    
    III. If I click on the 'New Category' button, I can create a new category without having to log in by providing a name and a description.
    The name field allows for 6 to 60 characters; the description field allows between 6 and 550 characters. An error message appears if these requirements are not met when I click the submit button ('Done!').
    If the requirements are met, a loading animation appears at the bottom of the form while the data is added to the repository's record and I am redirected to the main category page once that this action is completed.
    The new category tops the list displayed on the main category page.
               
    IV. If I click on a category's 'Read more' button, I am led to the category's detailed view. 
    The category page displays the the category's name; the entries associated to the category (separated by types); an 'Update Category' button and a 'Return' button.
           
    - IV.I. At the top of the category page, I can see breadcrumbs allowing me to know where exactly is the page within the repository. I can click on the active link part of the breadcrumb to go back to the category's parent page.
           
    - IV.II. If no entry has been recorded against a specific category, the category's detailed page will show instead '
    No story under this category yet.' or 'No being under this category yet.'.
    
    V. Clicking the 'Update Category' will present me with an editable version of the category's current name and description. I can modify both and click 'Done!' to update the records, or click 'Return' to go back to the categories main page.
       
    #####  While a visitor is logged in:
    
    **Repository main page**

    I. The page displays a definition of repository, buttons and a list of the available entries split by type. These lists are paginated.
    
    II. Clicking on the button 'New Entry' gives two options to select from: "Add Entry: Story" and "Add Entry: Being". **see Entries below**
    
    III. Clicking on the button "All Categories" leads me to the Category page.
    
    IV. Clicking on the button "Search All" brings me to the search query page.
    
    V. I can use the pagination to explore the repository and see further entries.
    
    VI. I can click on the link "Read more" of an entry to access the entry's detailed view.
    
    **Entries (Story and Being)**
    
    I. When clicking on the button 'New Entry', if I select one of the option, I am brought to a 'Create Story' or 'Create Being' page, where can create a new entry by providing the required information.
            
    - New Entry: Story
        - The required fields are: title; text; associated meanings and values; reference (url); category.
        - The category field is pre-populated with a selection of available categories (all currently in the database).
        - An error message appears if the requirements for various fields are not met when I click the submit button ('Done!').
    
    - New Entry: Being
        - The required fields are: name; text; associated meanings and values; reference (url); category.
        - The category field is pre-populated with a selection of available categories (all currently in the database).
        - An error message appears if the requirements for various fields are not met when I click the submit button ('Done!').

    Both pages have been manually tested with incorrect data to ensure relevance of the error messages.
    
    - I.I. If the requirements are met, a loading animation appears at the bottom of the form while the data is added to the repository's record and I am redirected to the main repository page once that this action is completed.
    The new entry tops its respective list on the main repository page. Newer entries are shown before the older ones.
    
    - I.III. Clicking on the 'Return' button while creating a new entry brings me back to the main repository page.
        
    II.When I access an entry detail page, it display the subject of the entry (name or title); the name and avatar of the post's author; 
    the entry's meaning and associated values; the entry's category; the entry's source (external link); 
    the entry's content; existing comments; the possibility to leave a comment on the entry. There is also a button at the bottom of the page letting me return to the repository's main page.
    
    - Ia. At the top of the entry page, I can see breadcrumbs allowing me to know where exactly is the page within the repository. I can click on the active link part of the breadcrumb to go back to the entry's parent page.

    III. I can click on the post author's name to access his/her profile page and view what this person has contributed to the website.
        
    - III.I. If the post author is me, additional options are available next to my username. I am able to edit my entry or delete it.
        
    - III.II. If I choose to edit my entry, I click on the blue pen (which has a tooltip confirming its purpose on hover). It brings me
    to a page where all of the entry's fields are pre-populated with the current data. The fields are editable and changes are confirmed if their requirements are met when I click 'Done'. 
        
        - III.II.I. When I click 'Done', I am redirected to the entry's detailed view.
        
        - III.II.II. If I click the 'Return' button instead while editing my entry, I am brought back to the Repository's main page. 
    
    - III.III. If I choose to delete my entry, I click on the red bin icon (which has a tooltip to confirm its function on hover). A modal pops up to confirm if I really want to delete my entry. 
     I have an option to 'Delete' and also to 'Go back'.
    
    IV. I can click on the entry's category to see the category's page, where all associated entries are listed.
    
    V. I can click on the external link given as the source of the entry. A new browser window opens and bring me to the url provided by the post author.
    
    VI. I can submit comments to the posts that are authored by others. 
        
    - VI.I. There is a note that comments can be viewed by everyone and cannot be edited or deleted. This comment feature is offered to visitors in good faith.
        
    - VI.II. An error message appears if the requirements for the comments fields (subject and comments)are not met when I click the submit button ('Done!').
         These fields been manually tested with incorrect data to ensure relevance of the error messages.
    
    **Categories**
    
    I. I can access the main category page ('Categories') by clicking on the Repository's 'All Categories' button.
        
    - I.I. If I click on a category via an entry, I am led to that specific category's page. I can access all categories via the breadcrumb path listed at the top of that page.
    
    II. The main category page lists all categories available using their name and an option to 'Read more' for each. A 'New Category' button is displayed at the top of the list.
    
    III. If I click on the 'New Category' button, I can create a new category without having to log in by providing a name and a description.
    The name field allows for 6 to 60 characters; the description field allows between 6 and 550 characters. An error message appears if these requirements are not met when I click the submit button ('Done!').
    If the requirements are met, a loading animation appears at the bottom of the form while the data is added to the repository's record and I am redirected to the main category page once that this action is completed.
    The new category tops the list displayed on the main category page.
               
    IV. If I click on a category's 'Read more' button, I am led to the category's detailed view. 
    The category page displays the the category's name; the entries associated to the category (separated by types); an 'Update Category' button and a 'Return' button.
           
    - IV.I. At the top of the category page, I can see breadcrumbs allowing me to know where exactly is the page within the repository. I can click on the active link part of the breadcrumb to go back to the category's parent page.
           
    - V.II. If no entry has been recorded against a specific category, the category's detailed page will show instead '
    No story under this category yet.' or 'No being under this category yet.'.
    
    V. Clicking the 'Update Category' will present me with an editable version of the category's current name and description. I can modify both and click 'Done!' to update the records, or click 'Return' to go back to the categories main page.
    

- #### About

   ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
   
- #### Contact

    ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
    - contact form
 
- #### Search

    ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
    - query page
    - search result
    
- #### User identification 
    - Register
    
    - Account and profile
        I. On the account page, my username and email address are displayed.
        
        II. I can update my email by typing in the editable field and clicking the 'Update email' button.
        
        III. I can access the content I provided so far on Amphora by clicking on 'Your Entries' button. This leads me to the detailed view of my profile 
        where entries, separated by type, and comments that I have authored are listed. Because I do not need to be logged in to create or edit a category, they are not included on my profile.
        I can click on any of the displayed content to access its location within Amphora directly.
        
    - Login
    
        I. When I log in, I need to provide my email and password.
         
            Ia. The login page displays a message reminding me that the fields are case-sensitive.
            
            Ib. There are two other links under the login input fields: a link leading to the 'register' page and another leading to the 'Forgot your password' option.
        
        II. Once logged in, I am redirected to my account page.
        
    - Logout 
        
        I. The logout option is only available in the navigation bar if I am logged in already.
        
        II. If I click on 'Log Out', an alert message advises me that I successfully logged out and I am brought back to the home page, from wherever I was on the website. The user-relevant are defaulted to 'Login' and 'Register'.
    
    - Password reset functionality
    
#### Python and Flask
   I ran the app in development mode by setting the FLASK_ENV=development environment variable in my environment file.
   I used the [Werkzeug Javascript's in-browser debugger](http://werkzeug.pocoo.org/) at length during this project and tackled the bugs uncovered one by one.
   It was most useful especially when I worked on the final page template.
   
   PyCharm was a wonderful tool to keep track of indentation and typos as well.

#### Javascript, CSS & HTML Validation

To the best of my ability, I conducted and documented tests to ensure that all of my website's functionality work well, while taking in account the user stories.

- [CSS Validation Service](http://jigsaw.w3.org/css-validator/)
    <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
        </a>
    </p>
     I ensured my CSS had no typos, errors or incorrect uses using The CSS Validation service.
     
     I also verified that all DOM elements were readable and easily accessible (i.e. no small links or buttons) on all viewports.

- [JSHINT](https://jshint.com/about/)
    
    - I used JSHINT to pinpoint any bug or typo in my scripts.

- [Nu Html Checker](https://validator.w3.org/nu/about.html)

    - I used the Nu checker to catch unintended mistakes in my Html documents, such as stand-alone tags.      

## Hurdles
- Search functionality

    - It took me a while to understand I need to use ILIKE operator in order to make the search in my database case-insensitive. [(reference)](https://docs.sqlalchemy.org/en/latest/orm/internals.html?highlight=ilike#sqlalchemy.orm.attributes.QueryableAttribute.ilike)
    - I also consulted this StackOverflow article [here](https://stackoverflow.com/questions/20336665/lower-like-vs-ilike?noredirect=1&lq=1)

- Transition from SQLAlchemy to Postgresql 
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

I thank my friends and family who visited Amphora, posted entries, tried to break the website and gave me feedback.
Once again, my mentor provided pointers, constructive criticism and advice that led me in the right direction.
 #### Thank you!
 ###
 
Please get in touch if you have any comments or questions.

vero@nuagesdencre.com