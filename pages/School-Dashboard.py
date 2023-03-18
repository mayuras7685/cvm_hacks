import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go


st.set_page_config(
    page_title="School Dashboard",
    
)

st.title('School Dashboard')

st.write('---')


uploaded_file = st.file_uploader('Upload a file')

df = pd.read_csv(uploaded_file)


df_head = df.head(5)

st.write(df_head)

class_list = ["All", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

select = st.sidebar.selectbox('Filter the Class here:', class_list, key='1')

if select =="All":
  filtered_df = df
else:
  filtered_df = df[df['Class']==select]


#Scatter Chart
fig = px.scatter(df,
x="Level Of Courses (Difficulty)",
y="Mental health assessment of all students",
color="Preventing Discrimination and Persuasion",
hover_name="Class",
size_max=10)
st.write(fig)


st.write("Curriculum Dependent Factors Affecting Happiness Index")

label = []
sizes = []

diff = df[df['Level Of Courses (Difficulty)'] > 2]
students_course_difficult = diff['Level Of Courses (Difficulty)'].count()
eas = df[df['Level Of Courses (Difficulty)'] <= 2]
students_course_easy = eas['Level Of Courses (Difficulty)'].count()
    # students_course_easy += 1
print(students_course_easy)
to_plot = {'Students finding course difficult': students_course_difficult,
               'Students finding Course Easy': students_course_easy}

fig0 = go.Figure(data=go.Scatterpolar(
r=[df['A Clean Environment'].mean(), df['Providing laboratory & workshop facilities'].mean(),
df['The school timetable'].mean(), df['Presenting more sporting & artistic classes'].mean(),
           df['Being able to solve problems of the learner'].mean()],
        theta=['A Clean Environment', 'Providing laboratory & workshop facilities',
               'Effectiveness of school timetable', 'Presenting more sporting & artistic classes',
               'Quality of doubt resolution'],
        fill='toself'
    ))
fig0.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            ),
        ),
        showlegend=False
    )



features = ['Level Of Courses (Difficulty)', 'Course relevance',
               'Critical learning of the learner']

fig1 = go.Figure(data=[
        go.Bar(name='Rated greater than 2', x=features, y=[students_course_difficult,
                                                           len(df[df['Course relevance'] > 2]),
       len(df[df['Involve with fundamental and critical aspects of learner , about manner of living'] > 2])]),
        go.Bar(name='Rated lower than or equal to 2', x=features, y=[students_course_difficult,
                                                           len(df[df['Course relevance'] <= 2]),
       len(df[df['Involve with fundamental and critical aspects of learner , about manner of living'] <= 2])])])
    # Change the bar mode
fig1.update_layout(barmode='group')



graph1 = plotly.offline.plot(fig0, auto_open=False, output_type="div")
fig = go.Figure(data=[go.Pie(labels=label, values=sizes)])
graph2 = plotly.offline.plot(fig1, auto_open=False, output_type="div")
fig3 = go.Figure(data=[go.Pie(labels=["<1","2-3","3-4","4-5"],
                                 values=[len(df[df['Mental health assessment of all students'] <= 1]),
                                         len(df[(df['Mental health assessment of all students'] > 1) &
                                                (df['Mental health assessment of all students'] <= 2)]),
                                         len(df[(df['Mental health assessment of all students'] > 2) &
                                                (df['Mental health assessment of all students'] <= 3)]),
                                         len(df[(df['Mental health assessment of all students'] > 3) &
                                                (df['Mental health assessment of all students'] <= 4)]),
                                         len(df[(df['Mental health assessment of all students'] > 4) &
                                                (df['Mental health assessment of all students'] <= 5)])
                                         ],
                    pull=[0.3, 0, 0, 0])])

graph3 = plotly.offline.plot(fig3, auto_open=False, output_type="div")
fig4 = go.Figure(data=go.Scatter(x=['Discrimination prevention',
                                        'Group Performance',
                                        'Extracurriculars',
                                        'Individual attention',
                                        'Problems solved',
                                        'Age-based conversations'
                                        ], y=[df['Preventing Discrimination and Persuasion'].mean(),
                                              df['Performing group work'].mean(),
                                              df['Presenting more sporting & artistic classes'].mean(),
                                              df['Focus on the individual'].mean(),
                                              df['Are these problems being solved by the School?'].mean(),
                                              df['Issues of concern should be made a point of conversation within age appropriate classrooms and children made aware of existing realities.'].mean()])
                     )
plotly.offline.plot(fig4, auto_open=False, output_type="div")
