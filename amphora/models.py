from amphora import db, login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time
import jwt


@login_manager.user_loader
def load_user(user_id):
    """
    Reload the user object from the user ID stored in the session
    """
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(72), unique=True, index=True)
    psw_hash = db.Column(db.String(128))
    # relationships
    # One author for many entries - stories & beings
    stories = db.relationship('Story', backref='user', lazy=True)
    beings = db.relationship('Being', backref='user', lazy=True)

    def __init__(self, username, email, psw):
        """
        Initialize user object
        """
        self.username = username
        self.email = email
        self.psw_hash = generate_password_hash(psw)

    def __repr__(self):
        """
        Set user self-representation
        """
        return "Username {}".format(self.username)

    def set_password(self, psw):
        """
        Set a new password (useful for psw reset)
        """
        self.psw_hash = generate_password_hash(psw)

    # password check
    def psw_check(self, psw):
        """
        Check if the password hash of the inputted password
        matches the hash on file
        """
        return check_password_hash(self.psw_hash, psw)

    #
    def get_reset_password_token(self, expires_in=600):
        """
        Generate a JWT token as a string following a password reset request
        """
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        """
        Decode the JWT token associated to the password reset request
        """
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def avatar(self, size):
        """
        Import user avatars using gravatar
        """
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Story(db.Model):
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False, unique=True, index=True)
    meaning = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text)
    source = db.Column(db.String(100), default='None provided')
    # relationships
    # one user_id per entry
    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # one category per entry(story, being)
    categories = db.relationship('Category')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # many comments per entry
    comments = db.relationship('Comment', backref='comments', lazy=True)

    def __init__(self, title, text, meaning, category_id, source, user_id):
        """
        Initialize story object
        """
        self.title = title
        self.text = text
        self.meaning = meaning
        self.category_id = category_id
        self.source = source
        self.user_id = user_id

    def __repr__(self):
        """
        Set story self-representation
        """
        return "Story title: {}".format(self.title)


class Being(db.Model):
    __tablename__ = 'beings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True, index=True)
    meaning = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text)
    picture = db.Column(db.String(72), default='amphora_default.png')
    source = db.Column(db.String(100), default='None provided')
    # relationships
    # one user_id per entry
    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # one category per entry(story, being)
    categories = db.relationship('Category')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # many comments per entry
    comments = db.relationship('Comment', backref='comments', lazy=True)

    def __init__(self, name, text, meaning, category_id, source, user_id):
        """
        Initialize being object
        """
        self.name = name
        self.text = text
        self.meaning = meaning
        self.category_id = category_id
        self.source = source
        self.user_id = user_id

    def __repr__(self):
        """
        Set being self-representation
        """
        return "Being name: {}".format(self.name)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True, index=True)
    description = db.Column(db.Text)
    # relationships
    # many entries(story, being) per category
    stories = db.relationship('Story', backref='category', lazy=True)
    beings = db.relationship('Being', backref='category', lazy=True)

    def __init__(self, name, description):
        """
        Initialize being object
        """
        self.name = name
        self.description = description

    def __repr__(self):
        """
        Set category self-representation
        """
        return "Category name: {}".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(60), nullable=False)
    content = db.Column(db.Text)
    # relationships
    # one user_id per comment
    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, subject, content, user_id):
        """
        Initialize being object
        """
        self.subject = subject
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        """
        Set category self-representation
        """
        return "Comment '{}' made by {}".format(self.subject, self.user_id)