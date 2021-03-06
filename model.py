"""Models and database functions for cattexts."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#*****************************************************************************#

class User(db.Model):
    """User model"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    timezone = db.Column(db.String(100), nullable=False)    
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide useful info when printed to console"""

        s = "<User user_id=%s email=%s timezone=%s>"

        return s % (self.user_id, self.email, self.timezone)

class Cat(db.Model):
    """Cat model"""

    __tablename__ = "cats"

    cat_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False) # foreign key to users
    name = db.Column(db.String(20), nullable=False)
    dinner_time = db.Column(db.DateTime, nullable=False)
    snack = db.Column(db.String(20), nullable=False)
    activity1 = db.Column(db.String(20), nullable=False)
    activity2 = db.Column(db.String(20), nullable=False)
    toy1 = db.Column(db.String(20), nullable=False)
    toy2 = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", backref=db.backref("cats"))

    def __repr__(self):
        """Provide useful info when printed to console"""

        s = "<cat cat_id=%s name=%s>"

        return s % (self.cat_id, self.name)

#*****************************************************************************#

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our Postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cattexts'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

    db.create_all()
