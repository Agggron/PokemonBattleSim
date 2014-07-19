class Team:
	''' A team holds six Pokémon and keeps track of the current Pokémon
	on the field. 

	>>> team1 = Team('Fantasy Pokemon League')
	>>> team1.add_pokemon('charizard')
	>>> team1.add_pokemon('gloom')
	>>> team1.add_pokemon('mew')
	>>> team1.print_team()
	Currently battling: []
	Alive Pokémon: ['charizard', 'gloom', 'mew']
	Fainted: []
	>>> team1.choose_battler()
	You choose who? 'gloom'
	>>> team1.print_team()
	Currently battling: ['gloom']
	Alive Pokémon: ['charizard', 'mew']
	Fainted: []
	>>> team1.faint_pokemon('gloom')
	>>> team1.print_team()
	Currently battling: []
	Alive Pokémon: ['charizard', 'mew']
	Fainted: ['gloom']
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

	def choose_battler(self):
		i_choose_you = input('You choose who? ')
		i_choose_you_without_strings = i_choose_you[1:len(i_choose_you) - 1]
		for member in self.team_members:
			if i_choose_you_without_strings == member:
				self.team_members.remove(member)
				self.on_field_member.append(member)
		# Add except statement for if the input does not match a battler.		

	def faint_pokemon(self, pokemon):
		for member in self.on_field_member:
			if member == pokemon:
				self.on_field_member.remove(pokemon)
				self.dead_members.append(pokemon)
		# Add except statement for if the input does not match a battler.

	def print_team(self):
		print("Currently battling:", self.on_field_member)
		print("Alive Pokémon:", self.team_members)
		print("Fainted:", self.dead_members)
