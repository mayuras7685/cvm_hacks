import streamlit as st
import numpy as np
from predict_happiness import predict

st.title('Weekly Questionnaire')

st.write('---')



# Level Of Courses (Difficulty)
A = st.radio('(1) Level Of Courses', (0,1,2,3,4) ,horizontal=True)

# Making a clean environment
B = st.radio('(2) A Clean Environment', (0, 1, 2, 3, 4) ,horizontal=True)

# Employing teachers with competency
C = st.radio('(3) Employing teachers with competency', (0, 1, 2, 3, 4) ,horizontal=True)

# Prevention from any Discrimination and Persuasion
D = st.radio('(4) Prevention from any Discrimination and Persuasion', (0, 1, 2, 3, 4) ,horizontal=True)

# Providing laboratory & workshop facilities and evaluation of time 
E = st.radio('(5) Providing laboratory & workshop facilities and evaluation of time ', (0, 1, 2, 3, 4) ,horizontal=True)

# The school timetable
F = st.radio('(6) The school timetable', (0, 1, 2, 3, 4) ,horizontal=True)

# Performing group work
G = st.radio('(7) Performing group work', (0, 1, 2, 3, 4) ,horizontal=True)

# Mental health assessment of all students
H = st.radio('(8) Mental health assessment of all students', (0, 1, 2, 3, 4) ,horizontal=True)

# Presenting more sporting & artistic classes
I = st.radio('(9) Presenting more sporting & artistic classes', (0, 1, 2, 3, 4) ,horizontal=True)

# Being able to solve problems of the learner
J = st.radio('(10) Being able to solve problems of the learner', (0, 1, 2, 3, 4) ,horizontal=True)

# Courses should have creative and colorful instructional materials and fun activities.
K = st.radio('(11) Courses should have creative and colorful instructional materials and fun activities.', (0, 1, 2, 3, 4) ,horizontal=True)

# Focus on the individual
L = st.radio('(12) Focus on the individual', (0, 1, 2, 3, 4) ,horizontal=True)

# Involve with fundamental and critical aspects of learner
M = st.radio('(13) Involve with fundamental and critical aspects of learner , about manner of living', (0, 1, 2, 3, 4) ,horizontal=True)

# Course relevance
N = st.radio("(14) Course relevance", (0, 1, 2, 3, 4) ,horizontal=True, label_visibility="visible")

# Issues of concern
O = st.radio('(15) Issues of concern should be made a point of conversation within age appropriate classrooms and children apprised of existing realities.', (0, 1, 2, 3, 4) ,horizontal=True)

# Are these problems being solved by the School?
P = st.radio('(16) Are these problems being solved by the School?', (0, 1, 2, 3, 4) ,horizontal=True)

if st.button('Predict Happiness index'):
    cost = predict(np.array([[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]]))
    st.text(cost[0])