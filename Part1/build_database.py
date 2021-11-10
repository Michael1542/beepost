import psycopg2

con = psycopg2.connect(database="postgres", user="michaelwang", password="Bruinbui4341!", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE GALLERY
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      TITLE           TEXT    NOT NULL,
      DATE            TEXT     NOT NULL,
      URL        TEXT        NOT NULL,
      DEPARTMENT        CHAR(50));''')
print("Table created successfully")

con.commit()
con.close()