from vendors.quries import get_db

db = get_db()


class User(db.Model):

    username = db.Column(db.String, primary_key=True)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated


# class Soil(db.Model):
#
#     user_id = db.Column(db.String)
