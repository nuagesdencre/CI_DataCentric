from amphora import db
# 3 tables:
# user
# story
# being


class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), nullable=False, unique=True, index=True)
    email = db.Column(db.String(72), unique=True, index=True)
    profile_pic = db.Column(db.String(72), nullable=False, default='amphora_profile.png')


class Story():

    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False, unique=True, index=True)


class Being():
    __tablename__ = 'beings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False, unique=True, index=True)
