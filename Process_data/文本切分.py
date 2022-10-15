from operator import index
import pandas as pd

#---需要人工改动的位置---
pattern = 1  # 第一次整理+切分，第二次根据不同关键词循环切分
pathname = "./4.xlsx"
savename = "./4_1.xlsx"
train_file = "data4.csv"
crime = 0 #! 0:受贿罪  1:帮信罪
# -------------------
if pattern == 0:
    keyword1 = "经审理查明"
    keyword2 = "上述事实"
    df = pd.read_excel(pathname)
    df2 = df[{'id','content'}].copy(deep=True)
    df2['caled'] = [0 for i in range(len(df))]
    # print(df2)
    for i in range(len(df)):
        text = df2.loc[i]['content']
        if pd.isnull(text):
            df2.loc[i, 'caled'] = -1
            continue
        if df2.loc[i, 'caled'] != 0:
            continue
        if "判决书" not in text:
            df2.loc[i, 'caled'] = -1
            continue

        index1 = text.find(keyword1)
        index2 = text.find(keyword2,index1)

        if index1 == -1 or index2 == -1:
            df2.loc[i, 'caled'] = 0
            continue


        facts = text[index1:index2]
        facts=facts.replace("\r\n","")
        facts=facts.replace("\n","")
        facts=facts.replace("\t","")
        facts=facts.replace(" ","")

        df2.loc[i, 'content'] = facts
        df2.loc[i, 'caled'] = 1

    df2.drop(df2[df2.caled == -1].index, inplace=True, axis=0)
    print(df2['caled'].value_counts())
    df2.to_excel(savename,index=None)

elif pattern==1:
    keywordlist1 = ["具体事实如下","经审理查明","经本院审理查明","经法庭审理查明","指控："]
    keywordlist2 = ["上述事实","以上事实","予以确认","予以采信","本院认为"]
    df2 = pd.read_excel(savename)
    # print(df2)
    for j1 in range(len(keywordlist1)):
        for j2 in range(len(keywordlist2)):
            for i in range(len(df2)):
                text = df2.loc[i]['content']
                if pd.isnull(text):
                    df2.loc[i, 'caled'] = -1
                    continue
                if df2.loc[i, 'caled'] != 0:
                    continue

                index1 = text.find(keywordlist1[j1])  
                index2 = text.find(keywordlist2[j2],index1)

                if index1 == -1 or index2 == -1:
                    df2.loc[i, 'caled'] = 0
                    continue
                if index1>index2:
                    df2.loc[i, 'caled'] = 0
                    continue
                facts = text[index1:index2]
                facts=facts.replace("\r\n","")
                facts=facts.replace("\n","")
                facts=facts.replace("\t","")
                facts=facts.replace(" ","")

                df2.loc[i, 'content'] = facts
                df2.loc[i, 'caled'] = 1

    df2.drop(df2[df2.caled == -1].index, inplace=True, axis=0)
    print(df2['caled'].value_counts())
    df2.to_excel(savename,index=None)

    df2.drop(df2[df2.caled == 0].index, inplace=True, axis=0)
    df2['label'] = [crime for k in range(len(df2))]
    df2[{'content','label'}].to_csv(train_file,sep=' ',index=None,columns = ['label','content'])
