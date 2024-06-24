import streamlit as st
from BEnd.Handle_data import HandleData

class Account:
    def __init__(self):

        self.handle_data = HandleData()
        self.username = ""
        self.password = ""
        self.check_log = ""


    def app(self):
        if 'check_login' not in st.session_state:
            if self.getCheckLog() == "False":
                st.session_state.check_login = False
            else:
                st.session_state.check_login = True 

        st.subheader('Hệ thống giám sát môi trường', divider='rainbow')
        st.subheader('_Tài khoản người dùng_')

        self.handle_data.connectSQL()
        if st.session_state.check_login:
            st.write("Bạn đã đăng nhập.")
            if st.button("Đăng xuất"):
                st.session_state.check_login = False
                st.experimental_rerun()
        else:
            st.write("Bạn chưa đăng nhập. Hãy đăng nhập để sử dụng hệ thống.")
            if st.button("Đăng nhập"):
                self.login()

    @st.experimental_dialog("Đăng nhập")
    def login(self):
        with st.form("login_form"):
            username = st.text_input("Tài khoản:")
            password = st.text_input("Mật khẩu:", type="password")
            submit_button = st.form_submit_button("Xong")
            if submit_button:
                if username == "admin" and password == "admin":
                    st.success("Đăng nhập thành công")
                    st.session_state.check_login = True
                    st.experimental_rerun()
                elif not username:
                    st.error("Vui lòng nhập tài khoản")
                elif not password:
                    st.error("Vui lòng nhập mật khẩu")
                else:
                    st.error("Tài khoản hoặc mật khẩu không đúng")

    def isLogin(self):
        return st.session_state.check_login
    
    def getUsername(self):
        login_data_records = self.handle_data.select_login_data()
        for row in login_data_records:
            self.username = row[1]
        return self.username
    
    def getPassword(self):
        login_data_records = self.handle_data.select_login_data()
        for row in login_data_records:
            self.password = row[2]
        return self.password
    
    def getCheckLog(self):
        login_data_records = self.handle_data.select_login_data()
        for row in login_data_records:
            self.check_log = row[3]
        return self.check_log


        

    