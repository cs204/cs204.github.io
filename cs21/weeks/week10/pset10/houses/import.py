# TODO
from sys import argv, exit
import csv
import cs50
if len(argv) != 2:
    print("using python import.py file.csv")
    exit(1)

open("students.db", "w").close()

db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE студенты(id INTEGER, имя VARCHAR(255), отчество VARCHAR(255), фамилия VARCHAR(255), факультет VARCHAR(10), рождение NUMERIC, PRIMARY KEY(id))")

fname = argv[1]

with open(fname, "r") as file_csv:
    reader = csv.DictReader(file_csv)
    for row in reader:
        names = row["имя"].split()
        if len(names) == 3:
            db.execute("INSERT INTO студенты(имя, отчество, фамилия, факультет, рождение)  VALUES(?, ?, ?, ?, ?)", names[0], names[1], names[2], row["факультет"], row["рождение"])
        elif len(names) == 2:
            db.execute("INSERT INTO студенты(имя, отчество, фамилия, факультет, рождение) VALUES(?, ?, ?, ?, ?)", names[0], "NULL" , names[1],  row["факультет"], row["рождение"])
        else:
            raise ValueError("wrong number of names")



