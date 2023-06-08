import streamlit as st

def run_app_home():
    st.balloons()
    st.write('세계 행복 보고서의 2021 국가 행복지수를 통해 각 나라들의 행복지수를 알아보고, 행복은 어떤 지표와 관련이 있는지 알아보는 앱입니다.')
    st.subheader('*국가 행복지수란??*')
    st.write('국가 행복지수는 유엔(UN) 산하 자문기구인 지속가능발전해법네트워크(SDSN)가 10에서 0까지의 삶의 만족도를 나타내는 캔트릴 사다리 척도 설문조사를 통해 산출합니다. SDSN 에서는 세계행복보고서에 국가별 행복지수를 보고하는데 해당 보고서에는 국가 행복지수와 연관이 있는 지표인 1인당 GDP,기대 건강수명,사회적 지원,삶을 선택힐 자유, 관대함, 부패에 대한 인식 등을 함께 산출합니다.')
    st.image('https://img.freepik.com/free-photo/happy-friends-silhouettes-jumping-sunset_285396-8163.jpg?w=1380&t=st=1685599553~exp=1685600153~hmac=435417eea2d52d145a4ce812428ff04698d0cfcf3d8d8ff911158a18653bc145', caption='Image by marymarkevich on Freepik')
