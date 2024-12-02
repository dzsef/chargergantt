import streamlit as st

st.title("Vehicle Charging and Travel Schedule")
st.write("Az alábbi Gantt diagram az elektromos járművek töltési és utazási ütemtervét mutatja be:")


html_file_path = "gantt_chart.html"

with open(html_file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

st.components.v1.html(html_content, width=1000, height= 800, scrolling=True)
