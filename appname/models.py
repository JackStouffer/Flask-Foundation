from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db, login_manager


db = SQLAlchemy()


class Permission:
    PERMISSION_1 = 0x01
    PERMISSION_2 = 0x02
    PERMISSION_3 = 0x04
    PERMISSION_4 = 0x08
    PERMISSION_5 = 0x10
    PERMISSION_6 = 0x20
    PERMISSION_7 = 0x40
    PERMISSION_8 = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.PERMISSION_1, True),
            'Manager': (Permission.PERMISSION_1 |
                        Permission.PERMISSION_2 |
                        Permission.PERMISSION_3 |
                        Permission.PERMISSION_4, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return not self.is_authenticated

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username
