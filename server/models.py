from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class DyeMaterial(db.Model, SerializerMixin):
    __tablename__ = 'dye_materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    base_color = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    dye_results = db.relationship('DyeResult', back_populates='dye_material')

    @validates('name', 'base_color', 'image')
    def validate_location(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 3:
            raise ValueError(f"{column_name} must be at least 3 characters long!")
        else:
            return value
        
    def __repr__(self):
        return f"<Dye Material {self.id} - Name: {self.name}, Base Color: {self.base_color}, Image: {self.image}>"
    

class Mordant(db.Model, SerializerMixin):
    __tablename__ = 'mordants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    effect = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    dye_results = db.relationship('DyeResult', back_populates='mordant')

    @validates('name', 'effect', 'image')
    def validate_location(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 3:
            raise ValueError(f"{column_name} must be at least 3 characters long!")
        else:
            return value
        
    def __repr__(self):
        return f"<Mordant {self.id} - Name: {self.name}, Effect: {self.effect}, Image: {self.image}>"


class DyeResult(db.Model, SerializerMixin):
    __tablename__ = 'dye_results'

    id = db.Column(db.Integer, primary_key=True)
    dye_material_id = db.Column(db.Integer, db.ForeignKey('dye_materials.id'), nullable=False)
    mordant_id = db.Column(db.Integer,db.ForeignKey('mordants.id'), nullable=False)
    resulting_color = db.Column(db.String, nullable=False)
    intensity = db.Column(db.Integer, nullable=False)

    dye_material=db.relationship('DyeMaterial', back_populates='dye_results')
    mordant = db.relationship('Mordant', back_populates='dye_results')

    @validates('name', 'effect', 'image')
    def validate_location(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 3:
            raise ValueError(f"{column_name} must be at least 3 characters long!")
        else:
            return value
        
    def __repr__(self):
        return f"<Dye Result {self.id}, Dye Material ID: {self.dye_material_id}, Mordant ID: {self.mordant_id}, Resulting Color: {self.resulting_color}, Intensity: {self.intensity}>"
