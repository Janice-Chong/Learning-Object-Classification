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

# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     # Display an image
#     image = 'Pictures/VAK-learning-styles.jpg'  # Replace with your file path
#     try:
#         st.image(image, caption='Aspect of Learning', width=350)
#     except FileNotFoundError:
#         st.error("Image not found. Please check the file path.")
    

            


st.header('Exploratory Data Analysis')
st.markdown("", unsafe_allow_html=True)

# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     # Display an image
#     image = 'Pictures/LevelStudy_Gender.png'  # Replace with your file path
#     try:
#         st.image(image, caption='Level of Study & Gender', width=500)
#     except FileNotFoundError:
#         st.error("Image not found. Please check the file path.")

from PIL import Image
LevelStudy_Gender = Image.open("Pictures/LevelStudy_Gender.png")
st.image(LevelStudy_Gender, caption='Level of Study & Gender', use_column_width="always")

VAK_Distributions = Image.open("Pictures/VAK_Distributions.png")
st.image(VAK_Distributions, caption='VAK Distributions', use_column_width="always")

Preferred_LearningMode = Image.open("Pictures/Preferred_LearningMode.png")
st.image(Preferred_LearningMode, caption='Preferred Learning Mode Based On a Dominant VAK', use_column_width="always")

Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")
st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")

# Load the images
# Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
# Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
# Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")

# Display images in a 3-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

with col2:
    st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

with col3:
    st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")
