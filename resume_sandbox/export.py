import os
from resume_sandbox.db import get_db
import psycopg2

def export_resume():
    curr = get_db().cursor()

    ##pull skills from db for resume
    curr.execute(
    "SELECT skill, author_id FROM skills s"
    " JOIN siteuser u ON s.author_id = u.id"
    )
    skills = curr.fetchall()

    ##pull job title from db for current openings
    curr.execute(
    "SELECT position, author_id FROM openings o"
    " JOIN siteuser u ON o.author_id = u.id"
    )
    op_position = curr.fetchall()

    ##pull company name from db for current openings
    curr.execute(
    "SELECT company, author_id FROM openings o"
    " JOIN siteuser u ON o.author_id = u.id"
    )
    op_company = curr.fetchall()

    ##pull job title from db for past experience
    curr.execute(
    "SELECT title, author_id FROM experience e"
    " JOIN siteuser u ON e.author_id = u.id"
    )
    exp_position = curr.fetchall()

    ##pull company name from db for experience
    curr.execute(
    "SELECT company, author_id FROM experience e"
    " JOIN siteuser u ON e.author_id = u.id"
    )
    exp_company = curr.fetchall()

    file = os.path.join(os.getcwd(), 'temp.txt')

    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w') as f:
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
