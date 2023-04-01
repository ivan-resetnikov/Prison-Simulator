import core.file as file



def save(prisonName:str) -> None:
	data = {
		# content to save
	}

	file.writeToJSON(f'data/saves/{prisonName}.json', data)


def load(prisonName:str) -> dict:
	data = file.readFromJSON(f'data/saves/{prisonName}.json')

	# assing values to player and level