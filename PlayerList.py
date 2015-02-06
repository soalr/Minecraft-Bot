"""
Just a dumb plugin to let me run !command arguments from ingame to fire off actions
I will probably turn this into a useful generic plugin at some point but for now
its just a testing bed for stuff
"""

from spock.plugins import clientinfo
class properties:
	def __init__(self):
                self.name=''
                self.signature=''

class players:
	def __init__(self):
                self.action=0
                self.uuid=0
                self.name=''
                self.properties=properties()
                self.gamemode=0
                self.ping=0
                self.display_name=''
                self.is_online=False
                    

class PlayerListPlugin:
	def __init__(self, ploader, settings):
		self.clinfo = ploader.requires('ClientInfo')
		ploader.reg_event_handler(
			'PLAY<Player List Item', self.handle_player_list
		)
                
                self.player_listzadas = [players()]
		ploader.provides('player_listzadas', self.player_listzadas)
		
		
        def handle_player_list (self, name, packet):
                #self.player_listzadas.append(players())
                players=packet.data['player_list']
                
                
                #print('uuidzadas', (coiso[0])['uuid'])
                
                #print("playerlistzadas", packet.data['action'], 'player_listzadas', packet.data['player_list'], 'tamanho', len( packet.data['player_list']))
                
       