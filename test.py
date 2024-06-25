import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('BackEnd/data_sql.sqlite')
query = "SELECT * FROM sensor_data"
df = pd.read_sql_query(query, conn)
conn.close()
df = df.drop(columns=['id'])
df = df.rename(columns={
    'temperature': 'Nhiệt độ',
    'humidity': 'Độ ẩm',
    'pm1': 'PM 1',
    'pm25': 'PM 2.5',
    'pm10': 'PM 10',
    'co_value': 'CO',
    'max_value': 'Max',
    'level': 'Mức độ',
    'date': 'Thời gian'
})
df = df.sort_values(by='Thời gian', ascending=False)
df.insert(0, 'STT', range(1, 1 + len(df)))
st.write(df)

st.line_chart(
   df, x="Thời gian", y=["Nhiệt độ", "Độ ẩm", "PM 1", "PM 2.5", "PM 10", "CO"],
   color=["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#00FFFF", "#FF00FF"]
)

