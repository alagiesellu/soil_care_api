from vendors.cache import get_cache, set_cache
from vendors.db_models import User
from vendors.quries import get_db, current_user, add_record

db = get_db()

default_pin = 2022


def logout():
    """Logout the current user."""
    user = current_user()
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    # logout_user()


def check_phone(_app, username):

    user = User.query.get(username)

    if user:
        set_cache(username, default_pin)

        return True

    else:
        user = User(username)
        add_record(user)


def check_pin_against_phone(_app, pin, username):

    user = User.query.get(username)

    if user and get_cache(username) == pin:
        user.authenticated = True

        add_record(user)

        return user
        # return login_user(user, remember=True)