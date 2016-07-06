import os
from flask import Blueprint, request, render_template, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app.data.models import Data
data = Data()
import pandas as pd

mod_data = Blueprint('data', __name__, url_prefix='/data')


@mod_data.route("/json/<string:filename>", methods=["GET"])
def json(filename=None):
    filename = secure_filename(filename)
    filename = data.root_folder + "/" + filename
    if data.is_exist(filename):
        response = data.to_json(filename)
    else:
        print "File not found!"
    return jsonify(response)