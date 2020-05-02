from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_file
)
from werkzeug.exceptions import abort

from resume_sandbox.auth import login_required
from resume_sandbox.db import get_db

bp = Blueprint("sandbox", __name__)

@bp.route("/home", methods=("GET", "POST"))
def home():
    curr = get_db().cursor()
    curr.execute(
        "SELECT s.id, author_id, skill, entered, username"
        " FROM skills s JOIN siteuser u ON s.author_id = u.id"
        " ORDER BY entered DESC LIMIT 5"
    )
    skills = curr.fetchall()

    curr.execute(
        "SELECT s.id, author_id, position, company, url, notes, "
        "todo, deadline, applied, created FROM openings s JOIN siteuser u "
        "ON s.author_id = u.id ORDER BY created"
    )
    openings = curr.fetchall()

    ##Export to .txt
    if request.method == "POST":
        if request.form["submit_button"] == "Export!!!":
            #curr = get_db().cursor()

            ##pull skills from db for resume
            curr.execute("SELECT skill FROM skills")
            fetch1 = curr.fetchone()##only returns one skill; fetchmany()?

            ##pull job title from db for resume
            curr.execute("SELECT position FROM openings")
            fetch2 = curr.fetchone()

            ##pull company name from db for resume
            curr.execute("SELECT company FROM openings")
            fetch3 = curr.fetchone()

            with open('resume.txt', 'w') as f:
                f.write("Skills:\n")
                for i in fetch1:
                    f.write("%s\n" % i)
                f.write("\nJob Openings:\n")
                for j in fetch2:
                    f.write("%s at " % j)
                    for k in fetch3:
                        f.write("%s\n" % k)
                f.write("\nWork History:\n")
                f.write("\nEducation:\n")
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
            curr = get_db().cursor()
            curr.execute(
                "INSERT INTO skills (skill, author_id) VALUES (%s, %s)",
                (skill, g.user[0]),
            )
            #db.commit()
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
            curr = get_db().cursor()
            #print("I have made it here!")
            curr.execute(
                "INSERT INTO openings (position, company, url, "
                "deadline, notes, todo, author_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (position, company, url, deadline, notes, todo, g.user[0]),
            )
            #db.commit()
            return redirect(url_for("sandbox.home"))

    return render_template("sandbox/openings.html")
