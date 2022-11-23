from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def add_record(record):
    db.session.add(record)
    db.session.commit()


def create_db(_app):

    with _app.app_context():
        db.create_all()


def init_db(_app):

    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///soil_care.db"
    db.init_app(_app)


def get_db():
    return db


def current_user():
    return None