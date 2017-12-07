import sys
import MySQLdb as mc
import csv
connection = mc.connect (host = "localhost",
                         user = "root",
                         passwd = "HiGroup6!",
                         db = "Easycook")
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS Recipe")
cur.execute("DROP TABLE IF EXISTS Ingredient")
cur.execute("DROP TABLE IF EXISTS User")
cur.execute("DROP TABLE IF EXISTS Market")
cur.execute("DROP TABLE IF EXISTS Use_R")
cur.execute("DROP TABLE IF EXISTS Use_I")
cur.execute("DROP TABLE IF EXISTS Favorite_R")
cur.execute("DROP TABLE IF EXISTS Have_I")
cur.execute("DROP TABLE IF EXISTS Sell_I")


sql1 = '''CREATE TABLE IF NOT EXISTS Recipe (
    id_R         INTEGER AUTO_INCREMENT PRIMARY KEY,
    name_R       TEXT ,
    description  TEXT,
    calories     INTEGER,
    fat          INTEGER,
    protein      INTEGER,
    sodium       INTEGER,
    ingredients  TEXT,
    categories   TEXT,
    directions   TEXT,
    rating       FLOAT
);'''
cur.execute(sql1)


sql2 = '''CREATE TABLE IF NOT EXISTS Ingredient (
    id_I        INTEGER AUTO_INCREMENT PRIMARY KEY,
    name_I      TEXT,
    calories    INTEGER
);'''
cur.execute(sql2)

sql3 = '''CREATE TABLE IF NOT EXISTS Market (
    id_M        INTEGER AUTO_INCREMENT PRIMARY KEY,
    name_M      TEXT,
    country_M   TEXT
);'''
cur.execute(sql3)

sql4 = '''CREATE TABLE IF NOT EXISTS User (
    id_U        INTEGER AUTO_INCREMENT PRIMARY KEY,
    email       TEXT,
    nickname    TEXT,
    password    TEXT,
    country_U   TEXT
);'''
cur.execute(sql4)

sql5 = '''CREATE TABLE IF NOT EXISTS Use_R (
    id_R      INTEGER,
    id_U      INTEGER,
    rating    FLOAT,
    comment   TEXT,
    picture   TEXT,
    PRIMARY KEY (id_R, id_U)
);'''
cur.execute(sql5)

sql6 = '''CREATE TABLE IF NOT EXISTS Use_I (
    id_U      INTEGER,
    id_I      INTEGER,
    PRIMARY KEY (id_U, id_I)
);'''
cur.execute(sql6)

sql7 = '''CREATE TABLE IF NOT EXISTS Favorite_R (
    id_R      INTEGER,
    id_U      INTEGER,
    PRIMARY KEY (id_R, id_U)
);'''
cur.execute(sql7)

sql8 = '''CREATE TABLE IF NOT EXISTS Have_I (
    id_R      INTEGER,
    id_I      INTEGER,
    PRIMARY KEY (id_R, id_I)
);'''
cur.execute(sql8)

sql9 = '''CREATE TABLE IF NOT EXISTS Sell_I (
    id_M        INTEGER,
    id_I        INTEGER,
    unit_price  FLOAT,
    PRIMARY KEY (id_M, id_I)
);'''
cur.execute(sql9)

#Insert data into Recipe
cur.execute('''LOAD DATA LOCAL INFILE 'recipe_mysql.csv'
INTO TABLE `Recipe`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';''')

#
# with open('recipe_mysql.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         sql = '''INSERT INTO `Recipe`(`name_R`, `description`, `calories`, `fat`, `protein`, `sodium`, `ingredients`, `categories`, `directions`, `rating`)
#             VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'''%(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
#         try:
#             cur.execute(sql)
#             connection.commit()
#         except:
#             connection.rollback()

cur.close()
connection.close()
