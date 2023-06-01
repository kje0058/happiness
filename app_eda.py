import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_app_eda():
    st.header('이 영역은 헤더 영역')

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

    st.subheader(':loudspeaker:국가 행복지수는 어떤 데이터일까?')
    if st.checkbox('국가 행복지수 데이터 보기'):
        st.dataframe(df)
        st.write('*국가, 세분화된 대륙, 대륙, 행복지수, GDP, 기대수명, 사회적 지지, 선택의 자유, 아량, 부정부패로 이루어져 있어요*')

    st.subheader(':loudspeaker:국가 행복지수 Top 10 나라')
    fig1 = plt.figure()
    df1 = df[(df.loc[:, "Ladder score"]>7.25)]
    sns.barplot(x = "Ladder score", y = "Country name", data=df1)
    plt.title("Happiest Countries in 2021")
    plt.xlabel('행복지수')
    plt.ylabel('국가')
    st.pyplot(fig1)

    st.subheader(':loudspeaker:국가 행복지수 Bottom 10 나라')
    fig2 = plt.figure()
    df2 = df[(df.loc[:, "Ladder score"] < 3.78)]
    sns.barplot(x = "Ladder score", y = "Country name", data=df2)
    plt.title("Happiest Countries in 2021")
    plt.xlabel('행복지수')
    plt.ylabel('국가')
    st.pyplot(fig2)