

from spock.utils import pl_announce
from spock.mcp.mcdata import (
	FLG_XPOS_REL, FLG_YPOS_REL, FLG_ZPOS_REL, FLG_YROT_REL, FLG_XROT_REL
)

class Info(object):
	pass

class Position(Info):
	def __init__(self):
		self.eid  = 0
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0

class Mob(Info):
	def __init__(self):
		self.Position

class MobInfo:
	def __init__(self):
		self.moblist = {}

	def reset(self):
		self.__init__()

@pl_announce('MobInfo')
class MobInfoPlugin:
	def __init__(self, ploader, settings):
		self.event = ploader.requires('Event')
		ploader.reg_event_handler('PLAY<Spawn Mob', self.handle_spawn_mob)
		ploader.reg_event_handler('PLAY<Entity Relative Move', self.handle_relative_movement)
		ploader.reg_event_handler('PLAY<Entity Look and Relative Move', self.handle_look_and_relative_movement)

		self.mob_info = MobInfo()
		ploader.provides('MobInfo', self.mob_info)




	def handle_spawn_mob(self, event, packet): # se o eid nao estiver no dicionario, acrescentar
		eid = packet.data['eid']

		if eid in self.mob_info.moblist.keys():
			pass
		else:
			self.mob_info.moblist['eid'] = Position()

	def handle_relative_movement(self,event,packet):
		eid = packet.data['eid']
		dx = packet.data['dx']
		dz = packet.data['dz']
		dy = packet.data['dy']

		if eid in self.mob_info.moblist.keys():
			oldPos = self.mob_info.moblist['eid']
			newPos = Position()
			newPos.x = oldPos.x + dx
			newPos.y = oldPos.y + dy
			newPos.z = oldPos.z + dz
			self.mob_info.moblist['eid'] = newPos

	def handle_look_and_relative_movement(self,event,packet):
		pass
