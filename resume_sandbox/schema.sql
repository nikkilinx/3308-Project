DROP TABLE IF EXISTS siteuser;
DROP TABLE IF EXISTS resumes;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS experience;
DROP TABLE IF EXISTS openings;

CREATE TABLE siteuser (
  ID SERIAL PRIMARY KEY NOT NULL,
  USERNAME TEXT UNIQUE NOT NULL,
  PASSWORD TEXT NOT NULL
);

CREATE TABLE resumes (
  ID  SERIAL  PRIMARY KEY,
  AUTHOR_ID INTEGER NOT NULL,
  CREATED TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
  TITLE TEXT  NOT NULL,
  FILE_PATH TEXT  NOT NULL,
  NOTES TEXT  NOT NULL,
  FOREIGN KEY (AUTHOR_ID) REFERENCES SITEUSER (ID)
);

CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    skill TEXT NOT NULL,
    entered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES siteuser (id)
);

CREATE TABLE experience (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    duties TEXT,
    FOREIGN KEY (author_id) REFERENCES siteuser (id)
);

CREATE TABLE openings (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    position TEXT NOT NULL,
    company TEXT NOT NULL,
    url TEXT NOT NULL,
    notes TEXT,
    todo TEXT,
    deadline TEXT,
    applied TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES siteuser (id)
);
