import csv
with open("D:/20mca/stud.csv",newline="") as csvfile:
    data = csv.DictReader (csvfile)
    print ("name")
    for col in  data:
        print (col['name'])