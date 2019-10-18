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

csvfile = open('c:/Users/Ярослав/Documents/GitHub/PythonNew/LTV/shuffled_smth.csv', 'r').readlines()

filename = 1
for i in range(len(csvfile)):
     if i % 10 == 0:
         open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+1000])
         filename += 1