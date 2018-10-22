from amphora import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



@login_manager.user_loader
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
    stories = db.relationship('Story', backref='user', lazy=True)
    # One author for many stories & beings
    beings = db.relationship('Being', backref='user', lazy=True)

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
        return check_password_hash(self.psw_hash, psw)

    # look for all authored entries
    # def list_stories(self):
    #     print("Entries for this username:")
    #     for story in self.stories:
    #         return story
    # def list_beings(self):
    #     for being in self.beings:
    #         return being


class Story(db.Model):

    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False, unique=True, index=True)
    country = db.Column(db.String(60), nullable=False, index=True)
    text = db.Column(db.Text)
    category = db.Column(db.String(60), index=True)
    # relationships
    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, text, country, category, user_id):
        self.title = title
        self.text = text
        self.country = country
        self.category = category
        self.user_id = user_id

    def __repr__(self):
        return "Story title: {}".format(self.title)


class Being(db.Model):

    __tablename__ = 'beings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True, index=True)
    country = db.Column(db.String(60), nullable=False, index=True)
    text = db.Column(db.Text)
    category = db.Column(db.String(60), index=True)
    # relationships
    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, text, country, category, user_id):
        self.name = name
        self.text = text
        self.country = country
        self.category = category
        self.user_id = user_id

    def __repr__(self):
        return "Being name: {}".format(self.name)