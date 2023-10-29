import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 01
# https://docs.streamlit.io/library/api-reference/write-magic
st.markdown('Helli Streamlit')
st.title('Layout and styling')
st.write('''
San Francisco Dataset !!!!
''')
tree_df = pd.read_csv('trees.csv')
col1, col2, col3 = st.columns(3)
df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

with col1:
     st.write('column 1')
     st.line_chart(df_dbh_grouped)
with col2:
     st.write('column 2')
     st.bar_chart(df_dbh_grouped)
with col3:
     st.write('column 3')
     st.area_chart(df_dbh_grouped)

st.caption('กราฟแสดงจํานวนต้นไม้ทั้งหมดซึ่งจัดกลุ่มตามเส้นผ่านศูนย์กลาง')
st.title('แปรผล')
st.write('''
ส่วนในต้นไม้ใน San Fransisco มีเส้นผ่านศูนย์กลางขนาด 3 ฟุต
''')


st.divider()