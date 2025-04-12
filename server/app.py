#!/usr/bin/env python3

# Standard library imports
from sqlalchemy import select

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import DyeMaterial, Mordant, DyeResult


# Views go here!

@app.route('/')
def index():
    return "<h1>Welcome to Thisbe's Dye Shop!</h1>"

class AllDyeMaterials(Resource):
    def get(self):
        stmt = select(DyeMaterial)
        result = db.session.execute(stmt)
        dye_materials = result.scalars().all()
        response_body = [material.to_dict(only=('id', 'name', 'r', 'g', 'b', 'image', 'hex')) for material in dye_materials]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_material = DyeMaterial(
                name = request.json.get('name'),
                r = request.json.get('r'),
                g = request.json.get('g'),
                b = request.json.get('b'),
                image = request.json.get('image')
            )

            db.session.add(new_material)
            db.session.commit()
            response_body = new_material.to_dict(only = ('id','name', 'r', 'g', 'b', 'image', 'hex'))
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
            response_body = dye_material.to_dict(only=('id', 'name', 'r', 'g', 'b', 'image', 'hex'))
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
                response_body = dye_material.to_dict(only=('id', 'name', 'r', 'g', 'b', 'image', 'hex'))
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
        stmt = select(Mordant)
        result = db.session.execute(stmt)
        mordants = result.scalars().all()
        response_body = [mordant.to_dict(only=('id', 'name', 'r_effect', 'g_effect', 'b_effect', 'image')) for mordant in mordants]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_mordant = Mordant(
                name = request.json.get('name'),
                r_effect = request.json.get('r_effect'),
                g_effect = request.json.get('g_effect'),
                b_effect = request.json.get('b_effect'),
                image = request.json.get('image')
            )

            db.session.add(new_mordant)
            db.session.commit()
            response_body = new_mordant.to_dict(only = ('id', 'name', 'r_effect', 'g_effect', 'b_effect', 'image'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllMordants, '/mordants')

# MordantByID requests - get, patch, delete
class MordantByID(Resource):
    def get(self, id):
        mordant = db.session.get(Mordant, id)
        if mordant:
            response_body = mordant.to_dict(only=('id', 'name', 'r_effect', 'g_effect', 'b_effect', 'image'))
            return make_response(response_body, 200)
        else:
            response_body = {
                "error" : "Mordant not found!"
            }
            return make_response(response_body, 404)

    def patch(self, id):
        mordant = db.session.get(Mordant, id)
        if mordant:
            try:
                for attr in request.json:
                    setattr(mordant, attr, request.json[attr])
                db.session.commit()
                response_body = mordant.to_dict(only=('id', 'name', 'r_effect', 'g_effect', 'b_effect', 'image'))
                return make_response(response_body, 200)
            except Exception as e:
                response_body = {
                    "error": str(e)
                }
                return make_response(response_body, 422)
        else:
            response_body = {
                "error": "Mordant not found!"
            }
            return make_response(response_body, 404)

    def delete(self, id):
        mordant = db.session.get(Mordant, id)
        if mordant:
            db.session.delete(mordant)
            db.session.commit()
            return make_response({}, 204)
        else:
            response_body = {
                "error": "Mordant not found!"
            }
            return make_response(response_body, 404)
            
api.add_resource(MordantByID, '/mordants/<int:id>')


class AllDyeResults(Resource):
    def get(self):
        stmt = select(DyeResult)
        result = db.session.execute(stmt)
        dye_results = result.scalars().all()
        response_body = [result.to_dict(only=('id', 'dye_material_id', 'mordant_id', 'final_hex')) for result in dye_results]
        return make_response(response_body, 200)

    def post(self):
        try:
            new_dye_result = DyeResult(
                dye_material_id = request.json.get('dye_material_id'),
                mordant_id=request.json.get('mordant_id'),
                final_hex = request.json.get('final_hex')
            )

            db.session.add(new_dye_result)
            db.session.commit()
            response_body = new_dye_result.to_dict(only = ('id', 'dye_material_id', 'mordant_id', 'final_hex'))
            return make_response(response_body, 201)
        except Exception as e:
            response_body = {
                "error": str(e)
            }
            return make_response(response_body, 422)

api.add_resource(AllDyeResults, '/dye-results')


# DyeResultsByID requests - get, patch, delete
class DyeResultByID(Resource):
    def get(self, id):
        dye_result = db.session.get(DyeResult, id)
        if dye_result:
            response_body = dye_result.to_dict(only=('id', 'dye_material_id', 'mordant_id', 'final_hex'))
            return make_response(response_body, 200)
        else:
            response_body = {
                "error" : "Dye Result not found!"
            }
            return make_response(response_body, 404)

    def patch(self, id):
        dye_result = db.session.get(DyeResult, id)
        if dye_result:
            try:
                for attr in request.json:
                    setattr(dye_result, attr, request.json[attr])
                db.session.commit()
                response_body = dye_result.to_dict(only=('id', 'dye_material_id', 'mordant_id', 'final_hex'))
                return make_response(response_body, 200)
            except Exception as e:
                response_body = {
                    "error": str(e)
                }
                return make_response(response_body, 422)
        else:
            response_body = {
                "error": "Dye Result not found!"
            }
            return make_response(response_body, 404)

    def delete(self, id):
        dye_result = db.session.get(DyeResult, id)
        if dye_result:
            db.session.delete(dye_result)
            db.session.commit()
            return make_response({}, 204)
        else:
            response_body = {
                "error": "Dye Result not found!"
            }
            return make_response(response_body, 404)
            
api.add_resource(DyeResultByID, '/dye-results/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)




# Authentication
    