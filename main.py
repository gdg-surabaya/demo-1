from lib.listener.incoming_message import IncomingMessage
import falcon

api = falcon.API()
api.add_route("/incoming_message",IncomingMessage())