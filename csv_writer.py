import csv
students = [
    {"name" : "Jon", "age" :23, "id" : 2},
    {"name" : "Jane", "age" :22, "id" : 5}

]

with open("new_data.csv", "w") as cw:
    csv_writer = csv.DictWriter(cw, fieldnames=students[0].keys(), delimiter = "\t")
    csv_writer.writeheader()
    for i in students:
        csv_writer.writerow(i)