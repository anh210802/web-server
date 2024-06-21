import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

class Monitor:
    def __init__(self) -> None:
        self.check_login = False
        self.temp = 30
        self.humi = 50
        self.co = 100
        self.pm1 = 10
        self.pm25 = 20
        self.pm10 = 30
        
    def app(self, log):
        self.check_login = log
        st.subheader('Hệ thống giám sát môi trường', divider='rainbow')
        st.subheader('_Giám sát cảm biến_')
            
        if self.check_login:
            pre_temp = 0
            pre_humi = 0
            pre_co = 0
            pre_pm1 = 0
            pre_pm25 = 0
            pre_pm10 = 0

            header = st.container(border=True)
            col1, col2, col3 = header.columns(3)

            # col1_container = col1.container(height=150)
            # col1_col1 , col2_col1 = col1_container.columns(2)
            # col1_col1.image('image/temp.jpg', width=100)
            # col2_col1.metric("Nhiệt độ", f"{self.temp}°C", "1.2°C", label_visibility = "visible")

            # col2_container = col2.container(height=150)
            # col1_col2, col2_col2 = col2_container.columns(2)
            # col1_col2.image('image/humi.jpg', width=100)
            # col2_col2.metric("Độ ẩm", f"{self.humi}%", "-4%")

            # col3_container = col3.container(height=150)
            # col1_col3, col2_col3 = col3_container.columns(2)
            # col1_col3.image('image/co.jpg', width=100)
            # col2_col3.metric("Khí CO", f"{self.co}%", "4%")

            col1.metric("Nhiệt độ", f"{self.temp} °C", "1.2°C")
            col2.metric("Độ ẩm", f"{self.humi} %", "1.2%")
            col3.metric("Khí CO", f"{self.co} ppm", "1.2ppm")

            header = st.container(border=True)
            col1, col2, col3 = header.columns(3)

            col1.metric("PM 1", f"{self.pm1} µg/m³", "1.2µg/m³")
            col2.metric("PM 2.5", f"{self.pm25} µg/m³", "1.2µg/m³")
            col3.metric("PM 10", f"{self.pm10} µg/m³", "1.2µg/m³")

            style_metric_cards(
                "#FFFFFF",
                2,
                "#CCC",
                5,
                "#9AD8E1",
                True,
            )
            
        else:
            st.write("Bạn chưa đăng nhập. Hãy đăng nhập để sử dụng hệ thống.")

    def setData(self, data):
        self.temp = data[0]
        self.humi = data[1]
        self.co = data[2]
        self.pm1 = data[3]
        self.pm25 = data[4]
        self.pm10 = data[5]
    
        