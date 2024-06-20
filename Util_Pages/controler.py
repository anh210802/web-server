import streamlit as st


class Controler:
    def __init__(self) -> None:
        return
    
    def app(self):
        st.write("This is a controler page")

# Initial values for environmental parameters
# temp = 30
# humi = 60
# co = 86
# pm1 = 1.2
# pm25 = 20
# pm10 = 40

# # Set page configuration
# st.set_page_config(page_title="Bảng điều khiển", page_icon=":shark:", layout="wide")

# # Initialize login state if not already done
# if "login" not in st.session_state:
#     st.session_state.login = False

# # Title of the app
# st.title("Hệ thống giám sát môi trường")

# # Navigation bar
# header = st.container()
# col1, col2, col3, col4 = header.columns(4)

# with col1:
#     st.link_button("Trang chủ", "Home", use_container_width=True, type="primary")
# with col2:
#     st.link_button("Bảng điều khiển", "Controler", use_container_width=True, disabled = False, type="primary")
# with col3:
#     st.link_button("Lịch sử", "History", use_container_width=True, disabled = False, type="primary")  
# with col4:
#     if st.button("Đăng xuất", use_container_width=True, type="primary"):
#         st.session_state.login = False
#         st.experimental_rerun()

# # Content based on login state
# if st.session_state.login:
#     st.header("Bảng điều khiển")
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         col1_col1, col2_col1 = st.columns(2)
#         col1_col1.image('image/temp.jpg', width=100)
#         col2_col1.metric("Nhiệt độ", f"{temp}°C", "1.2°C")

#     with col2:
#         col1_col2, col2_col2 = st.columns(2)
#         col1_col2.image('image/humi.jpg', width=100)
#         col2_col2.metric("Độ ẩm", f"{humi}%", "-4%")

#     with col3:
#         col1_col3, col2_col3 = st.columns(2)
#         col1_col3.image('image/co.jpg', width=100)
#         col2_col3.metric("Khí CO", f"{co} ppm", "4 ppm")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         col1_col1, col2_col1 = st.columns(2)
#         col1_col1.image('image/pm1.jpg', width=100)
#         col2_col1.metric("PM 1", f"{pm1} μg/m³", "1.2 μg/m³")

#     with col2:
#         col1_col2, col2_col2 = st.columns(2)
#         col1_col2.image('image/pm25.jpg', width=100)
#         col2_col2.metric("PM 2.5", f"{pm25} μg/m³", "30 μg/m³")

#     with col3:
#         col1_col3, col2_col3 = st.columns(2)
#         col1_col3.image('image/pm10.jpg', width=100)
#         col2_col3.metric("PM 10", f"{pm10} μg/m³", "4 μg/m³")
# else:
#     # login()
#     pass