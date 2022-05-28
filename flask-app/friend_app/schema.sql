DROP TABLE IF EXISTS friend;

CREATE TABLE friend (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

INSERT INTO friend (name) VALUES ('Tsuki');
INSERT INTO friend (name) VALUES ('Goon');
INSERT INTO friend (name) VALUES ('Joe');