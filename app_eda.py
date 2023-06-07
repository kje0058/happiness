import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
from matplotlib import font_manager, rc
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_app_eda():

    tab1, tab2 = st.tabs(["국가 행복지수", "대륙별"])

    with tab1:
        df1=pd.read_csv('data/world-happiness-report-2021.csv')
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

        st.subheader(':loudspeaker:국가 행복지수는 어떤 데이터일까?:thinking_face:')
        ck_1=st.checkbox('데이터 원본 보기')
        if ck_1 :
            st.write('데이터 출처 : kaggle(https://www.kaggle.com/datasets/unsdsn/world-happiness)')
            st.dataframe(df1)
        ck_2 = st.checkbox('국가 행복지수 데이터 보기',value=True)
        if ck_2 :

            st.dataframe(df)
            st.write('*국가, 세분화된 대륙, 대륙, 행복지수, 1인당 GDP, 사회적 지원, 기대 건강수명, 삶을 선택할 자유, 관대함, 부패에 대한 인식으로 이루어져 있어요*')
            with st.expander('6가지 행복 평가 항목'):
                st.text('① 1인당 GDP(GDP per Capita) :  세계은행의 구매력 평가 기준\n② 사회적 지원(Social Support) : 문제가 생겼을 때 도움을 줄 수 있는 사람 여부\n③ 기대 건강수명 (Healthy Life Expectancy) : 세계보건기구의 기대수명 기준\n④ 인생을 선택할 자유(Freedom to make life choices) : 삶에서 무엇을 할 것인지 선택할 자유에 만족하는지 여부\n⑤ 관대함 (Generosity) : 지난 한 달 동안 기부 여부\n⑥ 부패에 대한 인식(Perceptions of Corruption) : 부패가 만연하다고 생각하는지 여부')

        st.subheader(':loudspeaker:국가 행복지수 Map:world_map:')
        fig4 = px.choropleth(df.sort_values("Ladder score"), 
                        locations = "Country name", 
                        color = "Ladder score", color_continuous_scale = 'GnBu',
                        locationmode = "country names")
        fig4.update_layout(title = "국가 행복지수")
        st.plotly_chart(fig4)
        with st.expander('Ladder score란?'):
            st.image('https://www.researchgate.net/publication/41403889/figure/fig2/AS:203177002573832@1425452580488/Quality-of-life-ladder-Notes-Derived-from-Cantrils-self-anchoring-ladder-50-An.png', caption='서울대학교 행복연구센터(https://www.happyfinder.co.kr/2023/04/02/%ed%96%89%eb%b3%b5%ec%9d%98-%ec%b8%a1%ec%a0%95/)')
            st.text('사다리의 가장 밑인 0은 “자신이 스스로 평가할 때 내 삶은 최악의 상태이다.”입니다. \n가장 위의 10은 “자신이 스스로 평가할 때 내 삶의 최상의 상태이다.”입니다. \n이 척도에서 자신의 인생을 한번 평가하는 방법으로 삶의 만족도를 측정합니다.')

        st.subheader(':loudspeaker:국가 행복지수 Top 10 나라:blush:')
        if st.button('클릭:point_left:') :
            fig1 = plt.figure()
            df1 = df[(df.loc[:, "Ladder score"]>7.25)]
            sns.barplot(x = "Ladder score", y = "Country name", data=df1, palette='Spectral')
            plt.title("국가 행복지수 Top 10 in 2021")
            plt.xlabel('행복지수')
            plt.ylabel('국가명')
            st.pyplot(fig1)

        st.subheader(':loudspeaker:국가 행복지수 Bottom 10 나라:sob:')
        if st.button(':point_right:클릭') :   
            fig2 = plt.figure()
            df2 = df[(df.loc[:, "Ladder score"] < 3.78)]
            sns.barplot(x = "Ladder score", y = "Country name", data=df2, palette='Spectral')
            plt.title("국가 행복지수 Bottom 10 in 2021")
            plt.xlabel('행복지수')
            plt.ylabel('국가명')
            st.pyplot(fig2)

    with tab2:
        st.subheader(':loudspeaker:대륙별 국가 행복지수 차트:chart_with_upwards_trend:')
        df5=df.groupby("Continent")['Ladder score'].mean().sort_values(ascending=False)
        df5=df5.to_frame()
        df5 = df5.reset_index()

        fig3 = plt.figure()
        sns.kdeplot(df, x="Ladder score", hue = "Continent", fill = True, linewidth = 2)
        plt.axvline(df["Ladder score"].mean(), c = "red")
        plt.title("대륙별 행복지수")
        st.pyplot(fig3)

        st.subheader(':loudspeaker:대륙별 행복지수의 지표:bar_chart:')
        lang_list = ['1인당 GDP','기대 건강수명','사회적 지원','삶을 선택할 자유', '관대함', '부패에 대한 인식']

        choice_list = st.selectbox('칼럼을 선택하세요', lang_list)

        if choice_list=='1인당 GDP':
            st.write('*1인당 GDP*')
            fig5 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Logged GDP per capita',palette='Spectral')
            st.pyplot(fig5)
            
        elif choice_list=='기대 건강수명':
            st.write('*기대 건강수명*')
            fig6 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Healthy life expectancy',palette='Spectral')
            st.pyplot(fig6)

        elif choice_list=='사회적 지원':
            st.write('*사회적 지원*')
            fig7 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Social support',palette='Spectral')            
            st.pyplot(fig7)

        elif choice_list=='삶을 선택할 자유':
            st.write('*삶을 선택할 자유*')            
            fig8 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Freedom to make life choices',palette='Spectral')            
            st.pyplot(fig8)

        elif choice_list=='관대함':
            st.write('*관대함*')
            fig9 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Generosity',palette='Spectral')            
            st.pyplot(fig9)

        elif choice_list=='부패에 대한 인식':
            st.write('*부패에 대한 인식*')
            fig10 = plt.figure()
            sns.barplot(data=df, x='Continent', y='Perceptions of corruption', palette='Spectral')      
            st.pyplot(fig10)