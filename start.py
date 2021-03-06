from spock import Client
from spock.plugins import DefaultPlugins
from orderlistener import OrderListener
import orderlistener

from mobinfo import MobInfoPlugin



#Open login.py and put in your username and password
username = "s0lar"
#password = "notused"

plugins = DefaultPlugins
plugins.append(OrderListener)
plugins.append(MobInfoPlugin)


client = Client(plugins = plugins, username = username, authenticated=False)
#client.start() with no arguments will automatically connect to localhost
client.start('localhost', 25565)
