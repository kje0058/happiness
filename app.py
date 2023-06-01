import streamlit as st
from app_home import run_app_home
from app_eda import run_app_eda
from app_chart import run_app_chart

def main():
    pass

    st.title('😄Happiness 2021😄')

    menu = ['🏠Home, Sweet Home', '📝EDA', '📊DV']

    st.sidebar.header('행복한 하루되세요🍀')
    choice = st.sidebar.selectbox('📌메뉴', menu)
    st.sidebar.image("https://cafe24img.poxo.com/wigglewiggle20/file_data/wigglewiggle20//2022/07/15/4cde8592a2779a249026379d1c654cd8.jpg", use_column_width=True, caption='Image by Wiggle-Wiggle')
    # with st.sidebar:

    if choice == menu[0] :
        run_app_home()
    elif choice == menu[1] :
        run_app_eda()
    else :
        pass

if __name__ == '__main__':
    main()