import sqlite3
import resume_sandbox.db

def export_function(skills):
    ##skills = ''

    ##conn = sqlite3.connect(db)
    ##c  = conn.cursor()

    ##q = "SELECT * FROM skills;"
    ##c.execute(q)
    with open('testfile.txt', 'w') as f:
        f.write(str(skills))
        f.close()
    return(skills)
    ##conn.commit()
    ##conn.close()

def other_function():
    print('success')