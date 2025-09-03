from .extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    sender = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    received_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('emails', lazy=True))

    def __repr__(self):
        return f'<Email {self.id}>'

class AnalysisResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_phishing = db.Column(db.Boolean, nullable=False)
    score = db.Column(db.Float, nullable=False)
    details = db.Column(db.JSON, nullable=True)
    analyzed_at = db.Column(db.DateTime, default=datetime.utcnow)
    email_id = db.Column(db.Integer, db.ForeignKey('email.id'), nullable=False)

    email = db.relationship('Email', backref=db.backref('analysis_result', uselist=False))

    def __repr__(self):
        return f'<AnalysisResult {self.id}>'