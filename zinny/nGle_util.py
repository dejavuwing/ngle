import httplib
import json
import time, datetime

class nGle_util():

	def __init__(self):
		pass

	def get_headers(self, **kwargs):
		headers = {'Content-type': 'application/json;charset=UTF-8'}
		for name, value in kwargs.items():
			headers.update({name:value})

		return headers
		
	def https_post_getData(self, rul_path, params, headers):
		self.beta_server = 'beta-openapi-zinny.nzincorp.com'

		conn = httplib.HTTPSConnection(self.beta_server)
		params = json.dumps(params)
		conn.request("POST", rul_path, params, headers)
		response = conn.getresponse()
		status_code = response.status
		data = json.loads(response.read())
		conn.close()

		return (status_code, data)

	def get_timestamp_to_datetime(self, timestamp):
		timestamp = float(timestamp/1000.)
		return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

	def get_time(self):
		return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

	def get_current_timestemp(self):
		return time.time()




