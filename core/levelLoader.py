import core.constants as const
import core.assets as assets
import core.file as file

import shutil
import os

from core.level import Level



class Tile:
	def __init__(self, pos, name):
		self.img = assets.loadImage(
			f'assets/tiles/{name}.png',
			'(t)' in name,
			(const.TILE_SIZE, const.TILE_SIZE))

		self.pos = pos


	def render (self, frame, pos) :
		frame.blit(self.img, pos)



def createLevel(name):
	info = file.readFromJSON(f'data/temp/{name}/info.json')

	tiles = {'floor': [], 'ground': []}
	
	for layer in tuple(tiles.keys()) :

		for y, line in enumerate(info['levels'][layer]):
			for x, char in enumerate(line):

				if not char == ' ' :
					tiles[layer].append(Tile(
						(x * const.TILE_SIZE, y * const.TILE_SIZE),
						const.TILE_CODES[char]
					))

	return Level(info, tiles)


def loadLevels():
	for prisonName in os.listdir('data/prisons'):
		if not os.path.exists(f'data/temp/{prisonName}') :

			if prisonName[-4::] == '.zip':
				os.makedir(f'data/temp/{prisonName}')
				file.unzipArchieve(
					f'data/prisons/{prisonName}',
					f'data/temp/{prisonName}')

			else :
				shutil.copytree(
					f'data/prisons/{prisonName}',
					f'data/temp/{prisonName}')


def unloadLevels():
	for prisonName in os.listdir('data/temp'):
		shutil.rmtree(f'data/temp/{prisonName}')