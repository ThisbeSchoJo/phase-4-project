from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class DyeMaterial(db.Model, SerializerMixin):
    __tablename__ = 'dye_materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    r = db.Column(db.Integer, nullable=False)
    g = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)

    dye_results = db.relationship('DyeResult', back_populates='dye_material')

    serialize_only = ('id', 'name', 'image', 'r', 'g', 'b', 'hex')
    serialize_rules = ('-dye_results.dye_material',)

    @validates('name', 'image')
    def validate_name(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 3:
            raise ValueError(f"{column_name} must be at least 3 characters long!")
        else:
            return value
        
    @validates('r', 'g', 'b')
    def validate_rgb(self, column_name, value):
        if type(value) != int:
            raise TypeError(f"{column_name} must be an integer!")
        elif not (0 <= value <= 255):
            raise ValueError(f"{column_name} must be between 0 and 255!")
        else:
            return value
        
    @property
    def hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __repr__(self):
        return f"<Dye Material {self.id} - Name: {self.name}, Base Color: {self.r}{self.g}{self.b}, Image: {self.image}>"
    
class Mordant(db.Model, SerializerMixin):
    __tablename__ = 'mordants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    image = db.Column(db.String, nullable=False)
    r_effect = db.Column(db.Integer, nullable=False) 
    g_effect = db.Column(db.Integer, nullable=False)
    b_effect = db.Column(db.Integer, nullable=False)

    dye_results = db.relationship('DyeResult', back_populates='mordant')

    @validates('name', 'image')
    def validate_name(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) < 3:
            raise ValueError(f"{column_name} must be at least 3 characters long!")
        else:
            return value
        
    @validates('r_effect', 'g_effect', 'b_effect')
    def validate_effect(self, column_name, value):
        if type(value) != int:
            raise TypeError(f"{column_name} must be an integer!")
        elif value < -255 or value > 255:
            raise ValueError(f"{column_name} must be between -255 and 255!")
        else:
            return value
        
    def __repr__(self):
        return f"<Mordant {self.id} - Name: {self.name}, Effects: ({self.r_effect}, {self.g_effect}, {self.b_effect},) Image: {self.image}>"
    

class DyeResult(db.Model, SerializerMixin):
    __tablename__ = 'dye_results'

    id = db.Column(db.Integer, primary_key=True)
    dye_material_id = db.Column(db.Integer, db.ForeignKey('dye_materials.id'), nullable=False)
    mordant_id = db.Column(db.Integer,db.ForeignKey('mordants.id'), nullable=False)
    final_hex = db.Column(db.String, nullable=False)
    # resulting_color = db.Column(db.String, nullable=False)
    # intensity = db.Column(db.Integer, nullable=False)

    dye_material=db.relationship('DyeMaterial', back_populates='dye_results')
    mordant = db.relationship('Mordant', back_populates='dye_results')

    serialize_rules = ('-dye_material.dye_results', '-mordant.dye_results')

    @validates('final_hex')
    def validate_hex(self, column_name, value):
        if type(value) != str:
            raise TypeError(f"{column_name} must be a string!")
        elif len(value) != 7:
            raise ValueError(f"{column_name} must be in hex format (e.g. #000000)!")
        else:
            return value
        
    def __repr__(self):
        return f"<Dye Result {self.id}, Dye Material ID: {self.dye_material_id}, Mordant ID: {self.mordant_id}, Final Hex: {self.final_hex}>"