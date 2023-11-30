from pathlib import Path
import streamlit as st
from st_pages import Page, add_page_title, show_pages

st.title('Homepage')
st.write('What is VAK Learning Style?, general overview of people\'s styles using Tableau')

show_pages([
    Page('main.py', 'Home'),
    Page('pages/Questionaire.py', 'Questionaire'),
    Page('pages/UserManual.py', 'User Manual'),
])

