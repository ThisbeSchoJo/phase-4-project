#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import DyeMaterial


# Views go here!

class AllDyeMaterials(Resource):
    def get(self):
        dye_materials = DyeMaterial.query.all()
        response_body = [material.to_dict(only=('id', 'name', 'base_color', 'image')) for material in dyeMaterials]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_material = DyeMaterial(
                name = request.json.get('name'),
                base_color=request.json.get('base_color'),
                image = request.json.get('image')
            )

            db.session.add(new_material)
            db.session.commit()
            response_body = new_material.to_dict(only = ('id','name', 'base_color', 'image'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllDyeMaterials, '/dyematerials')

class DyeMaterialByID(Resource):
    def get(self, id):
        dye_material = db.session.get(DyeMaterial, id)
        if dye_material:
            response_body = dye_material.to_dict(only=('id', 'name', 'base_color', 'image'))
            make_response(response_body, 200)
        else:
            response_body = {
                "error" : "Dye material not found!"
            }
            make_response(response_body, 404)

    def patch(self, id):
        dye_material = db.session.get(DyeMaterial, id)
        if dye_material:
            try:
                for attr in request.json:
                    setattr(dye_material, attr, request.json[attr])
                db.session.commit()
                response_body = dye_material.to_dict(only=('id', 'name', 'base_color', 'image'))
                return make_response(response_body, 200)
            except Exception as e:
                response_body = {
                    "error": str(e)
                }
                return make_response(response_body, 422)
        else:
            response_body = {
                "error": "Dye material not found!"
            }
            return make_response(response_body, 404)

    def delete(self, id):
        dye_material = db.session.get(DyeMaterial, id)
        if dye_material:
            db.session.delete(dye_material)
            db.session.commit()
            return make_response({}, 204)
        else:
            response_body = {
                "error": "Dye material not found!"
            }
            return make_response(response_body, 404)
            
api.add_resource(DyeMaterialByID, '/dyematerials/<int:id>')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)




# Authentication
    