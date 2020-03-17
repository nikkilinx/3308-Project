"""
build_db.py

Create by: Josh White
Date Modified: 3/16/2020

This script contains the helper functions 'create' and 'populate', which are
used by the script 'test_db.py' to do exactly what their names suggest in order
to verify the capabilities of the Resume Sandbox database defined in
'schema.sql'.

"""

import sqlite3

def create(dbname):
    conn = sqlite3.connect(
        dbname, detect_types=sqlite3.PARSE_DECLTYPES
    )
    conn.row_factory = sqlite3.Row

    with open('../schema.sql') as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

def populate(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Populate user table
    c.execute("INSERT INTO user (username, password) "
            "VALUES ('Josh', 'P@$$W0RD');"
    )
    c.execute("INSERT INTO user (username, password) "
            "VALUES ('David', '123456')"
    )

    # Populate resumes table
    c.execute("INSERT INTO resumes "
            "(author_id, title, file_path, notes) "
            "VALUES "
            "((SELECT id FROM user WHERE username='Josh'), "
            "'My Resume', 'Users/Documents/Resumes/', "
            "'This is my first resume!');"
    )
    c.execute("INSERT INTO resumes "
            "(author_id, title, file_path, notes) "
            "VALUES "
            "((SELECT id FROM user WHERE username='David'), "
            "'WIP1', 'D:/Docs/Resumes/', "
            "'This resume is a work in progress');"
    )

    # Populate skills table
    c.execute("INSERT INTO skills "
            "(author_id, skill) "
            "VALUES "
            "((SELECT id FROM user WHERE username='Josh'), "
            "'Catfishing');"
    )
    c.execute("INSERT INTO skills "
            "(author_id, skill) "
            "VALUES "
            "((SELECT id FROM user WHERE username='David'), "
            "'Juggling');"
    )

    # Populate openings table
    c.execute("INSERT INTO openings "
            "(author_id, position, company, url, notes, "
            "todo, deadline, applied) VALUES "
            "((SELECT id FROM user WHERE username='David'), "
            "'Lion Tamer', 'Barnum and Baileys', 'https://www.linkedin.com/', "
            "'I really like big cats!', 'Need to learn how to tame lions first.', "
            "'April 1', 'March 31');"
    )
    c.execute("INSERT INTO openings "
            "(author_id, position, company, url, notes, "
            "todo, deadline, applied) VALUES "
            "((SELECT id FROM user WHERE username='Josh'), "
            "'Pencil Pusher', 'Dimmsdale Pencil Co', 'https://www.geeksforgeeks.org/', "
            "'This job has great benefits.', 'Identify references', "
            "'April 22', 'February 14');"
    )

    conn.commit()
    conn.close()
