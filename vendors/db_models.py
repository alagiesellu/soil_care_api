from vendors.quries import get_db

db = get_db()


class User(db.Model):

    phone = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)


    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.phone


    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated