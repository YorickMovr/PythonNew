import csv
import random
import math


fileName = 1
def doShuffle(filePath):
        # перемешать данные тут
        fid = open(str(filePath), "r")
        li = fid.readlines()
        # print(li[0:7])
        fid.close()

        random.shuffle(li)
        # print(li[0:7])

        fid = open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_"+str(fileName)+".csv", "w")
        fid.writelines(li)
        fid.close()
# ---------------------------------
# делим файл тут
# не правильно работает 
# ---------------------------------------------------------------
# fid = open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_"+str(fileName)+".csv", "r")
# li = fid.readlines()
# bigPart = math.floor(len(li)*0.7)
# fid.close()
# print(bigPart)
# -------------------------------------------------------
# import os

def split(filehandler, delimiter=',', row_limit= 50,
    output_name_template='c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/output_%s.csv', output_path='.', keep_headers=True):

        import csv
# ----------------------
        fid = open("c:/Uers/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_"+str(fileName)+".csv", "r")
        li = fid.readlines()
        bigPart = math.floor(len(li)*0.7)
        row_limit = bigPart
        fid.close()
        print(bigPart)
# -----------------------
        reader = csv.reader(filehandler, delimiter=delimiter)
        current_piece = 1
        current_out_path = os.path.join(
            output_path,
            output_name_template  % current_piece
        )
        current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
        current_limit = row_limit
        if keep_headers:
            headers=next(reader)
            current_out_writer.writerow(headers)
        for i, row in enumerate(reader):
            if i + 1 > current_limit:
                current_piece += 1
                current_limit = row_limit * current_piece
                current_out_path = os.path.join(
                    output_path,
                    output_name_template  % current_piece
                )
                current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)



doShuffle("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/smth.csv")
split(open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_1.csv", "r"))