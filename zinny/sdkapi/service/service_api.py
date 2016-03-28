# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class service():

	def __init__(self):
		self.ngle = nGle_util()

	def createZinnyDevice3Token(self, send_data):
		sd = send_data

		server = sd['server']
		url_path = sd['url_path']

		headers = self.ngle.get_headers(appId = sd['appId'], appSecret = sd['appSecret'])

		params = {
			"deviceId": sd['deviceId'],
			"serialNo": sd['serialNo'],
			"market": sd['market'],
			"appVer": sd['appVer'],
			"sdkVer": sd['sdkVer'],
			"os": sd['os']
			}
		
		status_code, data = self.ngle.https_post_getData(server, url_path, params, headers)
		return (status_code, data)