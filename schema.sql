DROP TABLE IF EXISTS users;

CREATE TABLE users (
    username TEXT NOT NULL UNIQUE,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    userpassword TEXT NOT NULL
);