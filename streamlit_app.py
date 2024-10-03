import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(5, 4),
    columns=('col %d' % i for i in range(4)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write('-----------------------------------------------')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write('-----------------------------------------------')

x = st.slider('xxx')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write('-----------------------------------------------')

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.write('-----------------------------------------------')


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.write('-----------------------------------------------')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

another_option = st.selectbox(
    'Which letter do you like most?',
    ['a','b','c','d','x','y']
)

'You selected: ', another_option