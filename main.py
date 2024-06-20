import streamlit as st
from streamlit_option_menu import option_menu
from Util_Pages.home import Home
from Util_Pages.account import Account
from Util_Pages.controler import Controler
from Util_Pages.history import History

class MainApp:
    def __init__(self):
        self.home = Home()
        self.account = Account()
        self.controler = Controler()
        self.history = History()
    
    def run(self):
        st.set_page_config(page_title="Hệ thống giám sát môi trường",
                           page_icon=":globe_with_meridians:",
                           layout="wide")
        with st.sidebar:
            selected_page = option_menu(
                menu_title="Menu",
                options=["Home", "Tài khoản", "Quan sát", "Lịch sử"],
                icons=["house", "person-circle", "gear", "book"],
                menu_icon="cast",
                default_index=0
            )

        if selected_page == "Home":
            self.home.app()
        elif selected_page == "Tài khoản":
            self.account.app()
        elif selected_page == "Quan sát":
            self.controler.app()
        elif selected_page == "Lịch sử":
            self.history.app()

app = MainApp()
app.run()
