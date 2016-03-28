# -*- coding: utf-8 -*-
import json
from nGle_util import nGle_util
from infodesk.infodesk_api import infodesk
from auth.auth_api import auth
from service.service_api import service


class run_scenario:
	def __init__(self):
		self.ngle = nGle_util()
		self.info = infodesk()
		self.auth = auth()
		self.service = service()

		with open('scenario001.json') as data_file:
			self.data = json.load(data_file)

	def _createZinnyDevice3Toen(self):
		
		send_data = {
			"server": self.data['server']['beta']['https'],
			"url_path": "/service/createZinnyDevice3Token",
			"appId":self.data['app']['appId'],
			"appSecret": self.data['app']['appSecret'],
			"deviceId": self.data['app']['deviceId'],
			"serialNo": self.data['app']['serialNo'],
			"market": self.data['app']['market'],
			"appVer": self.data['app']['appVer'],
			"sdkVer": self.data['app']['sdkVer'],
			"os": self.data['app']['os']
			}

		status_code, data = self.service.createZinnyDevice3Token(send_data)
		self.accessToken = data['accessToken']

		return (status_code, data)


	def _getAppClient(self):

		send_data = {
			"server": self.data['server']['beta']['wss'],
			"uri": 'infodesk://v2/getAppClient',
			"txNo": self.ngle.get_txNo(),
			"appId": self.data['app']['appId'],
			"appSecret": self.data['app']['appSecret'],
			"accessToken": self.accessToken,
			"country": self.data['app']['country'],
			"lang": self.data['app']['lang'],
			"appVer": self.data['app']['appVer'],
			"sdkVer": self.data['app']['sdkVer'],
			"os": self.data['app']['os'],
			"osVer": self.data['app']['osVer'],
			"market": self.data['app']['market'],
			"deviceId": self.data['app']['deviceId'],
			"serialNo": self.data['app']['serialNo'],
			"telecom": self.data['app']['telecom'],
			"deviceModel": self.data['app']['deviceModel'],
			"network": self.data['app']['network'],
			"loginType": self.data['app']['loginType']
		}

		data = self.info.getAppClient(send_data)
		return data

	def _loginZinnyDevice3(self):
		send_data = {
			"server": self.data['server']['beta']['wss'],
			"uri": "auth://v2/auth/loginZinnyDevice3",
			"txNo": self.ngle.get_txNo(),
			"appId": self.data['app']['appId'],
			"appSecret": self.data['app']['appSecret'],
			"accessToken": self.accessToken,
			"country": self.data['app']['country'],
			"lang": self.data['app']['lang'],
			"appVer": self.data['app']['appVer'],
			"sdkVer": self.data['app']['sdkVer'],
			"os": self.data['app']['os'],
			"osVer": self.data['app']['osVer'],
			"market": self.data['app']['market'],
			"deviceId": self.data['app']['deviceId'],
			"serialNo": self.data['app']['serialNo'],
			"telecom": self.data['app']['telecom'],
			"deviceModel": self.data['app']['deviceModel'],
			"network": self.data['app']['network'],
			"loginType": self.data['app']['loginType']
		}

		data = self.auth.loginZinnyDevice3(send_data)
		return data



if __name__=='__main__':
	s = run_scenario()
	
	status_code, data = s._createZinnyDevice3Toen()
	print str(status_code) + " " + str(data) + "\n" + '-' * 80

	data = s._getAppClient()
	print str(data) + "\n" + '-' * 80

	data = s._loginZinnyDevice3()
	print str(data) + "\n" + '-' * 80






