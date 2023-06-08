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

      st.subheader(':loudspeaker:국가 행복지수는 어떤 평가 항목과 관련이 있나요?:thinking_face:')
      ck_1=st.checkbox('히트맵 보기', value=True)   
      if ck_1:
            fig6=plt.figure()
            sns.heatmap(df.corr(numeric_only=True), mask=mask, fmt='.2f', annot=True, vmin=-1, vmax=1, cmap='coolwarm', linewidths=0.5)
            st.pyplot(fig6)

            st.subheader(':loudspeaker:행복지수와 상관관계?:thinking_face:')
            lang_list = ['1인당 GDP','기대 건강수명','사회적 지원','삶을 선택할 자유', '관대함', '부패에 대한 인식']

            choice_list = st.selectbox('평가항목을 선택하세요', lang_list)

      if choice_list=='1인당 GDP':
            fig11 = plt.figure()
            sns.regplot(x='Logged GDP per capita',y='Ladder score',data=df)
            plt.xlabel('1인당 GDP')
            plt.ylabel('국가 행복지수')
            plt.title('국가 행복지수와 1인당 GDP')
            st.pyplot(fig11)

            
      elif choice_list=='기대 건강수명':
            fig12 = plt.figure()
            sns.regplot(x='Healthy life expectancy',y='Ladder score', data=df)
            plt.xlabel('기대 건강수명')
            plt.ylabel('국가 행복지수')
            plt.title('국가 행복지수와 기대 건강수명')
            st.pyplot(fig12)

      elif choice_list=='사회적 지원':
            fig13 = plt.figure()
            sns.regplot(x='Social support',y='Ladder score', data=df)
            plt.xlabel('사회적 지원')
            plt.ylabel('국가 행복지수')   
            plt.title('국가 행복지수와 사회적 지원')    
            st.pyplot(fig13)


      elif choice_list=='삶을 선택할 자유':          
            fig14 = plt.figure()
            sns.regplot(x='Freedom to make life choices',y='Ladder score', data=df)
            plt.xlabel('삶을 선택할 자유')
            plt.ylabel('국가 행복지수')
            plt.title('국가 행복지수와 삶을 선택할 자유')            
            st.pyplot(fig14)


      elif choice_list=='관대함':
            fig15 = plt.figure()
            sns.regplot(x='Generosity',y='Ladder score', data=df)
            plt.xlabel('관대함')
            plt.ylabel('국가 행복지수')
            plt.title('국가 행복지수와 관대함')                  
            st.pyplot(fig15)


      elif choice_list=='부패에 대한 인식':
            fig16 = plt.figure()
            sns.regplot(x='Perceptions of corruption',y='Ladder score', data=df)
            plt.xlabel('부패에 대한 인식')
            plt.ylabel('국가 행복지수')
            plt.title('국가 행복지수와 부패에 대한 인식')        
            st.pyplot(fig16)