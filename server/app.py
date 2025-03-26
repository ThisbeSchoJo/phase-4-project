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

# class VolcanoByID(Resource):
#     def get(self, id):
#         volcano = db.session.get(Volcano, id)

#         if volcano:
#             response_body = volcano.to_dict(only=('id', 'location', 'image'))
#             return make_response(response_body, 200)
#         else:
#             response_body = {
#                 "error": "Volcano Not Found!"
#             }
#             return make_response(response_body, 404)
        
#     def patch(self, id):
#         volcano = db.session.get(Volcano, id)
#         if volcano:
#             try:
#                 for attr in request.json:
#                     setattr(volcano, attr, request.json[attr])
#                 db.session.commit()
#                 response_body = volcano.to_dict(only=('id', 'location', 'image'))
#                 return make_response(response_body, 200)
#             except:
#                 pass
#         else:
#             response_body = {
#                 "error": "Volcano Not Found!"
#             }
#             return make_response(response_body, 404)
#     def delete(self, id):
#         volcano = db.session.get(Volcano, id)
#         if volcano:
#             db.session.delete(volcano)
#             db.session.commit()
#             return make_response({}, 204)
#         else:
#             pass

# api.add_resource(VolcanoByID, '/volcanoes/<int:id>')


# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)




# # Authentication
# # 