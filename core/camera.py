class Camera :
	def __init__(self, renderScale):
		self.windowOffset = (renderScale[0] * 0.5, renderScale[1] * 0.5)
		self.pos = [0, 0]

		self.target = None


	def setTarget(self, target):
		self.target = target


	def update(self):
		if self.target:
			self.pos[0] += (self.target.pos[0] - self.windowOffset[0] - self.pos[0]) * 0.25
			self.pos[1] += (self.target.pos[1] - self.windowOffset[1] - self.pos[1]) * 0.25