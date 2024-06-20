import streamlit as st
import mysql.connector

class Account:
    def __init__(self) -> None:
        return
    
    def app(self):
        @st.experimental_dialog("Đăng nhập")
        def login():
            global check_login
            with st.form("login_form"): 
                username = st.text_input("Tài khoản:")
                password = st.text_input("Mật khẩu:", type="password")
                if st.form_submit_button("Xong"):
                    if username == "admin" and password == "admin":
                        st.success("Đăng nhập thành công")
                        st.session_state.login = True
                        st.rerun()

                    elif not username:
                        st.error("Vui lòng nhập tài khoản")
                    elif not password:
                        st.error("Vui lòng nhập mật khẩu")
                    else:
                        st.error("Tài khoản hoặc mật khẩu không đúng")

        if "login" not in st.session_state:
            st.session_state.login = False
        if st.session_state.login:
            if st.button("Đăng xuất"):
                st.session_state.login = False
                st.experimental_rerun()
        else:
            
            if st.button("Đăng nhập"):
                login()

