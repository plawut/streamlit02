import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.markdown('Hello Streamlit')
st.title('Map of San Fransisco Trees')
st.write('''
San Francisco Dataset !!!!
''')
tree_df = pd.read_csv('trees.csv')
tree_df = tree_df.dropna(subset=['longitude','latitude'])
tree_df = tree_df.sample(n = 1000, replace = True)
st.map(tree_df)