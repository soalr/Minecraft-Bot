"""
Basic demo example
"""

from spock import Client
from spock.plugins import DefaultPlugins
from demoplugin import DemoPlugin
from ChatCommand import ChatCommandPlugin
from PlayerList import PlayerListPlugin
from login import username

plugins = DefaultPlugins
#plugins.append(DemoPlugin)
plugins.append(ChatCommandPlugin)
plugins.append(PlayerListPlugin)
client = Client(plugins = plugins, username = username, authenticated=False)
#client.start() with no arguments will automatically connect to localhost
client.start('localhost', 25565)
