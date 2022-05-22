# #import random
def games():
	pass
# 	#correctx = []
# 	game_keys = []
# 	game_values = []
# 	game = {{"What food was the character Pac Man modeled after": "Pizza"},
# 			{"What video game franchise has racked up over 100 Billion dollars in lawsuits": "Grand Theft Auto"},
# 			{"What game did the character Sonic first appear in": "Red Mobile"},
# 			{"What is the best selling video game of all time": "Minecraft"},
# 			{"What is the best-selling handheld gaming system to date": "Nintendo "},
# 			{"Mario first appeared in what video game": "Donkey Kong"}}
# 	for i in game.keys():
# 		game_keys.append(i)
# 	for i in game.values():
# 		game_values.append(i)
	#
	# for i in game_keys:
	# 	ans = input(f"{random.shuffle(0, game_keys)}")
	# 	if ans == :
	# 		pass
	# 	else:
	# 		x = print(input("Incorrect Answer!\nDo you wish to try again: "))
	# 		if x == "yes":
	# 			games()
	# 		else:
	# 			main_menu()
def main_menu():
	name = input("Your name please: ").title()
	print(f'Welcome {name}, Hope you are ready for the tests?')
	while True:
		categories = print(input(f"Categories:\n[1]: Gaming\n[2]: Sports\n[3]: Travell\nWhich categories do you want?: "))
		if categories == '1':
			games()
		elif categories == '2':
			pass
		elif categories == '3':
			pass
		else:
			print("invalid option")
			break


if __name__ == "__main__":
	main_menu()
