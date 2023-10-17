###########day21

# import streamlit as st
# import time

# st.title('st.progress')

# with st.expander('About this app'):
#      st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.05)
#      my_bar.progress(percent_complete + 1)

# st.balloons()


###########day22
# import streamlit as st

# st.title('st.form')

# # Full example of using the with notation
# st.header('1. Example of using `with` notation')
# st.subheader('Coffee machine')

# with st.form('my_form'):
#     st.subheader('**Order your coffee**')

#     # Input widgets
#     coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
#     coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
#     brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
#     serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
#     milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
#     owncup_val = st.checkbox('Bring own cup')

#     # Every form must have a submit button
#     submitted = st.form_submit_button('Submit')

# if submitted:
#     st.markdown(f'''
#         ☕ You have ordered:
#         - Coffee bean: `{coffee_bean_val}`
#         - Coffee roast: `{coffee_roast_val}`
#         - Brewing: `{brewing_val}`
#         - Serving type: `{serving_type_val}`
#         - Milk: `{milk_val}`
#         - Bring own cup: `{owncup_val}`
#         ''')
# else:
#     st.write('☝️ Place your order!')


# # Short example of using an object notation
# st.header('2. Example of object notation')

# form = st.form('my_form_2')
# selected_val = form.slider('Select a value')
# form.form_submit_button('Submit')

# st.write('Selected value: ', selected_val)



###########day23

# import streamlit as st

# st.title('st.experimental_get_query_params')

# with st.expander('About this app'):
#   st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# # 1. Instructions
# st.header('1. Instructions')
# st.markdown('''
# In the above URL bar of your internet browser, append the following:
# `?firstname=Jack&surname=Beanstalk`
# after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
# such that it becomes 
# `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
# ''')


# # 2. Contents of st.experimental_get_query_params
# st.header('2. Contents of st.experimental_get_query_params')
# st.write(st.experimental_get_query_params())


# # 3. Retrieving and displaying information from the URL
# st.header('3. Retrieving and displaying information from the URL')

# firstname = st.experimental_get_query_params()['firstname'][0]
# surname = st.experimental_get_query_params()['surname'][0]

# st.write(f'Hello **{firstname} {surname}**, how are you?')



###########day24

# import streamlit as st
# import numpy as np
# import pandas as pd
# from time import time

# st.title('st.cache')

# # Using cache
# a0 = time()
# st.subheader('Using st.cache')

# @st.cache(suppress_st_warning=True)
# def load_data_a():
#   df = pd.DataFrame(
#     np.random.rand(2000000, 5),
#     columns=['a', 'b', 'c', 'd', 'e']
#   )
#   return df

# st.write(load_data_a())
# a1 = time()
# st.info(a1-a0)


# # Not using cache
# b0 = time()
# st.subheader('Not using st.cache')

# def load_data_b():
#   df = pd.DataFrame(
#     np.random.rand(2000000, 5),
#     columns=['a', 'b', 'c', 'd', 'e']
#   )
#   return df

# st.write(load_data_b())
# b1 = time()
# st.info(b1-b0)

###########day25

import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

