from amphora import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# 3 tables:
# user
# story
# being


@login_manager.user_loader()
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(72), unique=True, index=True)
    psw_hash = db.Column(db.String(128))
    profile_pic = db.Column(db.String(72), nullable=False, default='amphora_profile.png')
    # relationships
    stories = db.relationship('Story', backref='author', lazy=True)
    beings = db.relationship('Being', backref='author', lazy=True)

    # user set up
    def __init__(self, username, email, psw):
        self.username = username
        self.email = email
        self.psw_hash = generate_password_hash(psw)

    # user self-representation
    def __repr__(self):
        return "Username {}".format(self.username)


    # password check
    def psw_check(self, psw):
        return check_password_hash(self.password_hash, psw)


class Story():

    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False, unique=True, index=True)
    country = db.Column(db.String(60), nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(60), index=True)
    # relationships
    users = db.relationship('User', backref='user', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, country, text, category):
        self.title = title
        self.country = country
        self.text = text
        self.category = category

    def __repr__(self):
        return "Story title: {}".format(self.title)

class Being():

    __tablename__ = 'beings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True, index=True)
    country = db.Column(db.String(60), nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(60), index=True)
    # relationships
    users = db.relationship('User', backref='user', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, country, text, category):
        self.name = name
        self.country = country
        self.text = text
        self.category = category

    def __repr__(self):
        return "Being name: {}".format(self.name)