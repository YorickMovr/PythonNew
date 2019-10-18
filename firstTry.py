import csv
 
# def csv_reader(file_obj):
#     """
#     Read a csv file
#     """
#     reader = csv.reader(file_obj)
#     for row in reader:
#         print(" ".join(row))
 
# if __name__ == "__main__":
#     csv_path = "smth.csv"
#     with open(csv_path, "r") as f_obj:
#         csv_reader(f_obj)

import random
fid = open("smth.csv", "r")
li = fid.readlines()
fid.close()

random.shuffle(li)
print(li)

fid = open("shuffled_smth.csv", "w")
fid.writelines(li)
fid.close()