import json
import os

from ..model.messages import Message
from ..model.images import Image
from ..model.landmark_detection import LandmarkDetection
from ..model.smooch import Smooch

import falcon
import profig

class IncomingMessage:
	def on_post(self, req, res):
		body = req.stream.read()
		if not body:
			raise falcon.HTTPBadRequest("Empty Request Body", "A valid JSON document is required.")
		body = json.loads(body.decode("utf-8"))
		
		cfg = profig.Config(os.path.join(os.getcwd(), "config.ini"))
		cfg.sync()
		
		message = Message()
		message.parse_from(body["messages"][0])

		image = Image()
		image.download(message.media_url)
		
		reply = Message()
		reply.to = message.author_id
		try:
			vision = LandmarkDetection()
			vision.api_key = cfg["keys.api_key"]
			vision.detect(image)
			
			reply.text = "Ini adalah %s" % vision.landmark_name
		except AssertionError as ex:
			reply.text = str(ex)

		smooch = Smooch()
		smooch.jwt = cfg["keys.jwt_token"]
		smooch.send_message(role="appMaker", message=reply)

		res.status = falcon.HTTP_200