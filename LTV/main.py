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
csvfile = open('c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_smth.csv', 'r').readlines()
row_count = math.floor(len(csvfile) *0.7)  # количество строк в первый файл 70%
# print(row_count)

filename = 1
for i in range(len(csvfile)):
    if i == row_count:
        open("c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/"+ str(filename) + '.csv', 'w+').writelines(csvfile[i:i+100])
        filename += 1