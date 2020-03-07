DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS resumes;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);



CREATE TABLE resumes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  file_path TEXT NOT NULL,
  notes TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    skill TEXT NOT NULL,
    entered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    duties TEXT,
    FOREIGN KEY (author_id) REFERENCES user (id)
);
