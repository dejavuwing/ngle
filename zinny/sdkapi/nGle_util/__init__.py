import httplib
import json
import random
import time, datetime
from websocket import create_connection

class nGle_util():

	def __init__(self):
		pass

	def get_headers(self, **kwargs):
		headers = {'Content-type': 'application/json;charset=UTF-8'}
		for name, value in kwargs.items():
			headers.update({name:value})
		return headers
		
	def https_post_getData(self, server, url_path, params, headers):
		conn = httplib.HTTPSConnection(server)
		params = json.dumps(params)
		conn.request("POST", url_path, params, headers)
		response = conn.getresponse()
		status_code = response.status
		data = json.loads(response.read())
		conn.close()
		return (status_code, data)

	def websocket_sendData(self, server, params):
		data = json.dumps(params)
		ws = create_connection(server)
		ws.send(data)
		result =  ws.recv()
		ws.close()
		return result

	def get_txNo(self):
		return random.randrange(1000000, 9999999)

	def get_timestamp_to_datetime(self, timestamp):
		timestamp = float(timestamp/1000.)		
		return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

	def get_time(self):
		return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

	def get_current_timestemp(self):
		return time.time()

