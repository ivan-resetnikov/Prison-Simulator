import core.constants as const



class Level:
	def __init__(self, info, tiles):
		self.name   = info['name']
		self.author = info['author']

		self.tiles = tiles


	def renderTiles(self, level, frame, cam):
		for tile in self.tiles[level]:
			pos = (
				tile.pos[0] - cam.pos[0],
				tile.pos[1] - cam.pos[1])

			if pos[0] > -const.TILE_SIZE and \
			   pos[1] > -const.TILE_SIZE and \
			   pos[0] < const.RENDER_SCALE[0] and \
			   pos[0] < const.RENDER_SCALE[1]:

				tile.render(frame, pos)


	def render(self, frame, cam, playerLevel):
		match playerLevel :
			case 'ground' :
				self.renderTiles('floor',  frame, cam)
				self.renderTiles('ground', frame, cam)