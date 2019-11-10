import random

f1 = open("new_data_legit.csv","r",encoding="UTF-8")
f1_out = open("new_data_legit_out.csv","a",encoding="UTF-8")

f2 = open("new_data.csv","r",encoding="UTF-8")
f2_out = open("new_data_phishing_out.csv","a",encoding="UTF-8")

data = f1.read()
rows = data.split("\n")
index = 1
for row in rows:
    if (len(row.split(',')) < 30):
        continue
    f1_out.write(str(index)+","+row[:len(row)-1]+random.choice(['-1','1'])+",-1\n")
    index += 1

data = f2.read()
rows = data.split("\n")
index = 166
for row in rows:
    if (len(row.split(',')) < 30):
        continue
    f2_out.write(str(index)+","+row[:len(row)-1]+random.choice(['-1','1'])+",1\n")
    index += 1