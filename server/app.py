#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Volcano


# Views go here!

class AllVolcanoes(Resource):
    def get(self):
        volcanoes = Volcano.query.all()
        response_body = [volcano.to_dict(only=('id', 'location', 'image')) for volcano in volcanoes]
        return make_response(response_body, 200)

api.add_resource(AllVolcanoes, '/volcanoes')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

