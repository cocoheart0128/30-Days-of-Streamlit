###########day16
# import streamlit as st

# st.title('Customizing the theme of Streamlit apps')

# st.write('Contents of the `.streamlit/config.toml` file of this app')

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """)

# number = st.sidebar.slider('Select a number:', 0, 10, 5)
# st.write('Selected number from slider widget is:', number)


###########day17

# import streamlit as st

# st.title('st.secrets')

# st.write(st.secrets['message'])


###########day18

# import streamlit as st
# import pandas as pd

# st.title('st.file_uploader')

# st.subheader('Input CSV')
# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df.describe())
# else:
#   st.info('☝️ Upload a CSV file')


###########day19

import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


