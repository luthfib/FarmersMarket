from flask import Flask, render_template, make_response, redirect
from flask.ext.restful import Api, Resource, reqparse, abort

import json
import string
import random


# Load data from disk.
# This simply loads the data from our "database," which is just a JSON file.
with open('data.json') as data:
    data = json.load(data)


# Generate a unique ID for a new farm.
# By default this will consist of six lowercase numbers and letters.
def generate_id(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Respond with 404 Not Found if no farm with the specified ID exists.
def error_if_farm_not_found(farm_id):
    if farm_id not in data['farms']:
        message = "No farm with ID: {}".format(farm_id)
        abort(404, message=message)


# Given the data for a farm, generate an HTML representation
# of that farm.
def render_farm_as_html(farm):
    return render_template('farm.html', farm=farm)


# Given the data for a list of farms, generate an HTML representation
# of that list.
def render_farm_list_as_html(farms):
    return render_template('farms.html', farms=farms)


# Raises an error if the string x is empty (has zero length).
def nonempty_string(x):
    s = str(x)
    if len(x) == 0:
        raise ValueError('string is empty')
    return s


# Specify the data necessary to create a new farm.
new_farm_parser = reqparse.RequestParser()
for arg in ['name', 'description']:
    new_farm_parser.add_argument(
        arg, type=nonempty_string, required=True,
        help="'{}' is a required value".format(arg))
new_farm_parser.add_argument(
    'products', type=nonempty_string, required=True, action='append',
    help="'{}' is a required value".format(arg))


# Define our farm resource.
class Farm(Resource):

    # If a farm with the specified ID does not exist,
    # respond with a 404, otherwise respond with an HTML representation.
    def get(self, farm_id):
        error_if_farm_not_found(farm_id)
        return make_response(
            render_farm_as_html(
                data['farms'][farm_id]), 200)


# Define our farm list resource.
class FarmList(Resource):

    # Respond with an HTML representation of the farm list.
    def get(self):
        return make_response(
            render_farm_list_as_html(data['farms']), 200)

    # Add a new farm to the list, and respond with an HTML
    # representation of the updated list.
    def post(self):
        farm = new_farm_parser.parse_args()
        farm_id = generate_id()
        farm['@id'] = 'request/' + farm_id
        data['farms'][farm_id] = farm
        return make_response(
            render_farm_list_as_html(data['farms']), 201)


# Assign URL paths to our resources.
app = Flask(__name__)
api = Api(app)
api.add_resource(FarmList, '/requests')
api.add_resource(Farm, '/request/<string:farm_id>')


# Redirect from the index to the list of farms.
@app.route('/')
def index():
    return redirect(api.url_for(FarmList), code=303)


# Start the server.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
