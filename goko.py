import csv
import random
import math
import os
import sys
import io


MY_GL_FILE_PATH = "c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/qweqwe.csv"
MY_GL_PATH_TOSAVE = "c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/"





    # перемешать данные тут
# C:\Users\Ярослав\Downloads\orders_for_ltv.csv
with open(MY_GL_FILE_PATH,'r') as f:
        with open( MY_GL_PATH_TOSAVE +"smth.csv",'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)
    # os.remove('c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/output_2.csv')


fid = open(MY_GL_FILE_PATH,'r')
li = fid.readlines()
maxcount = len(li)-1
fid.close()
# print(maxcount)



def doShuffle(filePath,fileName) :
    while fileName <=5:
        fid = open(str(filePath), "r")
        li = fid.readlines()
        fid.close()

        random.shuffle(li)

        fid = open(MY_GL_PATH_TOSAVE +str(fileName) +"_shuffled.csv", "w", newline='')
        fid.writelines(li)
        fid.close()

def getBigPartCount():
    fid = open(MY_GL_PATH_TOSAVE + "smth.csv", "r")
    li = fid.readlines()
    # print(len(li))
    bigPart = math.floor(len(li)*0.7)
    fid.close()
    return bigPart-1
    # print(bigPart)

def removeErFirst():
    with open(MY_GL_PATH_TOSAVE +  "output_2.csv",'r') as f:
        with open(MY_GL_PATH_TOSAVE + "NEW_output_2.csv",'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)
    os.remove(MY_GL_PATH_TOSAVE + 'output_2.csv')

def split(filehandler, delimiter=',', row_limit= getBigPartCount(),
    output_name_template=MY_GL_PATH_TOSAVE  +'_output_%s.csv', output_path='.', keep_headers=True):

        import csv

        reader = csv.reader(filehandler, delimiter=delimiter)
        current_piece = 1
        current_out_path = os.path.join(
            output_path,
            output_name_template  % current_piece
        )
        current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
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
                current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)



# ----------------------------------------------------------------------------------------------
def init(filePath):
    # doShuffle(filePath)
    split(open(MY_GL_PATH_TOSAVE + "1_shuffled.csv", "r"))
    removeErFirst()


# init(MY_GL_PATH_TOSAVE+'smth.csv')
# ------------------------------------------------------------------------------------------------
# split(open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/orders_for_ltv.csv", "r"))


def get_csv_row_value(file_name, names=None, usecols=None, mode='r', encoding="utf8",
            quoting=csv.QUOTE_ALL,
            delimiter=',',
            as_obj=False):

    class RowObject:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    with open(file_name, mode=mode, encoding=encoding) as csvfile:
        data_reader = csv.reader(csvfile, quoting=quoting, delimiter=delimiter)
        for row in data_reader:
            if usecols and names:
                q = dict(zip(names, (row[i] for i in usecols)))
                yield q if not as_obj else RowObject(**q)
            elif usecols and not names:
                yield list(row[i] for i in usecols)
            elif names and not usecols:
                q = dict(zip(names, (row[k] for k, i in enumerate(row))))
                yield q if not as_obj else RowObject(**q)
            else:
                yield row




def get_your_POhIBKA(fileName):
    placeholder = MY_GL_PATH_TOSAVE + 'smth.csv'
    vs
# filename = MY_GL_PATH_TOSAVE + 'smth.csv'
# vs = get_csv_row_value(filename, names=( 'rew'))
# sum = 0
# for item in vs:
#     # print(len(vs))
#     # print(item['w'])
#     sum =sum + int(item['w'])
# print(sum/1000)


def doSomePrityThings(filePath):
    fileName =1
    while fileName <=5:
        doShuffle(filePath,fileName)
    # split(open(MY_GL_PATH_TOSAVE + fileName + '_shuffled.csv'),'r')
    fileName = fileName +1


doSomePrityThings(MY_GL_FILE_PATH)


