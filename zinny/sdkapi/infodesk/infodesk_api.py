# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class infodesk():

	def __init__(self):
		self.ngle = nGle_util()

	def getAppClient(self, send_data):
		sd = send_data

		server = sd['server']

		data = [
			sd['uri'],
			{
				"txNo": sd['txNo']
			},
			{
				"appId": sd['appId'],
				"appSecret": sd['appSecret'],
				"appVer": sd['appVer'],
				"sdkVer": sd['sdkVer'],
				"os": sd['os'],
				"market": sd['market'],
				"deviceId": sd['deviceId'],
				"serialNo": sd['serialNo']
			}
		]
		
		data = self.ngle.websocket_sendData(server, data)
		return data

		
