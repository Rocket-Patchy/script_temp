import sys
import csv

input_file = sys.argv[1]

dialect_dict = csv.excel
dialect_dict.delimiter = ','

with open(input_file, encoding='utf-8', newline='') as test_file:
    reader = csv.DictReader(test_file, dialect=dialect_dict)

    for row in reader:
        print(row)
