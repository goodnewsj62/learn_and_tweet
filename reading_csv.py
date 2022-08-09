import csv

headers = ["food","color"]
rows = [("rice","white")]

with open("file.csv", "w") as f:
    csv_obj =csv.writer(f,delimiter=":")
    csv_obj.writerow(headers)
    csv_obj.writerows(rows)
#RESULT in file.csv:
#food:color
#rice:white

with open("file.csv", "r") as f:
    csv_rows = csv.reader(f,delimiter=":")

    for row in csv_rows:
        """do some stuff"""

# another option of writing and reading using DictReader is available also

header =  ["food","color"]
items = [{"food":"rice","color":"white"}, {"food":"stake","color":"brown"}]
with open("file1.csv", "w") as f:
    csv_obj = csv.DictWriter(f,fieldnames=header,delimiter=":")
    csv_obj.writeheader()
    csv_obj.writerows(items)