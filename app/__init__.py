from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("../config.py")


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.dashboard.controllers import mod_dashboard as dashboard
from app.data.controllers import mod_data as data

app.register_blueprint(dashboard)
app.register_blueprint(data)