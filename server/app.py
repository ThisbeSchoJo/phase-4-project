#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import DyeMaterial, Mordant, DyeResult


# Views go here!

class AllDyeMaterials(Resource):
    def get(self):
        dye_materials = DyeMaterial.query.all()
        response_body = [material.to_dict(only=('id', 'name', 'base_color', 'image')) for material in dye_materials]
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

api.add_resource(AllDyeMaterials, '/dye-materials')

class DyeMaterialByID(Resource):
    def get(self, id):
        dye_material = db.session.get(DyeMaterial, id)
        if dye_material:
            response_body = dye_material.to_dict(only=('id', 'name', 'base_color', 'image'))
            return make_response(response_body, 200)
        else:
            response_body = {
                "error" : "Dye material not found!"
            }
            return make_response(response_body, 404)

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
            
api.add_resource(DyeMaterialByID, '/dye-materials/<int:id>')


class AllMordants(Resource):
    def get(self):
        mordants = Mordant.query.all()
        response_body = [mordant.to_dict(only=('id', 'name', 'effect', 'image')) for mordant in mordants]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_mordant = Mordant(
                name = request.json.get('name'),
                effect=request.json.get('effect'),
                image = request.json.get('image')
            )

            db.session.add(new_mordant)
            db.session.commit()
            response_body = new_mordant.to_dict(only = ('id','name', 'effect', 'image'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllMordants, '/mordants')



# Add create and read actions for each resource
class AllDyeResults(Resource):
    def get(self):
        dye_results = DyeResult.query.all()
        response_body = [result.to_dict(only=('id', 'dye_material_id', 'mordant_id', 'resulting_color', 'intensity')) for result in dye_results]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_dye_result = DyeResult(
                dye_material_id = request.json.get('dye_material_id'),
                mordant_id=request.json.get('mordant_id'),
                resulting_color = request.json.get('resulting_color'),
                intensity = request.json.get('intensity')
            )

            db.session.add(new_dye_result)
            db.session.commit()
            response_body = new_dye_result.to_dict(only = ('id', 'dye_material_id', 'mordant_id', 'resulting_color', 'intensity'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllDyeResults, '/dye-results')


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)




# Authentication
    