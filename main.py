# from BEnd.Handle_data import *
from BackEnd.sidebar import *
from FontEnd.home import *
from FontEnd.account import *
from FontEnd.monitor import *
from FontEnd.history import *


# # Configure the font end for web app
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


