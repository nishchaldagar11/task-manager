from extensions import db
from datetime import datetime

# ======================
# USER MODEL
# ======================
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20), default="user")

    # Relationship
    tasks = db.relationship('Task', foreign_keys='Task.created_by', backref='user', lazy=True)


# ======================
# TASK MODEL
# ======================
class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    remarks = db.Column(db.String(200))

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow)

    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'))