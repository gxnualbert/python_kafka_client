from client_sdk import client_sdk
__version__ = "0.1"

#__all__ = ["client_sdk"]
class client_sdk(client_sdk):
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
#	def new(self, cp_addr, client_token, stream_id, subscribe_token):
#            a = client_sdk()
#            a.init()
#            a.login(cp_addr,client_token)
#            a.subscribe_audio_callback(stream_id, subscribe_token)
