mysql -h hackathon.cgbbgydmzqnb.us-east-2.rds.amazonaws.com -u admin -p

USE TrumpBot;

CREATE TABLE Headline(
    text VARCHAR(400) PRIMARY KEY,
    posted TINYINT(1)
);