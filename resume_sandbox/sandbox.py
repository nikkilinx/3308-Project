from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from resume_sandbox.auth import login_required
from resume_sandbox.db import get_db

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

##Export * from skills into html template
@bp.route("/resume", methods=("GET", "POST"))
@login_required
def export():
    print("hi")
    db = get_db()
    db.execute("SELECT * FROM skills")
    return render_template("sandbox/resume.html")
