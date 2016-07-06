import os
from flask import Blueprint, request, render_template, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app.dashboard.models import Dashboard
from app.data.models import Data
import pandas as pd

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/')
dashboard = Dashboard()
data = Data()


@mod_dashboard.route("/", methods=["GET"])
def index():
    files = data.listing()
    return render_template("dashboard/index.html", files=files)


@mod_dashboard.route("upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and data.allowed_file(file.filename):
            print "hello"
            filename = secure_filename(file.filename)
            file.save(os.path.join(data.root_folder, filename))
            return redirect(url_for('dashboard.process', filename=filename))
    return render_template("dashboard/upload.html")


@mod_dashboard.route("process/<string:filename>", methods=["GET"])
def process(filename=None):
    filename = secure_filename(filename)
    json_url = url_for("data.json", filename=filename)
    filename = data.root_folder + "/" + filename
    headers = data.headers(filename)
    return render_template("dashboard/process.html", headers=headers,
                           json_url=json_url)


@mod_dashboard.route("delete/<string:filename>", methods=["GET"])
def delete(filename=None):
    filename = secure_filename(filename)
    filename = data.root_folder + "/" + filename
    response = {"status": False, "message": None}
    if data.is_exist(filename):
        os.remove(filename)
        response = {"status": True, "message": "Deleted!"}
    else:
        response = {"status": False, "message": "File not found!"}
    return jsonify(response)