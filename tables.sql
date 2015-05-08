DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Projections;
DROP TABLE IF EXISTS Reservations;
pragma foreign_keys = on;


CREATE TABLE Movie(
  movie_id INTEGER PRIMARY KEY,
  movie_name TEXT,
  movie_rating INTEGER
);

CREATE TABLE Projections(
  projections_id INTEGER PRIMARY KEY,
  movie_id INTEGER,
  type TEXT,
  data DATE,
  time TEXT,
  FOREIGN KEY(movie_id) REFERENCES Movie(movie_id)
);

CREATE TABLE Reservations(
  reservations_id INTEGER PRIMARY KEY,
  username TEXT,
  projections_id INTEGER,
  row INTEGER,
  col INTEGER,
  FOREIGN KEY(projections_id) REFERENCES Projections(projections_id)
);

INSERT INTO Movie(movie_name, movie_rating) VALUES("The Hunger Games: Catching Fire", 7.9);
INSERT INTO Movie(movie_name, movie_rating) VALUES("Wreck-It Ralph", 7.8);
INSERT INTO Movie(movie_name, movie_rating) VALUES("Her", 8.3);

INSERT INTO Projections(movie_id, type, data, time) VALUES(1, "3D", 2014-04-01, "19:10");
INSERT INTO Projections(movie_id, type, data, time) VALUES(1, "2D", 2014-04-01, "19:00");
INSERT INTO Projections(movie_id, type, data, time) VALUES(1, "4DX", 2014-04-02, "21:00");
INSERT INTO Projections(movie_id, type, data, time) VALUES(3, "2D", 2014-04-05, "20:20");
INSERT INTO Projections(movie_id, type, data, time) VALUES(2, "3D", 2014-04-02, "22:00");
INSERT INTO Projections(movie_id, type, data, time) VALUES(2, "2D", 2014-04-02, "19:30");

INSERT INTO Reservations(username, projections_id, row, col) VALUES("RadoRado", 1, 2, 1);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("RadoRado", 1, 3, 5);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("RadoRado", 1, 7, 8);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("Ivo", 3, 1, 1);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("Ivo", 3, 1, 2);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("Mysterious", 5, 2, 3);
INSERT INTO Reservations(username, projections_id, row, col) VALUES("Mysterious", 5, 2, 4);
