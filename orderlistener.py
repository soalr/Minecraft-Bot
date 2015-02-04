"""
Just a dumb plugin to let me run !command arguments from ingame to fire off actions
I will probably turn this into a useful generic plugin at some point but for now
its just a testing bed for stuff
"""

from spock.mcp import mcdata
from spock.plugins import clientinfo

import datetime
import threading
import time

import sys

from bot import Bot
Bot = Bot()


class OrderListener:
	def __init__(self, ploader, settings):
		self.timers = ploader.requires('Timers')
		self.physics = ploader.requires('Physics')
		self.net = ploader.requires('Net')
		self.inventory = ploader.requires('Inventory')
		self.clinfo = ploader.requires('ClientInfo')
		ploader.reg_event_handler(
			'PLAY<Chat Message', self.handle_chat_message
		)
		ploader.reg_event_handler("PLAY<Entity Properties",Bot.updatePlayers)

	def handle_chat_message(self, name, packet):
		self.walk(0)
		chat_data = packet.data['json_data']
		message = self.parse_chat(chat_data)
		print('Chat:', message)
		try:
                        name_pos = message.find(' ')
			if name_pos == -1:
                                player_name='???'
                        else:
                                player_name=' '.join(message[:name_pos].split(' '))
                        message=message[name_pos+1:]
			command = message[message.index('!'):]
			args = []
			spacepos = command.find(' ')
			if spacepos == -1: #no arguments
				command = command[1:]
			else: #have arguments
				args = command[spacepos+1:].split(' ')
				command = command[1:spacepos]
			self.command_handle(player_name, command.strip(), args)
		except ValueError: #not a command so just move along
			pass

	def command_handle(self, player_name, command, args):
		if command == '':
			return
		print("Command:", command)
		if command == 'jump' or command == 'j':
			self.physics.jump()
		elif command == 'walk':
				walk(args[0]);
		elif command == 'attack':
			self.net.push_packet('PLAY>Use Entity', {'target':84204033,'action': 1})
		elif command == 'listplayers':
			Bot.listPlayers()
		elif command == 'login':
			self.net.push_packet('PLAY>Chat Message', {'message': '/login gabi'})
		elif command == 'date':
			self.net.push_packet('PLAY>Chat Message', {'message': 'Current Date: ' + str(datetime.datetime.now())})
		elif command == 'cmd':
			self.net.push_packet('PLAY>Chat Message', {'message': '/' + ' '.join(args)})
		elif command == 'slot':
			if len(args) == 1 and (int(args[0]) >= 0 and int(args[0]) <= 8):
				self.net.push_packet('PLAY>Held Item Change', {'slot': int(args[0])})
		elif command == 'place':
			#cur_pos_# 0-16
			# we can send held item of -1 and it will work might not be as clean but he still places the object because server side inventories
			block_data = {'location': {'x': int(args[0]),'y': int(args[1]),'z': int(args[2])}, 'direction':1, 'held_item': {'id': -1}, 'cur_pos_x': 8, 'cur_pos_y': 16, 'cur_pos_z': 8}
			print(block_data)
			self.net.push_packet('PLAY>Player Block Placement', block_data)
		elif command == 'inv':
			self.inventory.test_inventory()
                elif command == 'animation':
			self.net.push_packet('PLAY>Animation', '')
                elif command == 'pos':
                        print ('!!!',self.clinfo.position.get_dict())
                elif command == 'derp':
                        global inc
                        inc=0
                        self.timers.reg_event_timer(0.05, self.derp)
                elif command == 'home':
                        #e preciso fazer o boneco andar um pouco para ficar centrado num bloco para ele poder construir a casa a vontade sem colisoes
                        self.casota()

        def derp (self):
                global inc
                self.net.push_packet('PLAY>Player Look', {'yaw': float(inc), 'pitch': float(inc),'on_ground':0})
                self.physics.walk( float(inc))
                if inc == 360:
                        inc=0
                else:
                        inc=inc+10

        def casota (self):
                posicao=self.clinfo.position
                #centrar o player num unico bloco(+ ou meno 0.5)
                posicao.x=float(int(posicao.x)+0.5 )
                posicao.y=int(posicao.y)
                posicao.z=float(int(posicao.z)+0.5)
                #deslocar o player para a nova posicao
                self.net.push_packet('PLAY>Player Position', {'x': posicao.x ,'y': posicao.y,'z': posicao.z,'on_ground':1})
                #para colocar os blocos asseguir precisamos da posicao certa(inteiro)
                posicao.x=posicao.x-0.5
                posicao.y=posicao.y
                posicao.z=posicao.z-0.5

               #posicao=self.clinfo.position

               	for i in range(10):
                	block_data = {'location': {'x': posicao.x ,'y': posicao.y +2,'z': posicao.z}, 'direction':1, 'held_item': {'id': -1}, 'cur_pos_x': 8, 'cur_pos_y': 16, 'cur_pos_z': 8}
                	self.net.push_packet('PLAY>Player Block Placement', block_data)
                	posicao.x +=1;
                	self.net.push_packet('PLAY>Player Position', {'x': posicao.x ,'y': posicao.y,'z': posicao.z,'on_ground':1})
                	

	def parse_chat(self, chat_data):
		message = ''
		if type(chat_data) is dict:
                        if 'text' in chat_data:
                                message += chat_data['text']
				if 'extra' in chat_data:
					message += self.parse_chat(chat_data['extra'])
			elif 'translate' in chat_data:
				if 'with' in chat_data:
					message += self.parse_chat(chat_data['with'])
		elif type(chat_data) is list:
			for text in chat_data:
                                if type(text) is dict:
					message += self.parse_chat(text)
				elif type(text) is unicode:
					message += ' ' + text

		return message;

	def say(self,msg):
		self.net.push_packet('PLAY>Chat Message', {'message': + msg})
		
	def print_packets(self, name, packet):
		print(packet)
	def walk(self,args):
		angulo = args
		self.physics.walk( int(angulo))
