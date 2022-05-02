import cs50
from sys import argv, exit

if len(argv) != 2:
    print("usage: python roster.py name_house")
    exit(1)

факультет = argv[1]

db = cs50.SQL("sqlite:///students.db")
rows = db.execute("SELECT имя, отчество, фамилия, рождение FROM студенты WHERE факультет=? ORDER BY фамилия, имя", факультет) 
for row in rows:
    if row["отчество"] == "NULL":
        print(row["имя"], row["фамилия"] + ", родился в", row["рождение"])
    else:
        print(row["имя"], row["отчество"], row["фамилия"] + ", родился в", row["рождение"])

