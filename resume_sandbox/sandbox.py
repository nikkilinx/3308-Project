from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_file
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

    ##Export
    if request.method == "POST":
        if request.form["submit_button"] == "Export!!!":
            db = get_db()
            sk1 = db.execute("SELECT s.id, skill, author_id, entered, username"
            " FROM skills s JOIN user u ON s.author_id = u.id")
            fetch = sk1.fetchone()
            sk2 = db.execute("SELECT s.id, author_id, position, company, url, notes, "
            "deadline, applied, created, todo FROM openings s JOIN user u "
            "ON s.author_id = u.id")
            fetch2 = sk2.fetchone()
            with open('resume.txt', 'w') as f:
                f.write("HERE ARE YOUR SKILLS:\n")
                for i in fetch:
                    f.write("%s\n" % i)
                f.write("\nHERE ARE THE OPENINGS:\n")
                for j in fetch2:
                    f.write("%s\n" % j)
                f.close()
            return send_file('resume.txt', mimetype='text/txt', attachment_filename='resume.txt', as_attachment=True)
        else:
            pass
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
