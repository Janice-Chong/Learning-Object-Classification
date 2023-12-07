import streamlit as st

st.title('Learning Style')
st.text('What is VAK Learning Style?, general overview of people\'s styles using Tableau')


# st.markdown("Learning Style is a way of classifying the different <span style='color:blue'>***ways people learn***</span> and <span style='color:blue'>***how they approach information***</span> (Sreenidhi and Tay, 2017)", unsafe_allow_html=True)

# st.markdown("According to research by Sreenidhi and Tay, 2017, the Fleming’s VARK model, provides the learners with a <span style='color:blue'>***profile of their learning styles***</span>. Learners are able to <span style='color:blue'>***understand the type of learning that best suits them***</span>. People learn by:  ", unsafe_allow_html=True)

def italic_16px_text(text):
    color = "black"
    font_size = "16px"
    italic = True
    style = "font-size:{}; color:{}; font-style:italic;" if italic else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"
     
def col_17px_text(text):
    color = "blue"
    font_size = "17px"
    bold = False
    italic = True
    style = "font-size:{}; color:{}; font-weight:bold; font-style:italic;" if bold else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"

ls_text = f"""
<div style="text-align: justify;">
    <p>Learning Style is a way of classifying the different {col_17px_text('ways people learn')} and {col_17px_text('how they approach information')} (Sreenidhi and Tay, 2017). There are many types of learning style and this project focuses on the {italic_16px_text('VAK Learning Style')}.</p>
</div>
"""
st.markdown(ls_text, unsafe_allow_html=True)

st.header('VAK Learning Style')
vak_text = f"""
<div style="text-align: justify;">
    <p>According to research by Sreenidhi and Tay, 2017, the Fleming’s VARK model, provides the learners with a {col_17px_text('profile of their learning styles')}. Learners are able to {col_17px_text('understand the type of learning that best suits them')}. People learn by:</p>
</div>
"""
st.markdown(vak_text, unsafe_allow_html=True)

vak = """
- Seeing  (<u>**V**</u>isual)
- Hearing  (<u>**A**</u>uditory)
- Doing (<u>**K**</u>inesthetic)
"""
st.markdown(vak, unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    # Display an image
    image = 'Pictures/VAK-learning-styles.jpg'  # Replace with your file path
    try:
        st.image(image, caption='Aspect of Learning', width=350)
    except FileNotFoundError:
        st.error("Image not found. Please check the file path.")
    

            


st.header('Exploratory Data Analysis')
st.markdown("", unsafe_allow_html=True)