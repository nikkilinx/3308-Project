"""
build_db.py

Create by: Josh White
Date Modified: 3/16/2020

This script contains the helper functions 'create' and 'populate', which are
used by the script 'test_db.py' to do exactly what their names suggest in order
to verify the capabilities of the Resume Sandbox database defined in
'schema.sql'.

"""

import psycopg2

def populate(db):

    c = db.cursor()
    with open('../schema.sql','r', encoding='utf-8') as f:
        c.execute(f.read())

    # Populate user table
    c.execute("INSERT INTO siteuser (username, password) "
            "VALUES ('Josh', 'P@$$W0RD');"
    )
    c.execute("INSERT INTO siteuser (username, password) "
            "VALUES ('David', '123456')"
    )

    # Populate resumes table
    c.execute("INSERT INTO resumes "
            "(author_id, title, file_path, notes) "
            "VALUES "
            "((SELECT id FROM siteuser WHERE username='Josh'), "
            "'My Resume', 'Users/Documents/Resumes/', "
            "'This is my first resume!');"
    )
    c.execute("INSERT INTO resumes "
            "(author_id, title, file_path, notes) "
            "VALUES "
            "((SELECT id FROM siteuser WHERE username='David'), "
            "'WIP1', 'D:/Docs/Resumes/', "
            "'This resume is a work in progress');"
    )

    # Populate skills table
    c.execute("INSERT INTO skills "
            "(author_id, skill) "
            "VALUES "
            "((SELECT id FROM siteuser WHERE username='Josh'), "
            "'Catfishing');"
    )
    c.execute("INSERT INTO skills "
            "(author_id, skill) "
            "VALUES "
            "((SELECT id FROM siteuser WHERE username='David'), "
            "'Juggling');"
    )

    # Populate openings table
    c.execute("INSERT INTO openings "
            "(author_id, position, company, url, notes, "
            "todo, deadline, applied) VALUES "
            "((SELECT id FROM siteuser WHERE username='David'), "
            "'Lion Tamer', 'Barnum and Baileys', 'https://www.linkedin.com/', "
            "'I really like big cats!', 'Need to learn how to tame lions first.', "
            "'April 1', 'March 31');"
    )
    c.execute("INSERT INTO openings "
            "(author_id, position, company, url, notes, "
            "todo, deadline, applied) VALUES "
            "((SELECT id FROM siteuser WHERE username='Josh'), "
            "'Pencil Pusher', 'Dimmsdale Pencil Co', 'https://www.geeksforgeeks.org/', "
            "'This job has great benefits.', 'Identify references', "
            "'April 22', 'February 14');"
    )

    # Populate experience table
    c.execute("INSERT INTO experience "
            "(author_id, title, company, start_date, end_date, duties) "
            "VALUES ((SELECT id FROM siteuser WHERE username='David'), "
            "'Bag Boy', 'Safeway', '2012-15-07', '2014-15-09', 'Bag stuff.');"
            )
    c.execute("INSERT INTO experience "
            "(author_id, title, company, start_date, end_date, duties) "
            "VALUES ((SELECT id FROM siteuser WHERE username='Josh'), "
            "'Programmer', 'Google', '2018-05-01', '2020-10-08', "
            "'Update Google Maps backend code.');"
            )

    db.commit()
