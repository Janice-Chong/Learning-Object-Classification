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
    

            


st.header('Exploratory Data Analysis (EDA)')
intro_eda = f"""
<div style="text-align: justify;">
    <p>The data is collected via a {col_17px_text('survey')} using a Google form. It is distributed across students in Universiti Malaya. The collected dataset consists of data from years {col_17px_text('2021 to 2023')}. It consists of {col_17px_text('1035 rows')} and {col_17px_text('47 columns')} comprising of demographics (3), preferred learning mode (1), learning objects preferrences (13) and the VAK learning style questions (30).</p>
</div>


"""
st.markdown(intro_eda, unsafe_allow_html=True)

tableau_embeded = """
<div class='tableauPlaceholder' id='viz1702043538136' style='position: relative'><noscript><a href='#'><img alt='Dataset Distribution Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSPDashboards&#47;DatasetDistributionDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DSPDashboards&#47;DatasetDistributionDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSPDashboards&#47;DatasetDistributionDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1702043538136');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(tableau_embeded, height=550)

tableau_embeded_lo = """
<div class='tableauPlaceholder' id='viz1702043645760' style='position: relative'><noscript><a href='#'><img alt='Most Preferred Learning Objects Based on a Dominant VAK Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LO&#47;LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LO&#47;LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1702043645760');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(tableau_embeded_lo, height=550)


# tableau_embeded_lo = """
# <div class='tableauPlaceholder' id='viz1702007856599' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PreferredLearningObjectsBasedonaDominantVAK&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PreferredLearningObjectsBasedonaDominantVAK&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PreferredLearningObjectsBasedonaDominantVAK&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1702007856599');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
# """
# st.components.v1.html(tableau_embeded_lo, height=1000000)


# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     # Display an image
#     image = 'Pictures/LevelStudy_Gender.png'  # Replace with your file path
#     try:
#         st.image(image, caption='Level of Study & Gender', width=500)
#     except FileNotFoundError:
#         st.error("Image not found. Please check the file path.")

# st.subheader('Level of Study and Gender')
# LevelStudy = f"""
# <div style="text-align: justify;">
#     <p>Figure 1 shows the </p>
# </div>
# """
# st.markdown(LevelStudy, unsafe_allow_html=True)

# from PIL import Image
# LevelStudy_Gender = Image.open("Pictures/LevelStudy_Gender.png")
# st.image(LevelStudy_Gender, caption='Figure 1: Level of Study & Gender', use_column_width="always")

# VAK_Distributions = Image.open("Pictures/VAK_Distributions.png")
# st.image(VAK_Distributions, caption='VAK Distributions', use_column_width="always")

# Preferred_LearningMode = Image.open("Pictures/Preferred_LearningMode.png")
# st.image(Preferred_LearningMode, caption='Preferred Learning Mode Based On a Dominant VAK', use_column_width="always")

# Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
# st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

# Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
# st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

# Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")
# st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")

# # Load the images
# # Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
# # Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
# # Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")

# # Display images in a 3-column layout
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

# with col2:
#     st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

# with col3:
#     st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")
