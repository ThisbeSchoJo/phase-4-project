from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class Volcano(db.Model, SerializerMixin):
    __tablename__ = 'volcanoes'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    @validates('location', 'image')
    def validate_location(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 4:
            raise ValueError(f"{column_name} must be at least 5 characters long!")
        else:
            return value
        
    def __repr__(self):
        return f"<Volcano {self.id} - Location: {self.location}, Image: {self.image}>"
