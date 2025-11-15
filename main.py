import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv('WHO_time_series.csv')

df['Date_reported']=pd.to_datetime(df['Date_reported'])

fig1=px.line(df, x='Date_reported', y='Cumulative_cases', color='Country', title='Números de casos de Covid no Mundo')
fig1.update_layout(xaxis_title='Data',yaxis_title='Número de Casos Acumulados')
fig1.show()

df_brasil_india = df.query('Country == "India" or Country== "Brazil"')
fig2=px.line(df_brasil_india,x='Date_reported', y='Cumulative_cases', color='Country', title='Números de casos de Covid no Brasil')
fig2.update_layout(xaxis_title='Data',yaxis_title='Número de Casos Acumulados no Brasil e na Índia')
fig2.show()

st.set_page_config(page_title="DashCovid",layout="wide")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
