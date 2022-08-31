from filedate import File

#-=-=-=-#

class Keep:
	"""Utility for "holding" and "dropping" file dates."""
	def __init__(self, Files: list):
		Files = list(Files) if isinstance(Files, list) else [Files]
		#---#
		self.files = Files

	def pick(self) -> dict:
		"""Pick the files dates."""
		self.__dates = {}

		for Path in self.files:
			self.__dates[Path] = File(Path).get()

	def drop(self):
		"""Drop the files dates."""
		for Key, Value in self.__dates.items():
			File(Key).set(
				created = Value["created"],
				modified = Value["modified"],
				accessed = Value["accessed"]
			)
	
	hold = pick
	release = drop

Batch = Keep