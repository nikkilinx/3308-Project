from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
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

    op1 = db.execute(
        "SELECT s.id, author_id, position, company, url, notes, "
        "deadline, applied, created, todo FROM openings s JOIN user u "
        "ON s.author_id = u.id ORDER BY created"
    )
    openings = op1.fetchall()
    return render_template("sandbox/home.html", skills=skills, openings=openings)

##Skills input
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


##Job Openings page
@bp.route("/openings", methods=("GET", "POST"))
@login_required
def openings():
    """Enter new job opening"""
    if request.method == "POST":
        position = request.form["position"]
        company = request.form["company"]
        url = request.form["url"]
        deadline = request.form["deadline"]
        todo = request.form["todo"]
        notes = request.form["notes"]
        error = None

        if not position:
            error.append("Enter a job opening.")
        if not company:
            error.append("Enter a company name.")
        if not url:
            error.append("Enter a link to the job opening.")

        if error is not None:
            flash(error)
        else:
            db = get_db()
            print("I have made it here!")
            db.execute(
                "INSERT INTO openings (position, company, url, "
                "deadline, notes, todo, author_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (position, company, url, deadline, notes, todo, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("sandbox.home"))

    return render_template("sandbox/openings.html")
