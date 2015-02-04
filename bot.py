class Bot:
	global players
	players = dict() #dictionario {uuid:eid}

	def updatePlayers(self, name, packet):
		if (packet.data['eid']) in players.keys():
			players[packet.data['eid']] = packet.data['properties']
		else:
			players[packet.data['eid']] = dict()
		pass


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

	def listPlayers(self):
		print players