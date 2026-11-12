%%writefile my_script.py
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('/content/Advertising_F.csv')
st.title("Adversiting Effictiveness Arghawan ")
st.sidebar.head("Fikters")
x_var = st.sidebar.selectbox("X axis", ["TV", "radio", "newspaper"])

#show scatterplot
fig=px.scatter(df, x=x_ar', y='sales',
           labels={'TV': 'TV Ad Spend', 'radio': 'Radio add Spend'})

 st.plptly_chart(fig)
 #show bar plot

sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city,x='City',y='sales',title="data is fun")
st.plotly_chart(fig)

#show the dataframe
st.dataframe(df)                                   
                                           
                            
