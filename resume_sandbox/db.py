import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(current_app.config['DATABASE'])
        g.db.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        g.db.autocommit = True
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    curr = db.cursor()

    curr.execute(open('resume_sandbox/schema.sql','r', encoding='utf-8').read())

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
