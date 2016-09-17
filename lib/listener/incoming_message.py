import requests
import falcon
import json
import shutil
import os
import base64

class IncomingMessage:
	def on_post(self, req, res):
		body = req.stream.read()
		if not body:
			raise falcon.HTTPBadRequest("Empty Request Body", "A valid JSON document is required.")
		body = json.loads(body.decode("utf-8"))
		print(json.dumps(body, indent=4))
		if "mediaUrl" in body["messages"][0]:
			media_url = body["messages"][0]["mediaUrl"]
			r = requests.get(media_url, stream=True)
			if r.status_code == 200:
				with open(os.path.join(os.getcwd(),"images.jpg"), "wb") as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw,f)
			image_content = open(os.path.join(os.getcwd(), "images.jpg"),"rb")
			encoded_image = base64.b64encode(image_content.read())
			encoded_image = encoded_image.decode("utf-8")
			
			request_document = {
			  "requests":[
			    {
			      "image":{
			        "content": encoded_image
			      },
			      "features": [
			        {
			          "type":"LANDMARK_DETECTION",
			          "maxResults":1
			        }
			      ]
			    }
			  ]
			}
			r = requests.post(
				"https://vision.googleapis.com/v1/images:annotate?key=%s" % ("AIzaSyCIzFcPY7DMsUZgR4h22MOP45Wh-RXtS4k"), 
				data=json.dumps(request_document),
				headers={'Content-Type': 'application/json'}
			)
			
			vision_response = r.json()["responses"][0]["landmarkAnnotations"][0]
			print("Ini adalah %s" % vision_response["description"])
		res.status = falcon.HTTP_200