from app import app
from os import path, listdir
from flask import url_for
import pandas as pd

ALLOWED_EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]


class Data(object):

    def __init__(self):
        self.root_folder = app.config["BASE_DIR"] + "/data"

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def is_exist(self, filename):
        if path.exists(filename):
            return True
        return False

    def listing(self):
        files = list()
        for index, file in enumerate(listdir(self.root_folder)):
            index += 1
            url = url_for("dashboard.process", filename=file)
            url2 = url_for("dashboard.delete", filename=file)
            files.append((index, file, url, url2))
        return files

    def parsing(self):
        pass

    def diff(self, str1, str2):
        pass

    def headers(self, filename):
        headers = list()
        if self.is_exist(filename):
            df = pd.read_csv(filename)
            headers = df.columns
        return headers

    def to_json(self, filename):
        response = {"data": list()}
        if self.is_exist(filename):
            df = pd.read_csv(filename)
            headers = df.columns
            items = list()
            for value in df.values:
                item = dict(zip(headers, value))
                items.append(item)
            response = {"data": items}
        return response
