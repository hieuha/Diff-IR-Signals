#!/usr/bin/python
from app import app

if __name__ == '__main__':
    app.secret_key = "rat phuc tap va an toan"
    app.run(host=app.config["HOST"],
            port=app.config["PORT"])
