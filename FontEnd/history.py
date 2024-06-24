import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt

class History:
    def __init__(self):
        self.check_login = False

    def app(self, log):
        st.subheader('Hệ thống giám sát môi trường', divider='rainbow')
        st.subheader('_Lịch sử_')
        self.check_login = log
        if self.check_login:
            col_value, col_search = st.columns([3, 1])
            
            with col_value:
                tab1, tab2 = st.tabs(["Dữ liệu dạng bảng", "Dữ liệu dạng biểu đồ"])
                with tab1:
                    df = pd.DataFrame({
                        'Thời gian': pd.date_range('2021-01-01', periods=50, freq='H'),
                        'Nhiệt độ': np.random.randint(20, 40, 50),
                        'Độ ẩm': np.random.randint(0, 70, 50),
                        'CO': np.random.randint(0, 150, 50),
                        'PM 1': np.random.randint(5, 15, 50),
                        'PM 2.5': np.random.randint(0, 40, 50),
                        'PM 10': np.random.randint(20, 50, 50),
                        'Max': np.random.randint(20, 50, 50),
                        'Level': np.random.randint(1, 3, 50),
                    })
                    st.write(df)
                    
                with tab2:
                    df_chart = pd.DataFrame({
                        'Thời gian': pd.date_range('2021-01-01', periods=50, freq='H'),
                        'Giá trị': np.random.randint(20, 40, 50),
                        'col3': np.random.choice(['Nhiệt độ', 'Độ ẩm', 'CO', 'PM 1', 'PM 2.5', 'PM 10'], 50)  # Corrected to 50
                    })

                    st.write('Dữ liệu dạng biểu đồ')

                    st.area_chart(df_chart, x='Thời gian', y='Giá trị', color="col3", use_container_width=True)

            with col_search:
                with st.form("my_form"):
                    st.write('Tìm kiếm dữ liệu theo thời gian')

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