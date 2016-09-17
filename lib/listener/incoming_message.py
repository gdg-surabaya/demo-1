import requests
import falcon
import json
import shutil

class IncomingMessage:
	def on_post(self, req, res):
		body = req.stream.read()
		if not body:
			raise falcon.HTTPBadRequest("Empty Request Body", "A valid JSON document is required.")
		body = json.loads(body.decode("utf-8"))

		if "mediaUrl" in body["messages"][0]:
			media_url = body["messages"][0]["mediaUrl"]
			r = requests.get(media_url, stream=True)
			if r.status_code == 200:
				with open(os.path.join(os.getcwd(),"images.jpg"), "wb") as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw,f)

		res.status = falcon.HTTP_200