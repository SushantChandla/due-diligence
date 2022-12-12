from flask import Blueprint, request, jsonify

from random import choice
import json

blueprint = Blueprint('loan', __name__)

@blueprint.route('/', methods=['POST'])
def loan():
    details = request.form
    print(details)
    return jsonify(choice([True, False]))
