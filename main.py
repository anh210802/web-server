# Description: This is the main file for the web app. It will run the web app and configure the front end and back end of the web app.
from BackEnd.sidebar import *
from FontEnd.home import *
from FontEnd.account import *
from FontEnd.monitor import *
from FontEnd.history import *
from BackEnd.server import *
import threading


# Configure the font end for web app
home = Home()
account = Account()
monitor = Monitor()
history = History()

# Configure the back end for web app
# Configure the images
home.setImage1('image/img1.jpg')
home.setImage2('image/img2.jpg')

sidebar = Sidebar(home, account, monitor, history)
sidebar.run()

# Configure the server
server = Server('177.30.34.76', 2108)
threading.Thread(target=server.start).start()
# server.start()

