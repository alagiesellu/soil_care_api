from vendors.cache import get_cache
from vendors.db_models import User
from vendors.quries import get_db, current_user

db = get_db()


def logout():
    """Logout the current user."""
    user = current_user()
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    # logout_user()


def check_pin_against_phone(_app, pin, phone):

    user = User.query.get(phone)

    if user and get_cache(phone) == pin:
        user.authenticated = True
        db.session.add(user)
        db.session.commit()

        return user
        # return login_user(user, remember=True)