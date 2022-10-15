import jieba
import pandas as pd
# 创建停用词列表


def stopwordslist():
    stopwords = [line.strip() for line in open(
        './stopword/stopwords.txt', encoding='gbk').readlines()]
    return stopwords

# 对句子进行中文分词


def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    # print("正在分词")
    sentence_depart = jieba.cut(sentence.replace("\n"," ").strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# 给出文档路径
filename = "./4.xlsx"
outfilename = "4_embedding.txt"

outputs = open(outfilename, 'w+', encoding='UTF-8')


read_file_name = "./4.xlsx"

df = pd.read_excel(read_file_name)

for text in df.content:
    seg_list = seg_depart(text) 
    print("------working------")
    outputs.write(seg_list)

outputs.close()
