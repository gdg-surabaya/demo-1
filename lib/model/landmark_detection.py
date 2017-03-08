""" A LandmarkDetection module """
import copy
import json

from .images import Image

import requests

class LandmarkDetection:
	""" A LandmarkDetection class """
	def __init__(self, **kwargs):
		self.image = kwargs.get("image", None)
		self.api_key = kwargs.get("api_key", None)
		self.landmark_name = kwargs.get("landmark_name", None)
		
	@property
	def request_document(self):
		""" Generate request document that will be sent to
			API.
			Exceptions:
			- AssertionError
		"""
		assert self.image is not None, "image is not defined."
		return {"requests":[{
			"image": {"content": self.image.base64},
			"features":[{
				"type": "LANDMARK_DETECTION",
				"maxResults": 1
			}]
		}]}

	def detect(self, image=None):
		""" Detect a landmark based on given image.
			Exceptions:
			- AssertionError
		"""
		assert image is not None, "image is not defined."
		assert isinstance(image, Image), "incorrect data type for image. Found %s" % type(image)
		assert self.api_key is not None, "api_key is not defined."
		
		self.image = copy.copy(image)
		r = requests.post(
			"https://vision.googleapis.com/v1/images:annotate?key=%s" % self.api_key,
			data=json.dumps(self.request_document),
			headers={"Content-Type": "application/json"}
		)
		
		responses = r.json()["responses"]
		assert len(responses) > 0, "Detection failed! try another image!"
		assert "landmarkAnnotations" in responses[0], "Detection failed! try another image!"
		self.landmark_name = responses[0] \
									  ["landmarkAnnotations"][0] \
									  ["description"]
		