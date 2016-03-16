# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class api_login():

	def __init__(self):
		self.ngle = nGle_util()

		with open('scenario.json') as data_file:
			self.scenario = json.load(data_file)
		

	def loginTestPlayer(self):

		url_path = "/service/loginTestPlayer"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'])
		params = {
			"deviceId": self.scenario['deviceId'],
			"serialNo": "5858",
			"accessToken": self.scenario['deviceId'],
			"country": "kr",
			"lang": "ko",
			"market": self.scenario['market'],
			"appVer": self.scenario['appVer'],
			"sdkVer": self.scenario['sdkVer'],
			"os": self.scenario['os'],
			"osVer": "5.1.1",
			"telecom": "SKT",
			"deviceModel": "lge LG-F600K",
			"network": "3g",
			"loginType": "manual"
			}
		
		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		self.zat = data['zat']
		self.playerId = data['player']['playerId']

		return (status_code, data)

	

