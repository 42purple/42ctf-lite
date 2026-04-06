DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
);

INSERT INTO users (username, email, password) VALUES
('alice', 'alice@42madrid.com', '1234'),
('bob', 'bob@42madrid.com', 'bobby420'),
('charlie', 'charlie@42madrid.com', 'asdf'),
('ancarvaj', 'webminisdef@oc.mde.es', '1b0efb95aaf05748f873a468066d39da901f7f75de5db6be7bbb1859dc7fda63'),
('flag', 'getme@42madrid.com', 'dmVyeV93ZWFrX3Bhc3N3ZAo=')
;