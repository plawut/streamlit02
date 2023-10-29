import streamlit as st
import pandas as pd
from st_pages import Page, show_pages

st.set_page_config(layout="wide")
show_pages(
     [
          Page("app.py", "HOME", "🏠"),
          Page("pages/map.py", "MAP", "🎇"),
          Page("pages/tab.py", "TAB", "🎈"),
     ]
)

# --- 01
# https://docs.streamlit.io/library/api-reference/write-magic

st.markdown('Helli Streamlit')
st.title('Layout and styling')
st.write('''
San Francisco Dataset !!!!
''')
tree_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

owners = st.sidebar.multiselect('Tree Owner Filter', tree_df['caretaker'].unique())

if owners:
     tree_df = tree_df[tree_df['caretaker'].isin(owners)]


df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']


col1, col2, col3 = st.columns(3)
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

# tab1, tab2, tab3 = st.tabs(['Line Chart', 'Bar Chart', 'Area Chart'])
# with tab1:
#      st.write('Tab 1')
#      st.line_chart(df_dbh_grouped)
# with tab2:
#      st.write('Tab 2')
#      st.bar_chart(df_dbh_grouped)
# with tab3:
#      st.write('tab 3')
#      st.area_chart(df_dbh_grouped)
#
# st.caption('กราฟแสดงจํานวนต้นไม้ทั้งหมดซึ่งจัดกลุ่มตามเส้นผ่านศูนย์กลาง')
# st.title('แปรผล')
# st.write('''
# ส่วนในต้นไม้ใน San Fransisco มีเส้นผ่านศูนย์กลางขนาด 3 ฟุต
# ''')

tree_df = tree_df.dropna(subset=['longitude','latitude'])
tree_df = tree_df.sample(n = 1000, replace = True)
st.map(tree_df)
