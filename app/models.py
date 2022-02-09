from app import db

class UserSigninInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(90), nullable=False)
    email = db.Column(db.String(90), nullable=False)
    password = db.Column(db.String(90), nullable=False)