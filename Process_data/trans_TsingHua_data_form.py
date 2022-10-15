import pandas as pd

# train_path = "valid"


# f = open("attributes", 'r',encoding="ISO-8859-1")
# wri = open("class.txt",encoding="ISO-8859-1",mode="w+")
# content = f.readlines()
# for i in content:
#     z = i.strip().split("\t")
#     wri.write(z[2]+"\n")
# f.close()
# wri.close()
train_path = "test"
f = open(train_path, "r",encoding='ISO-8859-1')
wri = open(train_path+".txt",encoding="ISO-8859-1",mode="w+")
content = f.readlines()
# 读入train文件
for i in content:
    z = i.strip().split("\t")
    if(len(z) != 3):
        continue
    z[0]=z[0].replace(" ","")
    tmp =  z[1].strip().split()[0]
        
    wri.write(z[0]+"\t"+tmp+"\t"+z[2]+"\n")
    
f.close()
wri.close()
