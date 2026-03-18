from extensions import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(20))   # NEW

    status = db.Column(db.String(20))
    remarks = db.Column(db.String(200))

    created_on = db.Column(db.DateTime, default=datetime.utcnow)  # NEW
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow) # NEW

    created_by = db.Column(db.String(50))
    updated_by = db.Column(db.String(50))