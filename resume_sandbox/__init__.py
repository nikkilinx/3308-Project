import os
from urllib.parse import urlparse

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    url = urlparse(os.environ['DATABASE_URL'])
    #db = "dbname=%s user=%s password=%s host=%s" % (url.path[1:], url.username, url.password, url.hostname)
    db = f"dbname={url.path[1:]} user={url.username} password={url.password} host={url.hostname} port={url.port} sslmode=require"
    #db = "dbname=dej170joc0ll2 user=essrjztaqfkqua password=7f20a5bcfa03daaa6d9fc1667e2c50f38ecdf8863db163f73cff03250b3cfee3 host=ec2-50-17-90-177.compute-1.amazonaws.com port=5432 sslmode=require"
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
    def index():
        return render_template('sandbox/index.html')

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
