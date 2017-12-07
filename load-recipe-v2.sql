CREATE TABLE IF NOT EXISTS Recipe (
    name_R       VARCHAR(512) UNIQUE KEY,
    description  TEXT,
    calories     INTEGER,
    fat          INTEGER,
    protein      INTEGER,
    sodium       INTEGER,
    ingredients  TEXT,
    categories   TEXT,
    directions   TEXT,
    rating       FLOAT,
    id_R         INTEGER AUTO_INCREMENT PRIMARY KEY
);

LOAD DATA LOCAL INFILE 'recipe_mysql.csv'
INTO TABLE `Recipe`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';