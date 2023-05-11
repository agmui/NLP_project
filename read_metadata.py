# import csv
#
# with open('./Project_CodeNet/metadata/p00000.csv', mode = 'r') as csvfile:
#     spamreader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(row)

import pandas
# reading the CSV file
csvFile = pandas.read_csv('./Project_CodeNet/metadata/p00000.csv')
# displaying the contents of the CSV file
print(csvFile["problem_id"], csvFile["submission_id"])
