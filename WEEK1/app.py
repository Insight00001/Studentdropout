import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
total_table = pd.read_csv('total table.csv')

percentage_table = pd.read_csv('percentage table.csv')
data=pd.read_csv('cleaned_data.csv')

st.set_page_config(
    page_title='Data Visualization Apps',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)
alt.themes.enable('dark')
with st.sidebar:
    st.title("Student Dropout Analysis and Visualization")
    total_colums = total_table.columns
    percentage_columns=percentage_table.columns
    select_total=st.selectbox('Select Total',total_colums[1:])
    select_percentage = st.selectbox("Select Percentage",percentage_columns[1:])


def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

def format_number(num):
    if num>1000000:
        if not num%1000000:
            return f'{num//1000000} M'
        return f'{round(num/1000000,1)} M'
    return f'{num//1000} K'
col=st.columns((2,2,2),gap='medium')

with col[0]:
    st.markdown("Totals")
    total_male = total_table['Total Number of Male']
    #total_male_f=format_number(total_male)
    donut_chart_total_male = make_donut(total_male, 'Total Male', 'green')
    st.altair_chart(donut_chart_total_male)

with col[1]:
    st.text('Total Number of Students')
    st.text('4423')