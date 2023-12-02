from pathlib import Path
import streamlit as st
from st_pages import Page, add_page_title, show_pages

st.title('Homepage')

st.header('About')
st.markdown("This is a Data Science Project based on the topic of:<br><center>\"<span style='color:blue'><span style='font-size:20px'>***Learning Object Classification Based On Personalisation***</span></span>\"</center>", unsafe_allow_html=True)

# st.markdown("<span style='font-size:17px'>***Each individual possesses a unique approach to learning***</span></span>, also known as the <span style='color:blue'><span style='font-size:17px'>***learning style***</span></span>, and a distinct preference for specific learning objects. There exist various types of learning objects which we can choose to use as our medium to learn. With the variety of options, there appears to be a problem or <span style='font-size:17px'>***contemplation in choosing the right***</span></span> <span style='color:blue'><span style='font-size:17px'>***learning object***</span></span>.", unsafe_allow_html=True)

# st.markdown("Research by Martin & Maria, 2019, noted that <span style='color:blue'><span style='font-size:17px'>***personalisation***</span></span> is the key to improving learning performance. Furthermore, Imran et al. (2015) stated that <span style='font-size:17px'>***tailoring learning objects***</span></span> to align with students' individual learning styles and preferences can <span style='font-size:17px'>***enhance educational experience***</span></span> and <span style='font-size:17px'>***increases learners' performance and satisfaction***</span></span>.", unsafe_allow_html=True)

#-----
# text = """
# <div style="text-align: justify; font-size: 17px;">
#     <p><strong>Each individual possesses a unique approach to learning</strong>, also known as the <span style="color:blue"><strong>learning style</strong></span>, and a distinct preference for specific learning objects. There exist various types of learning objects which we can choose to use as our medium to learn. With the variety of options, there appears to be a problem or <strong>contemplation in choosing the right</strong> <span style="color:blue"><strong>learning object</strong></span>.</p>
#     <p>Research by Martin & Maria, 2019, noted that <span style="color:blue"><strong>personalisation</strong></span> is the key to improving learning performance. Furthermore, Imran et al. (2015) stated that <strong>tailoring learning objects</strong> to align with students' individual learning styles and preferences can <strong>enhance educational experience</strong> and <strong>increase learners' performance and satisfaction</strong>.</p>
# </div>
# """
# st.markdown(text, unsafe_allow_html=True)
#-----
# def apply_style(text, color=None, font_size=None, bold=False):
#     style = "font-size:{}; color:{}; font-weight:bold;" if bold else "font-size:{}; color:{};"
#     color = color if color else "black"
#     font_size = font_size if font_size else "inherit"
#     return f"<span style='{style.format(font_size, color)}'>{text}</span>"


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

about_text = f"""
<div style="text-align: justify;">
    <p>{italic_16px_text('Each individual possesses a unique approach to learning')}, also known as the {col_17px_text('learning style')}, and everyone has a distinct preference for specific learning objects. There exist various types of learning objects which we can choose to use as our medium to learn. With the variety of options, there appears to be a problem or {italic_16px_text('contemplation in choosing the right')} {col_17px_text('learning object')}.</p>
    <p>Research by Martin & Maria (2019), noted that {col_17px_text('personalisation')} is the key to improving learning performance. Furthermore, Imran et al. (2015) stated that {italic_16px_text('tailoring learning objects')} to align with students' individual learning styles and preferences can {italic_16px_text('enhance educational experience')} and {italic_16px_text('increase learners performance and satisfaction')}.</p>
</div>
"""
st.markdown(about_text, unsafe_allow_html=True)


st.header('Objectives')
objectives = """
- To <span style='color:blue'><span style='font-size:17px'>develop</span></span> a learning object classification based on personalisation model
- To <span style='color:blue'><span style='font-size:17px'>evaluate</span></span> a learning object classification based on personalisation model
"""
st.markdown(objectives, unsafe_allow_html=True)

st.header('Methodology')
methodology_text = f"""
<div style="text-align: justify;">
    <p>A {col_17px_text('SVM Model')} is trained, taking the learning objects preferences of over 1500 respondents into considerations.</p>
    <p>continue...  </p>
</div>
"""
st.markdown(methodology_text, unsafe_allow_html=True)





st.markdown("", unsafe_allow_html=True)


# one of the most prevalent and widely
# embraced categorisations of diverse learning styles is
# Fleming’s VARK model, sometimes abbreviated as VAK,
# representing Visual (V), Auditory (A), and Kinaesthetic
# (K) sensory modalities. This model provides learners
# with a comprehensive insight into their learning styles,
# drawing from the sensory modalities that engage in their
# information absorption process. The paper also added
# individuals often possess a favoured learning style, which
# could encompass a mix of all three sensory modes. This
# preference can vary from a strong inclination towards
# a specific style to a balanced combination of two or
# all three. Understanding one’s preferred learning style
# empowers them to identify the most effective learning
# approaches, enabling informed choices in their learning
# strategies.
# 1) Visual (V): Individuals who have a preference for
# the visual aspect of learning excel when presented
# 2
# with pictorial information and descriptions, in-
# cluding drawings, graphics, and images. For these
# learners, the most suitable activities encompass
# lectures, slide presentations, diagrams, graphics,
# videos, and image-rich materials. Engaging in ex-
# ercises, surveys, or any visual information content
# is particularly effective for their learning style
# (Dantas and Cunha, 2020).
# 2) Auditory (A): Individuals who excel in absorbing
# information through their sense of hearing. They
# are more inclined to prefer recording lectures for
# later review, rather than relying on visual aids
# like PowerPoint presentations. Additionally, these
# learners may read their notes aloud as part of their
# study approach (Shahbodin et al., 2015).
# 3) Kinaesthic (K): Individuals who learn best by
# doing (Surjono, 2011). These learners enjoy the
# hands-on experience or engage in complete phys-
# ical immersion within the learning environment,
# which may involve activities such as field trips,
# dramatization, pantomime, or interviews (Maulidia
# Tifani Alfin Nur Hardiana, 2018). Additionally,
# individuals with this learning style encompass var-
# ious forms of movement and emotions, both in
# terms of experiencing and recollecting them. It in-
# cludes aspects like physical motion, coordination,
# rhythm, emotional reactions, and physical comfort
# (Rita Syofyan, 2018).

show_pages([
    Page('main.py', 'Home'),
    Page('pages/vak.py', 'VAK Learning Style'),
    Page('pages/LearningObjects.py', 'Learning Objects'),
    Page('pages/Questionaire.py', 'Which Learning Objects Suits Me Best?'),
    Page('pages/UserManual.py', 'User Manual'),
])

