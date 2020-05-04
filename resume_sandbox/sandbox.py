from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_file, send_from_directory
)
from werkzeug.exceptions import abort

from resume_sandbox.auth import login_required
from resume_sandbox.db import get_db

import sys
import psycopg2
import os

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

            ##pull skills from db for resume
            curr.execute(
            "SELECT skill, author_id FROM skills s"
            " JOIN siteuser u ON s.author_id = u.id"
            )
            fetch1 = curr.fetchall()

            ##pull job title from db for resume
            curr.execute(
            "SELECT position, author_id FROM openings o"
            " JOIN siteuser u ON o.author_id = u.id"
            )
            fetch2 = curr.fetchall()

            ##pull company name from db for resume
            curr.execute(
            "SELECT company, author_id FROM openings o"
            " JOIN siteuser u ON o.author_id = u.id"
            )
            fetch3 = curr.fetchall()
            p = os.getcwd()
            file = os.path.join(p, 'temp.txt')
            if os.path.exists(file):
                os.remove(file)
            with open(file, 'w') as f:
                f.write("Skills:\n")
                for i in fetch1:
                    f.write("%s\n" % i[0])
                f.write("\nJob Openings:\n")
                for j in fetch2:
                    if (fetch2 == None):
                        break
                    f.write("%s at " % j[0])
                    for k in fetch3:
                        f.write("%s\n" % k[0])
                f.write("\nWork History:\n")
                f.write("\nEducation:\n")
            ##return_resume(file)
            ##os.remove(file)
            ##send_file() returns attachment - temporary placeholder
            return send_file(file, mimetype="text/txt", attachment_filename='resume.txt', as_attachment=True, cache_timeout=0)
        else:
            pass
    return render_template("sandbox/home.html", skills=skills, openings=openings)

##Secondary function to return attachment - requires more work
def return_resume(fname):
    if os.path.exists(fname):
        return send_file(fname, mimetype="text/txt", attachment_filename='resume.txt', as_attachment=True)
    else:
        pass

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
