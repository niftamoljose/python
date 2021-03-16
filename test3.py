import csv
with open ("D:/20mca/stud.csv", newline="") as csvfile:
 data = csv.reader(csvfile, delimiter=" ", quotechar="|")
 for row in data:
    print(",".join(row))