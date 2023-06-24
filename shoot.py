import result

class Shoot:
	def __init__(self):
		self.row = 0
		self.col = 0
		self.res = result.INITIALIZED

	@property
	def row(self):
		return self._row

	@row.setter
	def row(self, value):
		self._row = value


	@property
	def col(self):
		return self._col

	@col.setter
	def col(self, value):
		self._col = value


	@property
	def res(self):
		return self._res

	@res.setter
	def res(self, value):
		self._res = value


	def is_missed(self):
		return self.res == result.MISSED

	def is_wounded(self):
		return self.res == result.WOUNDED

	def is_dead(self):
		return self.res == result.DEAD

	def is_end_game(self):
		return self.res == result.END_GAME

	def isValid(self):
		pass

	def makeInvalid(self):
		pass
