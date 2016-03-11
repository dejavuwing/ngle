import httplib
import json

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


