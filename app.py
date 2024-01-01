from flask import Flask, request, redirect, url_for, jsonify, render_template
from flask_migrate import Migrate
from extensions import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Initialize extensions
    # api.init_app(app)
    # db.init_app(app)
    # admin.init_app(app)
    # jwt.init_app(app)
    migrate.init_app(app, db)

    # api.authorizations = {
    #     'apikey': {
    #         'type': 'apiKey',
    #         'in': 'header',  # Place the token in the header
    #         'name': 'Authorization'  # Header name for the token
    #     }
    # }

    # Register blueprints and other settings

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
