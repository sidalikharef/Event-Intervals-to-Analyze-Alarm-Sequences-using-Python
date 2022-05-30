import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pyplot
class Algorithm:
    def GetAlarms(DfAlarm):
        Rec= DfAlarm['Alarm']
        Rec=list(dict.fromkeys(DfAlarm['Alarm']))
        Rec=list(filter(lambda x: x > 0, Rec))
        return Rec
    def GetAlarmss(DfAlarm):
        Rec=list(dict.fromkeys(DfAlarm['Alarm']))
        Rec=list(filter(lambda x: x < 0, Rec))
        return Rec

    def calcul(DfAlarm,rec,x):
        DfALL=DfAlarm.index[DfAlarm["Tag"].astype("str").str.contains("1")].tolist()
        m=[]
        l=[]
        Flag=False
        for i in DfALL:
            if DfAlarm.at[i,'Alarm'].astype(int) == x:
                Flag=True
            else:
                if DfAlarm.at[i,'Alarm'].astype('int')== -x:
                    Flag=False
            if DfAlarm.at[i,'Alarm'].astype('int') != x and DfAlarm.at[i,'Alarm'].astype('int') != -x and Flag==True:
                l.append((DfAlarm.at[i,'Alarm'].astype('int')))

            else:
                    if l :
                        m.append(l)
                        l=[]
                        Flag=False



        return m

    def user_calcul(DfAlarm,rec,x,t):
        DfALL=DfAlarm.index[DfAlarm["Tag"].astype("str").str.contains("1")].tolist()
        m=[]
        l=[]
        t1=0
        Flag=False
        for i in DfALL:
            if DfAlarm.at[i,'Alarm'].astype(int) == x:
                Flag=True
            else:
                if DfAlarm.at[i,'Alarm'].astype('int')== -x or t1>=t:
                    Flag=False
                    t1=0
            if DfAlarm.at[i,'Alarm'].astype('int') != x and DfAlarm.at[i,'Alarm'].astype('int') != -x and Flag==True:
                t1=t1+1
                l.append((DfAlarm.at[i,'Alarm'].astype('int')))

            else:
                    if l :
                        m.append(l)
                        l=[]
                        Flag=False



        return m
