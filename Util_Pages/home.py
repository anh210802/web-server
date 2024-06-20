import streamlit as st

class Home:
    def __init__(self) -> None:
        return

    def app(self):     
        st.header("Giới thiệu")
        st.write("Hệ thống giám sát môi trường là hệ thống giám sát môi trường trực tuyến.")
        st.write("Hệ thống giám sát môi trường sử dụng các cảm biến để đo lường các thông số môi trường như nhiệt độ, độ ẩm, khí CO, PM 1, PM 2.5, PM 10.")
        st.image('image/img1.jpg', width=600)

