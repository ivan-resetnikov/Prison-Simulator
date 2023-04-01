import pygame as pg
core = None



class PrisonSimulator :
	def __init__ (self) :
		global core
		import core

		self.window = pg.display.set_mode(core.const.WINDOW_SIZE)
		self.frame  = pg.Surface(core.const.RENDER_SCALE)
		self.clock  = pg.time.Clock()

		pg.display.set_caption(core.const.TITLE)


	def run(self):
		self.onStart()

		self.running = True
		while self.running:
			for event in pg.event.get():
				match event.type:
					case pg.QUIT:
						self.running = False

			self.update()
			self.render()


	def update(self):
		pass


	def render(self):
		self.frame.fill((0, 0, 0))

		self.window.blit(pg.transform.scale(self.frame, core.const.WINDOW_SIZE), (0, 0))
		self.clock.tick(core.const.FPS)


	def onStart(self):
		pass


if __name__ == '__main__' :
	PrisonSimulator().run()