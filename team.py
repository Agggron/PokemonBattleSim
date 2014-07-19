class Team:
	''' A team holds six Pokémon and keeps track of the current Pokémon
	on the field. 
	'''

	def __init__(self, player):
		self.team_members = []
		self.on_field_member = []
		self.dead_members = []
		self.pokemon_number = 0
		self.player = player

	def add_pokemon(self, pokemon):
		self.team_members += [pokemon]
		self.pokemon_number += 1

	# def choose_battler(self):
		# print(input('You choose who? '))
		#

	def faint_pokemon(self, pokemon):
		for member in self.team_members:
			if member == pokemon:
				self.team_members.remove(pokemon)
				self.dead_members.append(pokemon)

	def print_team(self):
		print("Currently battling:", self.on_field_member)
		print("Alive Pokémon:", self.team_members)
		print("Fainted:", self.dead_members)
