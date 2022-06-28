from flask import Flask,request
from flask import jsonify
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import PreProcessing_DATA as PreP_D
import Relation_Discovry as Rule_Discovry
import numpy as np

import seaborn as sns
from json import loads
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET







app = Flask(__name__)

temp,datas=3,'a.csv'


@app.route("/add", methods=["POST"], strict_slashes=False)
def articles():
  global temp
  global datas
  temp =  request.json['temp']
  datas = request.json['data']
  print(int(temp))
  return temp,datas

@app.route('/PreProData')
def PreProData():
  print(datas)
  data = pd.read_csv(datas)
  DFAlarms = data.drop(['Heure'],axis=1)
  DfAlarm=PreP_D.Preprocecssing.NumTag(DFAlarms)
  DfAlarm=PreP_D.Preprocecssing.checkNumTag(DFAlarms)
  DfAlarm=PreP_D.Preprocecssing.AlarmState(DFAlarms)
  DfAlarm.dropna(inplace=True)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.SequenceAlarm(DfAlarm)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.AlarmTime(DfAlarm)
  #df.to_json(r'D:\File Name.json', orient='index')
  json_obj =DfAlarm.to_json(orient='records')
  xml = dicttoxml(loads(json_obj))
  with open("XmlFiles/Preprocessing_DATA.xml", "wb") as f:
    f.write(xml)
  return json_obj

@app.route('/Dashboard')
def Dashboard():
  data = pd.read_csv('a.csv')
  DFAlarms = data.drop(['Date'],axis=1)
  DfAlarm=PreP_D.Preprocecssing.tagFault(DFAlarms)
  DfAlarm=PreP_D.Preprocecssing.NumTag(DFAlarms)
  DfAlarm=PreP_D.Preprocecssing.AlarmState(DFAlarms)
  DfAlarm.dropna(inplace=True)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.SequenceAlarm(DfAlarm)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.AlarmTime(DfAlarm)
  print(DfAlarm)
  df = pd.DataFrame({'ALARM':[],'Tag': [],'Simple_Sliding': [],'User_Sliding': [],'Proposed': []})
  df=Rule_Discovry.Rule_Discovry.fill_tag(df,DfAlarm)
  for i in df['Tag']:
    r=Rule_Discovry.Rule_Discovry.calcule_rols(int(i),df,DfAlarm)
    r1=Rule_Discovry.Rule_Discovry.user_calcule_rols(int(i),df,DfAlarm,int(temp))
    df=Rule_Discovry.Rule_Discovry.to_dataframe(int(i),r,df,'slid')
    df=Rule_Discovry.Rule_Discovry.to_dataframe(int(i),r1,df,'user')
  df.dropna(inplace=True)
  for i in df['Tag']:
    df=Rule_Discovry.Rule_Discovry.proposed(int(i),df)
  json_obj =df.to_json(orient='records')
  xml = dicttoxml(loads(json_obj))
  with open("XmlFiles/Dashboard.xml", "wb") as f:
    f.write(xml)
  return json_obj


if __name__ == '__main__':
  app.run(debug=True)

