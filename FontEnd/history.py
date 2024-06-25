import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
from BackEnd.connectSQLite import SQLite
import time
import sqlite3

class History:
    def __init__(self):
        self.check_login = False
        self.db = SQLite("BackEnd/data_sql.sqlite")

    def app(self, log):
        st.subheader('Hệ thống giám sát môi trường', divider='rainbow')
        st.subheader('_Lịch sử_')
        self.check_login = log
        self.db.connectSQL()
        if self.check_login:
            col_value, col_search = st.columns([3, 1])
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
            with col_value:
                tab1, tab2 = st.tabs(["Dữ liệu dạng bảng", "Dữ liệu dạng biểu đồ"])
                with tab1:
                    st.write(df)
                with tab2:
                    st.line_chart (df, x="Thời gian", y=["Nhiệt độ", "Độ ẩm", "PM 1", "PM 2.5", "PM 10", "CO"],
                                color=["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#00FFFF", "#FF00FF"])
            with col_search:
                with st.form("my_form"):
                    st.write('Bộ lọc dữ liệu theo thời gian')

                    col1, col2 = st.columns(2)
                    with col1:
                        date_start = st.date_input("Từ ngày")
                    with col2:
                        time_start = st.time_input("Giờ")
                        datetime_start = datetime.datetime.combine(date_start, time_start)

                    col1, col2 = st.columns(2)
                    with col1:
                        date_end = st.date_input("Đến ngày")
                    with col2:
                        time_end = st.time_input("Giờ.")
                        datetime_end = datetime.datetime.combine(date_end, time_end)

                    submitted = st.form_submit_button("Tìm kiếm")

                    if submitted:
                        st.write(f"Tìm kiếm dữ liệu từ {datetime_start} đến {datetime_end}")
        else:
            st.write("Bạn chưa đăng nhập. Hãy đăng nhập để sử dụng hệ thống.")
        
    def searchData(self, datetime_start, datetime_end):
        conn = sqlite3.connect('BackEnd/data_sql.sqlite')
        query = "SELECT * FROM sensor_data WHERE date BETWEEN ? AND ?"
        df = pd.read_sql_query(query, conn, params=(datetime_start, datetime_end))
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
        return df
