from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_file, send_from_directory, session
)
import os
from resume_sandbox.db import get_db
import psycopg2

def export_resume():
    curr = get_db().cursor()

    ##pull skills from db for resume
    curr.execute(
    "SELECT skill, author_id FROM skills"
    " WHERE author_id = %s", (g.user[0],)
    )
    skills = curr.fetchall()

    ##pull job title from db for current openings
    curr.execute(
    "SELECT position, author_id FROM openings"
    " WHERE author_id = %s", (g.user[0],)
    )
    op_position = curr.fetchall()

    ##pull company name from db for current openings
    curr.execute(
    "SELECT company, author_id FROM openings"
    " WHERE author_id = %s", (g.user[0],)
    )
    op_company = curr.fetchall()

    ##pull job title from db for past experience
    curr.execute(
    "SELECT title, author_id FROM experience"
    " WHERE author_id = %s", (g.user[0],)
    )
    exp_position = curr.fetchall()

    ##pull company name from db for experience
    curr.execute(
    "SELECT company, author_id FROM experience"
    " WHERE author_id = %s", (g.user[0],)
    )
    exp_company = curr.fetchall()

    file = os.path.join(os.getcwd(), 'temp.txt')

    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w') as f:
        f.write("%s's Resume\n" % g.user[1])
        f.write("<><><><><><><><><><><><><><><><><><><><><><>\n")
        f.write("Skills:\n")
        for i in skills:
            f.write("%s\n" % i[0])

        f.write("\nPrevious Experience:\n")
        for i in exp_position:
            if (exp_position == None):
                break
            f.write("%s at " % i[0])
            for j in exp_company:
                f.write("%s\n" % j[0])

        f.write("\nJob Openings:\n")
        for i in op_position:
            if (op_position == None):
                break
            f.write("%s at " % i[0])
            for j in op_company:
                f.write("%s\n" % j[0])

    return file
