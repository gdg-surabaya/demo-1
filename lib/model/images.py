""" A module for Images """
import os
import base64
import shutil
import uuid

import requests

class Image:
	""" A class for Image """
	def __init__(self, **kwargs):
		self.name = kwargs.get("name", None)
		self.path = kwargs.get("path", None)
		
	@property
	def base64(self):
		""" Convert from binary to base64 image. """
		assert self.path is not None, "path is not defined."
		image_file = open(self.path, "rb")
		base64_image = base64.b64encode(image_file.read())
		return base64_image.decode("utf-8")
	
	def download(self, url=None):
		""" Download an image from given url,
			and save the image to path.
			
			Exceptions:
			- AssertionError
		"""
		assert url is not None, "url is not defined."
		
		r = requests.get(url, stream=True)
		assert r.status_code == 200, "cannot load image: %s" % r.status_code
		
		self.name = "%s.jpg" % uuid.uuid4()
		self.path = os.path.join(os.getcwd(), "images", self.name)
		with open(self.path, "wb") as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
		