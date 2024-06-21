# from BEnd.Handle_data import *
from BEnd.sidebar import *
from FEnd.home import *
from FEnd.account import *
from FEnd.monitor import *
from FEnd.history import *


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


