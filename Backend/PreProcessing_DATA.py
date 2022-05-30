import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pyplot

class Preprocecssing:

    def NumTag(Dframe):
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        X = le.fit_transform(Dframe['Tag'])
        Dframe['NumTag']=X
        return Dframe

    def checkNumTag(Dframe):
        DfALL=Dframe.index[Dframe["Tag"].astype("str").str.contains("1")].tolist()
        for i in DfALL:
            if Dframe.at[i,'NumTag'].astype(int) == 0:
                Dframe.at[i,'NumTag']=Dframe.at[i,'NumTag'].astype(int)+99
        return Dframe
    def tagFault(Dframe):
        x=Dframe['Alarm']
        Dframe['Fault']=x
        return Dframe
    def AlarmState(Dframe):
        x=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" NR")].tolist()
        r0=Dframe.index[Dframe["Alarm"].astype("str").str.contains("ONUSER")].tolist()
        r1=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" AUT")].tolist()
        y7=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" DegC ")].tolist()
        r3=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" Recover")].tolist()
        r4=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" IMAN")].tolist()
        r5=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" CAS")].tolist()
        r6=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" TRK")].tolist()
        r7=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" MAN")].tolist()
        y0=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" HH")].tolist()
        y1=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" HI")].tolist()
        y2=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" LL")].tolist()
        y3=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" LO")].tolist()
        y4=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" ALM")].tolist()
        y5=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" NR")].tolist()
        y6=Dframe.index[Dframe["Alarm"].astype("str").str.contains(" MHI")].tolist()

        r=r0+r1+r3+r4+r5+r6+r7
        y=y0+y1+y2+y3+y4+y5+y6+y7

        for i in x:
            Dframe.at[i,'Alarm']=  Dframe.at[i,'NumTag'].astype(int)*-1
        for j in y:
            Dframe.at[j,'Alarm']=  Dframe.at[j,'NumTag'].astype(int)*1
        for i in x:
            Dframe.at[i,'Alarm']=  Dframe.at[i,'NumTag'].astype(int)*-1

        for z in r:
            Dframe.at[z,'Alarm']= np.nan

        del Dframe["NumTag"]
        return Dframe;


    def SequenceAlarm(DfAlarm):

        DfAlarm =DfAlarm.reset_index(drop=True)
        DfALL=DfAlarm.index[DfAlarm["Tag"].astype("str").str.contains("1")].tolist()
        for i in DfALL:
            if(i==0):
                x=1
            else:
                if DfAlarm.at[i,'Alarm'].astype(int) == DfAlarm.at[i-1,'Alarm'].astype(int) :
                    DfAlarm=DfAlarm.drop(i-1)
        DfAlarm =DfAlarm.reset_index(drop=True)
        return DfAlarm

    def AlarmTime(Dframe):
        Dframe.insert(2, 'Time', range(1, 1 + len(Dframe)))
        return Dframe
