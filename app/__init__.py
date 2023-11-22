from flask import Flask

app = Flask(__name__)

from .tasks.routes import task

app.register_blueprint(task)
