# -*- coding: utf-8 -*-
import httplib
import json

from nGle_util import nGle_util


class APITest():

	def __init__(self):
		self.ngle = nGle_util()

		self.appId = 'test03'
		self.appSecret = '67fcd4ed73ead0f278ba43e7d5c72afd292ebead'
		self.deviceId = '8523698741'
		self.market = 'googlePlay'
		self.appVer = '0.1.0'
		self.sdkVer = '2.12.0'
		self.os = 'android'
		pass

	def loginTestPlayer(self):
		'''
		테스트 사용자로 로그인합니다. 만약 이전에 로그인한 적이 없다면 새로운 사용자를 생성합니다.
		이 API를 통해 테스트용 사용자를 생성할 수 있습니다.
		http://wiki.nzincorp.com/display/ZP/loginTestPlayer
		'''

		url_path = "/service/loginTestPlayer"
		headers = self.ngle.get_headers(
			appId = self.appId,
			appSecret = self.appSecret)
		params = {
        	"deviceId": self.deviceId,
        	"serialNo": "5858",
        	"accessToken": self.deviceId,
        	"country": "kr",
	        "lang": "ko",
    	    "market": self.market,
        	"appVer": self.appVer,
        	"sdkVer": self.sdkVer,
        	"os": self.os,
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


	def validateZinnyAccessToken(self, inPlayerId=None, inZat=None):
		'''
		인증토큰(zat)이 유효한지 체크한다. Status Code가 200일 경우, 인증된 것으로 처리하면 된다.
		http://wiki.nzincorp.com/display/ZP/validateZinnyAccessToken
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if inZat == None:
			inZat = self.zat

		url_path = "/service/validateZinnyAccessToken"
		headers = self.ngle.get_headers(
			appId = self.appId,
			appSecret = self.appSecret,
			playerId = inPlayerId,
			zat = inZat)
		params = {}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)

		return (status_code, data)

	def refreshZinnyAccessToken(self, inPlayerId=None, inZat=None):
		'''
		인증 토큰을 갱신한다.
		Zinny SDK를 적용한 게임이라면 인증토큰이 필요한 경우, 항상 클라이언트를 통해 인증토큰을
		얻어와야하기 때문에 이 API는 서버에서 호출할 필요가 없다.
		http://wiki.nzincorp.com/display/ZP/refreshZinnyAccessToken
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if inZat == None:
			inZat = self.zat

		url_path = "/service/refreshZinnyAccessToken"
		headers = self.ngle.get_headers(
			appId = self.appId,
			appSecret = self.appSecret,
			playerId = inPlayerId,
			zat = inZat)
		params = {
			"appVer": self.appVer,
			"sdkVer": self.sdkVer,
			"os": self.os,
			"market": self.market,
        	"deviceId": self.deviceId
		}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		self.zat = data['zat']

		return (status_code, data)

	def sendMessage(self, inPlayerId=None):
		'''
		메시지 배송 서버로 다른 유저에게 메시지를 전달 요청을 한다.
		첨부는 item만 등록가능하다.
		http://wiki.nzincorp.com/display/ZP/sendMessage
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/sendMessage"
		headers = self.ngle.get_headers(
			appId = self.appId,
			appSecret = self.appSecret,
			playerId = inPlayerId)
		params = {
        	"receiverId": inPlayerId,
        	"message": {
            	"messageBoxId": "api_test",           
            	"title": "api test : title",
            	"body": "api test : body",
            	"resourceMap": {
                	"imageLink": "test://api"
            	}
        	},
        	"items": [{
	                "itemCode": "api_item_1",
	                "quantity": 100,
	                "validityTime": 3600000        
            	}]
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)

		return (status_code, data)

	def getReceivedMessages(self, inPlayerId=None):
		'''
		메시지 배송 서버로 전달된 메시지 목록을 조회한다.
		조회된 목록은 시간 역순으로 가장 최신 메시지가 첫페이지로 조회 된다.
		메시지에는 복수개의 첨부아이템 목록이 존재한다.
		http://wiki.nzincorp.com/display/ZP/getReceivedMessages
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/getReceivedMessages"
		headers = self.ngle.get_headers(
			appId = self.appId,
			appSecret = self.appSecret,
			playerId = inPlayerId)
		params = {
			"messageBoxId":"api_test",
			"count": 20
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		self.item_totalCount = data['totalCount']
		
		self.itemIds = []
		if self.item_totalCount >= 20:
			self.item_totalCount = 20

		for i in range(self.item_totalCount):
			self.itemIds.append(str(data['messages'][i]['items'][0]['itemId']))

		return (status_code, data)

if __name__=='__main__':
	api = APITest()
	
	status_code, data = api.loginTestPlayer()
	print '-' * 80
	print status_code, data
	print '-' * 80

	status_code, data = api.validateZinnyAccessToken()
	print status_code, data
	print '-' * 80

	# status_code, data = api.refreshZinnyAccessToken()
	# print status_code, data
	# print '-' * 80

	# status_code, data = api.sendMessage()
	# print status_code, data
	# print '-' * 80

	status_code, data = api.getReceivedMessages()
	print status_code, data
	print '-' * 80

	

