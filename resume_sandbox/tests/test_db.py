"""
test_db.py

Create by: Josh White
Date Modified: 3/16/2020

This script contains unit tests to verify the capabilities of the Resume Sandbox
database defined in 'schema.sql'. To execute this script, simply type:

>>> python3 test_db.py

"""

import unittest
import build_db
import os
import psycopg2
import testing.postgresql

class SandboxdbTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()
        self.postgresql.db_conf = self.postgresql.dsn()
        self.postgresql.con = psycopg2.connect(**self.postgresql.db_conf)
        self.postgresql.con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        build_db.populate(self.postgresql.con)


    def tearDown(self):
        self.postgresql.con.close()
        self.postgresql.stop()

    def test_user(self):
        print("\nTesting 'siteuser' table functionality. . .")
        c = self.postgresql.con.cursor()
        result = 'David'
        c.execute("SELECT username FROM siteuser WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected user username")
        result = 'P@$$W0RD'
        c.execute("SELECT password FROM siteuser WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected user password")
        print("Passed!")

    def test_resumes(self):
        print("\nTesting 'resumes' table functionality. . .")
        c = self.postgresql.con.cursor()
        result = 1
        c.execute("SELECT author_id FROM resumes WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected resumes author_id")
        result = 'My Resume'
        c.execute("SELECT title FROM resumes WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected resumes title")
        result = 'D:/Docs/Resumes/'
        c.execute("SELECT file_path FROM resumes WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected resumes file_path")
        result = 'This is my first resume!'
        c.execute("SELECT notes FROM resumes WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected resumes notes")
        print("Passed!")

    def test_skills(self):
        print("\nTesting 'skills' table functionality. . .")
        c = self.postgresql.con.cursor()
        result = 2
        c.execute("SELECT author_id FROM skills WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected skills author_id")
        result = 'Catfishing'
        c.execute("SELECT skill FROM skills WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected skills skill")
        print("Passed!")

    def test_openings(self):
        print("\nTesting 'openings' table functionality. . .")
        c = self.postgresql.con.cursor()
        result = 2
        c.execute("SELECT author_id FROM openings WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings author_id")
        result = 'Pencil Pusher'
        c.execute("SELECT position FROM openings WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings position")
        result = 'Barnum and Baileys'
        c.execute("SELECT company FROM openings WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings company")
        result = 'https://www.geeksforgeeks.org/'
        c.execute("SELECT url FROM openings WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings url")
        result = 'I really like big cats!'
        c.execute("SELECT notes FROM openings WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings notes")
        result = 'Identify references'
        c.execute("SELECT todo FROM openings WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings todo")
        result = 'April 1'
        c.execute("SELECT deadline FROM openings WHERE id=1;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings deadline")
        result = 'February 14'
        c.execute("SELECT applied FROM openings WHERE id=2;")
        test_val = c.fetchone()
        self.assertEqual(result, test_val[0], "'result' does not match expected openings applied")
        print("Passed!")

if __name__ == '__main__':
    unittest.main()
