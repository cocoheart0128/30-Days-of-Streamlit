###########day11
# import streamlit as st

# st.header('st.multiselect')

# options = st.multiselect(
#      'What are your favorite colors',
#      ['Green', 'Yellow', 'Red', 'Blue'],
#      ['Yellow', 'Red'])

# st.write('You selected:', options)


###########day12

# import streamlit as st

# st.header('st.checkbox')

# st.write ('What would you like to order?')

# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')

# if icecream:
#      st.write("Great! Here's some more 🍦")

# if coffee: 
#      st.write("Okay, here's some coffee ☕")

# if cola:
#      st.write("Here you go 🥤")


###########day14

# from pydantic_settings import BaseSettings
# import streamlit as st
# import pandas as pd
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# pr = df.profile_report()
# st_profile_report(pr)


###########day15

import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


