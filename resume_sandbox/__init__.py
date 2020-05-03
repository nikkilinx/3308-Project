import os
from urllib.parse import urlparse

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    #url = urlparse(os.environ.get('DATABASE_URL'))
    #db = "dbname=%s user=%s password=%s host=%s" % (url.path[1:], url.username, url.password, url.hostname)
    db = "dbname='resume_sandbox' user='dbuser' host='localhost'"
    app.config.from_mapping(
        SECRET_KEY = '3308',
        DATABASE = db
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
    def base():
        return render_template('base.html')

    ## Is this how we want to add additional webpages?
    @app.route('/about')
    def about():
	    return render_template('sandbox/about.html')

    ## Exists but not used at this time
    @app.route('/resume')
    def resume():
        return render_template('sandbox/resume.html')

    from . import db
    db.init_app(app)

    from . import auth, sandbox
    app.register_blueprint(auth.bp)
    app.register_blueprint(sandbox.bp)

    return app
