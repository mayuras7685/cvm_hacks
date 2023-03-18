import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Daily Mood Tracking",
    
)

st.title('Daily Mood Tracking')

st.write('---')





# Create a default list of habits
#default_habits = ['Exercise', 'Meditation', 'Reading', 'Writing']
# Add a brief description
st.markdown("This application allows you to track your progress on various Mood over time. Use the sidebar to select Moods, specify progress, and save your data. You can also import and export progress data as a CSV file.")

if 'count' not in st.session_state:
	st.session_state.count = ['Very Happy', 'Happy', 'Nuteral', 'Sad', 'Very Sad']

# Create a Pandas DataFrame to store the user's progress data
df = pd.DataFrame(columns=['Date', 'Mood', 'Progress'])

# Create a sidebar for selecting habits and specifying progress
st.sidebar.title('Mood Tracker')

# Add a button for loading the progress data from a CSV file
if st.sidebar.button('Load progress'):
    if os.path.exists('progress.csv'):
        df = pd.read_csv('progress.csv')
        df = df.drop_duplicates(subset = ['Date', 'Mood'], keep='last')
        df = df.sort_values(by='Date')
        df.to_csv('progress.csv', index=False)
        st.success("Progress data imported successfully!")
    else:
        st.error("Error: Could not find progress.csv file.")



# Add a button for adding a new habit to the list
new_habit = st.sidebar.text_input('Add a new Mood:')
#@st.cache
if st.sidebar.button('Add Mood'):

    # Create a unique identifier for the habit
    new_habit_id = new_habit.replace(" ", "_").lower()
    st.session_state.count.append(new_habit)
    #st.text(selected_habits)

# Add a multi-select widget for choosing habits
selected_habits = st.sidebar.multiselect('Default Moods:', st.session_state.count)

# Add a date picker for selecting a specific date
selected_date = st.sidebar.date_input('Select date:')




# Add the new data to the DataFrame and save it to a CSV file
# Add a slider for specifying progress for each habit
for Mood in selected_habits:
    #st.text(selected_habits)
    # Create a unique identifier for the habit
    habit_id = Mood.replace(" ", "_").lower()
    progress = st.sidebar.slider(f'{Mood} progress:', min_value=0, max_value=100, value=50, step=1, key = habit_id)
    #df = df.append({'Date': selected_date, 'Habit': habit, 'Progress': progress}, ignore_index=True)
    df = pd.concat([df, pd.DataFrame({'Date': selected_date, 'Mood': Mood, 'Progress': progress}, index=[0])], ignore_index=True)
    #st.text(habit)

#
# Add a button for removing a habit from the list
removed_habit = st.sidebar.selectbox('Remove a Mood:', st.session_state.count)
if st.sidebar.button('Remove Mood'):
    st.session_state.count.remove(removed_habit)
    selected_habits.remove(removed_habit)

# Add a button for saving the progress data to a CSV file
st.info("In the case that a data for any date has already been entered, your last data will be saved.")
if st.sidebar.button('Save progress'):
    if os.path.exists('progress.csv'):
        csv_df = pd.read_csv('progress.csv')
        df = pd.concat([csv_df, df], ignore_index=True)
        df = df.drop_duplicates(subset = ['Date', 'Habit'], keep='last')
        df = df.sort_values(by='Date')
        df.to_csv('progress.csv', index=False)
        st.success("Progress data saved successfully!")
    else:
        df.to_csv('progress.csv', index=False)
        st.success("Progress data saved successfully!")
# Use Plotly to create visualizations of the user's progress for each habit
for Mood in st.session_state.count:
    df_habit = df[df['Mood'] == Mood]
    fig = px.line(df_habit, x='Date', y='Progress', title=Mood)
    st.plotly_chart(fig)

# Create a table to display all of the progress data and analysis results
# Remove duplicates and pivot the data
df = df.drop_duplicates(subset = ['Date', 'Mood'], keep='last')
st.table(df.pivot(index='Date', columns='Mood', values='Progress'))
