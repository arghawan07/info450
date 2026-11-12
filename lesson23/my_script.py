import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv(Path(__file__).parent / "Advertising_F.csv")

st.title("Advertising Effectiveness - Arghawan")
st.sidebar.header("Filters")
x_var = st.sidebar.selectbox("X axis", ["TV", "radio", "newspaper"])


fig = px.scatter(
    df, x=x_var, y="sales",
    labels={"TV": "TV Ad Spend", "radio": "Radio Ad Spend", "newspaper": "Newspaper Ad Spend"},
)
st.plotly_chart(fig)


sales_per_city = df.groupby("City")["sales"].sum().reset_index()
fig2 = px.bar(sales_per_city, x="City", y="sales", title="Total Sales by City")
st.plotly_chart(fig2)


st.dataframe(df)                                 
                                           
                            
