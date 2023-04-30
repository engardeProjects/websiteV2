import streamlit as st

st.set_page_config(page_title="test2",page_icon=":tada:",layout="wide")
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''

hide_st_style = """

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

"""

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader('test')

