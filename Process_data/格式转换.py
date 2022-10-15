import json
import pandas as pd
import numpy as np
user_dict = {}
list_s=[]
with open("帮助信息网络犯罪活动罪裁判文书.txt","r",encoding="utf-8",errors='ignore') as f:
    for userline in f:
        # userline=userline.replace("\n","")
        # userline=userline.replace('\\','\\\\')
        # userline=userline.replace("}",',}')
        # userline=userline.replace("'","")  
        userline=userline.replace(" ","")
        userline=userline.replace("\n","")
        userline=userline.replace("\t","")
        userline=eval(userline)
        list_s.append(userline)


# print(list_s)
# columns_name = {"id", "doc_id", "browse_count", "publish_date", "upload_date", "trial_date", "trail_member", "lawyer", "law_firm", "court_name", "court_id", "court_province", "court_city", "court_region", "court_district", "effect_level", "pub_prosecution_org", "admin_behavior_type", "admin_manage_scope", "case_name", "case_id, case_type", "appellor", "settle_type", "cause", "trial_round", "doc_type", "fulltext_type", "basics_text", "judge_record_text", "head_text", "tail_text", "judge_result_text", "judge_member_text", "abbr_adjudication_text", "case_skb_text", "judge_reson_text", "additional_text", "correction_text", "private_reason", "legal_base", "Items", "doc_content", "status", "etl", "content", "d", "channel", "crawl_time", "is_private", "keywords"}
columns_name={"id","content"}
df = pd.DataFrame(columns=columns_name)

num=0
for list_a in list_s:
    # print(list_a['id'])
    # print(list_a['judge_record_text'])
    # dic = {'judge_record_text':list_a['judge_record_text'],'fake':1}
    df.loc[num]=list_a
    num=num+1

df.to_excel("5.xlsx",index=None)