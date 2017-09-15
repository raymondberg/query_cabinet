DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_sequence;
CREATE SEQUENCE users_id_sequence START 1;
CREATE TABLE users (id integer PRIMARY KEY DEFAULT nextval('users_id_sequence'), name varchar, email varchar);

INSERT INTO users (name, email) VALUES
 ('BamBam Rubble', 'bam@example.com'),
 ('Barney Rubble', 'barn@example.com'),
 ('Betty Rubble', 'betty@example.com'),
 ('Fred Flintstone', 'freddy@example.com'),
 ('Pebbles Flintstone', 'pebbles@example.com'),
 ('Wilma Flintstone', 'wilmaexample.com');

