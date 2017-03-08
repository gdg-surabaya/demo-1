""" A module for Smooch API """
import json

from .messages import Message

import requests

class Smooch:
	""" A class for bridging Smooch """
	def __init__(self, **kwargs):
		self.jwt = kwargs.get("jwt", None)
		self.accepted_roles = ["appMaker", "appUser"]
	
	def send_message(self, role=None, message=None):
		""" Send a message to someone.
			If your role is appMaker, you send a message from appMaker to appUser
			so the otherwise
			
			Exceptions:
			- AssertionError
		"""
		assert self.jwt is not None, "jwt is not defined."
		assert role is not None, "role is not defined."
		assert role in self.accepted_roles, "role is not accepted."
		assert message is not None, "message is not defined."
		assert isinstance(message, Message), "incorrect data type for message. Found %s" % type(message)
		assert message.to is not None, "message.to is not defined."
		assert message.text is not None, "message.text is not defined."
		
		r = requests.post(
			"https://api.smooch.io/v1/appusers/%s/messages" % message.to,
			data=json.dumps({
				"role": role,
				"text": message.text,
				"type": "text"
			}),
			headers={
				"Content-Type": "application/json",
				"Authorization": "Bearer %s" % self.jwt
			}
		)
		