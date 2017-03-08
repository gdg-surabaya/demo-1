""" A module for Message """
class Message:
	""" A class for Message """
	def __init__(self, **kwargs):
		""" Initialze all needed variables. 
			type can be initialized by:
			- `type`
			
			media_url can be intialized by:
			- `mediaUrl`
			- `media_url`
			
			author_id can be initialized by:
			- `authorId`
			- `author_id`
			
			id can be initialized by:
			- `id`
			- `_id`
			
			to can be initialized by:
			- `to`
			
			text can be initialized by:
			- `text`
		"""
		self.type = kwargs.get("type", None)
		self.text = kwargs.get("text", None)
		self.to = kwargs.get("to", None)
		
		self.id = kwargs.get("_id", None)
		if self.id is None:
			self.id = kwargs.get("id", None)
		
		self.media_url = kwargs.get("mediaUrl", None)
		if self.media_url is None:
			self.media_url = kwargs.get("media_url", None)
		
		self.author_id = kwargs.get("authorId", None)
		if self.author_id is None:
			self.author_id = kwargs.get("author_id", None)
	
	def parse_from(self, something=None):
		assert something is not None, "something is not defined."
		assert isinstance(something, dict), "incorrect data type for something. Found %s" % type(something)
		self.__init__(**something)