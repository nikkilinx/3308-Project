import os

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = '3308',
        DATABASE = os.path.join(app.instance_path, 'resume_sandbox.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return render_template('base.html')

    ## Is this how we want to add additional webpages?
    @app.route('/about')
    def about():
	    return 'This is what you can accomplish on our webpage'

    from . import db
    db.init_app(app)

    return app
