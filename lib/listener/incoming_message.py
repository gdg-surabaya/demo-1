import falcon

class IncomingMessage:
	def on_post(self, req, res):
		print(req.body)
		res.status = falcon.HTTP_200