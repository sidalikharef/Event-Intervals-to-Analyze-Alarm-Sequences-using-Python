import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pyplot
import Teloiral_Win as Algorithm

class Rule_Discovry:
    def DictSequences(DfAlarm):
        r=[]
        for i in DfAlarm:
            res = list(filter(lambda x : x > 0, i))
            r.append(res)
        return r

    def fill_tag(df,DfAlarm):
        m=[]
        rec=Algorithm.Algorithm.GetAlarms(DfAlarm)
        flag=True
        for i in rec:
            for j in DfAlarm['Time']:
                if (i==DfAlarm.at[j-1,'Alarm'].astype(int))  and flag==True:
                    m.append(DfAlarm.at[j-1,"Fault"])
                    flag=False
            flag=True
        df['ALARM']=m
        df['Tag']=rec
        return df

    def calcule_rols(x,df,DfAlarm):
        r=[]
        rec=Algorithm.Algorithm.GetAlarms(DfAlarm)
        m=Algorithm.Algorithm.calcul(DfAlarm,rec,x)
        m=Rule_Discovry.DictSequences(m)
        freq=DfAlarm['Alarm'].values.tolist()
        for i in m :
            conf= (m.count(i)/freq.count(x))*100
            conf=round(conf, 2)
            strr='',x,' => ',i,'  ',conf,')'
            r.append(strr);
        return r

    def user_calcule_rols(x,df,DfAlarm):
        r=[]
        rec=Algorithm.Algorithm.GetAlarms(DfAlarm)
        m=Algorithm.Algorithm.user_calcul(DfAlarm,rec,x,4)
        m=Rule_Discovry.DictSequences(m)
        freq=DfAlarm['Alarm'].values.tolist()
        for i in m :
            conf= (m.count(i)/freq.count(x))*100
            conf=round(conf, 2)
            strr='',x,' => ',i,'  ',conf,')'
            r.append(strr);
        return r

    def to_dataframe(x,r,df,pos):
        x1=df.index[df['Tag'] == x].tolist()
        retruned=[]
        for i in r:
            m=''
            p=0
            for j in i:
                if p<6:
                    m=m+str(j)
                if p==6:
                    m=m+"      "
                    retruned.append(m)
                    p=0;
                p+=1

        my_final_list = set(retruned)
        for i in my_final_list:
            if float(i[-11:-3]) < 100:
                m=0;
                if(m<float(i[-11:-3])):
                    m=float(i[-11:-3])
                    for s in my_final_list:
                        if(float(s[-11:-3])==m):
                            first_slid=s
                for r in x1:
                    if(pos=='slid'):
                        df.at[r,'Simple_Sliding']= first_slid
                        s=''
                    else:
                        df.at[r,'User_Sliding']= first_slid
                        s=''

        return df
