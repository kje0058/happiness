import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_app_ml():
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
   df_corr = df.corr(numeric_only=True)
   mask = np.array(df_corr)
   mask[np.tril_indices_from(mask)] = False

   st.subheader(':loudspeaker:행복지수는 어떤 지표와 관련이 있나요?:thinking_face:')
   bu_1=st.button('히트맵 보기')   
   if bu_1:
      fig6=plt.figure()
      sns.heatmap(df.corr(numeric_only=True), mask=mask, fmt='.2f', annot=True, vmin=-1, vmax=1, cmap='coolwarm', linewidths=0.5)
      st.pyplot(fig6)
