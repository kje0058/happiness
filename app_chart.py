import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



def run_app_chart():
    df=pd.read_csv('data/world-happiness-report-2021.csv')
    df.drop(['Standard error of ladder score','upperwhisker', 'lowerwhisker',
       'Ladder score in Dystopia',
       'Explained by: Log GDP per capita', 'Explained by: Social support',
       'Explained by: Healthy life expectancy',
       'Explained by: Freedom to make life choices',
       'Explained by: Generosity', 'Explained by: Perceptions of corruption',
       'Dystopia + residual'], axis=1, inplace=True)
    df['Continent']=df['Regional indicator'].replace({'Sub-Saharan Africa':'Africa',
                                                      'Western Europe':'Europe','Latin America and Caribbean':'America',
                                                      'Middle East and North Africa':'Africa','Central and Eastern Europe':'Europe',
                                                      'Commonwealth of Independent States':'CIS','Southeast Asia':'Asia','East Asia':'Asia',
                                                      'North America and ANZ':'America','South Asia':'Asia'})
    df=df.reindex(['Country name','Regional indicator', 'Continent', 'Ladder score',
                    'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
                    'Freedom to make life choices', 'Generosity','Perceptions of corruption'],axis = 1)
    
    st.subheader(':loudspeaker:대륙별 행복지수')
    