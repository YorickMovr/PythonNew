import csv
import random
import math



# перемешать данные тут
fid = open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/smth.csv", "r")
li = fid.readlines()
fid.close()

random.shuffle(li)
# print(li)

fid = open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_smth.csv", "w")
fid.writelines(li)
fid.close()
# ---------------------------------
# делим файл тут
# не правильно работает 

# csvfile = open('c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_smth.csv', 'r').readlines()
# print(len(csvfile))
# print(csvfile[1][0])
# -------------------------------------
# row_sum = math.floor(len(csvfile) *0.7)
# print(row_sum)
# filename = 1
# for i in range(len(csvfile)):
#     if i< row_sum:
#         open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+row_sum])
        # filename +
# ----------------------------------------
# for i in range(len(csvfile)):
#      if i % 100 == 0:
#          open(str(filename) + '.csv', 'w+').writelines(csvfile[i:4])
#          filename += 1
# ----------------------------------------------
import os

def split(filehandler, delimiter=',', row_limit=1000,
          output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

split(open('c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_smth.csv', 20))