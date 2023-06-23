from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('name')
    def validate_name(self, key, name_value):
        if name_value == '':
            raise ValueError("Name must be a string")
        return name_value
    @validates('phone_number')
    def validate_phone(self, key, phone_value):
        if len(phone_value) < 10:
            raise ValueError("Phone number must be 10 digits long")
        return phone_value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validates_title(self, key, title_value):
        if title_value == '':
            raise ValueError("Title must be a string")
        elif "Won't Believe" not in title_value and "Secret" not in title_value and "Top" not in title_value and "Guess" not in title_value:
            raise ValueError("Needs to be more clickbaity!")
        return title_value
    
    @validates('content')
    def validates_content(self, key, content):
        if len(content) <= 249:
            raise ValueError("Content too short test. Less than 250 chars.")
        return content
    
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary too long test. More than 250 chars.")
        return summary
    
    @validates('category')
    def validates_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError('Incorrect Category')
        return category


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
