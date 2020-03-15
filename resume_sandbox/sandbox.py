from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import send_file
from werkzeug.exceptions import abort

from resume_sandbox.auth import login_required
from resume_sandbox.db import get_db
from resume_sandbox.export import export_function

bp = Blueprint("sandbox", __name__)

@bp.route("/home", methods=("GET", "POST"))
def home():
    db = get_db()
    sk1 = db.execute(
        "SELECT s.id, skill, author_id, entered, username"
        " FROM skills s JOIN user u ON s.author_id = u.id"
        " ORDER BY entered DESC LIMIT 5"
    )
    skills = sk1.fetchall()
    if request.method == "POST":
        if request.form["submit_button"] == "Export!!!":
            db = get_db()
            sk1 = db.execute("SELECT s.id, skill, author_id, entered, username"
            " FROM skills s JOIN user u ON s.author_id = u.id")
            fetch = sk1.fetchone()
            with open('new.txt', 'w') as f:
                for i in fetch:
                    f.write("%s\n" % i)
                f.close()
            return send_file('new.txt', mimetype='text/txt', attachment_filename='new.txt', as_attachment=True)
        else:
            pass
    return render_template("sandbox/home.html", skills=skills)


@bp.route("/skills", methods=("GET", "POST"))
@login_required
def skills():
    """Enter new skills"""
    if request.method == "POST":
        skill = request.form["skill"]
        error = None

        if not skill:
            error = "Enter a skill."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO skills (skill, author_id) VALUES (?, ?)",
                (skill, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("sandbox.home"))


    return render_template("sandbox/skills.html")
