from flask import Flask,render_template
from flask import jsonify
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import PreProcessing_DATA as PreP_D
import Rule_Discovry as Rule_Discovry
import numpy as np
import seaborn as sns
from collections import Counter


app = Flask(__name__)
df = pd.read_csv('a.csv')

@app.route('/')
@app.route('/table')
def table():
  data = pd.read_csv('a.csv')

  return data.to_json(orient='records')

@app.route('/PreProData')
def PreProData():
  data = pd.read_csv('a.csv')
  DFAlarms = data.drop(['Date'],axis=1)
  DfAlarm=PreP_D.Preprocecssing.NumTag(DFAlarms)
  DfAlarm=PreP_D.Preprocecssing.AlarmState(DFAlarms)
  DfAlarm.dropna(inplace=True)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.SequenceAlarm(DfAlarm)
  DfAlarm =DfAlarm.reset_index(drop=True)
  DfAlarm=PreP_D.Preprocecssing.AlarmTime(DfAlarm)
  #df.to_json(r'D:\File Name.json', orient='index')

  return DfAlarm.to_json(orient='records')
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
    r1=Rule_Discovry.Rule_Discovry.user_calcule_rols(int(i),df,DfAlarm)
    df=Rule_Discovry.Rule_Discovry.to_dataframe(int(i),r,df,'slid')
    df=Rule_Discovry.Rule_Discovry.to_dataframe(int(i),r1,df,'user')

  return df.sort_values(by=['Tag']).to_json(orient='records')

if __name__ == '__main__':
  app.run(debug=True)

