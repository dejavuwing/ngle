# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class openapi_temp():

	def __init__(self):
		self.ngle = nGle_util()

		with open('scenario.json') as data_file:
			self.scenario = json.load(data_file)

	def loginTestPlayer(self):
		'''
		http://wiki.nzincorp.com/display/ZP/loginTestPlayer
		'''

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

	def validateZinnyAccessToken(self, inPlayerId=None, inZat=None):
		'''
		http://wiki.nzincorp.com/display/ZP/validateZinnyAccessToken
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if inZat == None:
			inZat = self.zat

		url_path = "/service/validateZinnyAccessToken"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId,
			zat = inZat)
		params = {}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)

		return (status_code, data)

	def refreshZinnyAccessToken(self, inPlayerId=None, inZat=None):
		'''
		http://wiki.nzincorp.com/display/ZP/refreshZinnyAccessToken
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if inZat == None:
			inZat = self.zat

		url_path = "/service/refreshZinnyAccessToken"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId,
			zat = inZat)
		params = {
			"appVer": self.scenario['appVer'],
			"sdkVer": self.scenario['sdkVer'],
			"os": self.scenario['os'],
			"market": self.scenario['market'],
			"deviceId": self.scenario['deviceId']
		}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		self.zat = data['zat']

		return (status_code, data)

	def sendMessage(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/sendMessage
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/sendMessage"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
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

	def getReceivedMessages(self, inPlayerId=None, list_count=20):
		'''
		http://wiki.nzincorp.com/display/ZP/getReceivedMessages
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/getReceivedMessages"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"messageBoxId":"api_test",
			"count": list_count
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		self.item_totalCount = data['totalCount']

		if self.item_totalCount >= 20:
			self.item_totalCount = 20

		self.itemIds = []
		self.messageIds = []
		if self.item_totalCount > 0:
			for i in range(list_count):
				self.itemIds.append(str(data['messages'][i]['items'][0]['itemId']))
				self.messageIds.append(str(data['messages'][i]['message']['messageId']))

		self.claim_itemId = []
		self.claim_messageId = []
		if self.item_totalCount > 0:
			self.claim_itemId.append(str(data['messages'][0]['items'][0]['itemId']))
			self.claim_messageId.append(str(data['messages'][0]['message']['messageId']))

		return (status_code, data)

	def claimAttachedItems(self, inPlayerId=None, itemIds=[]):
		'''
		http://wiki.nzincorp.com/display/ZP/claimAttachedItems
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if len(itemIds) == 0:
			in_claim_itemId = self.claim_itemId
		else:
			in_claim_itemId = itemIds

		url_path = "/service/claimAttachedItems"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"itemIds": in_claim_itemId
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)

		return (status_code, data)

	def confirmAttachedItems(self, inPlayerId=None, itemIds=[]):
		'''
		http://wiki.nzincorp.com/display/ZP/confirmAttachedItems
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if len(itemIds) == 0:
			in_claim_itemId = self.claim_itemId
		else:
			in_claim_itemId = itemIds

		url_path = "/service/confirmAttachedItems"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"itemIds": in_claim_itemId
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)

		return (status_code, data)

	def claimItems(self, inPlayerId=None, messageIds=[]):
		'''
		http://wiki.nzincorp.com/display/ZP/claimItems
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if len(messageIds) == 0:
			in_claim_messageId = self.messageIds
		else:
			in_claim_messageId = messageIds

		url_path = "/service/claimItems"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"messageIds": in_claim_messageId
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def confirmItems(self, inPlayerId=None, messageIds=[]):
		'''
		http://wiki.nzincorp.com/display/ZP/confirmItems
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if len(messageIds) == 0:
			in_claim_messageId = self.messageIds
		else:
			in_claim_messageId = messageIds

		url_path = "/service/confirmItems"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"messageIds": in_claim_messageId
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def finishMessages(self, inPlayerId=None, messageIds=[]):
		'''
		http://wiki.nzincorp.com/display/ZP/finishMessages
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		if len(messageIds) == 0:
			in_claim_messageId = self.messageIds
		else:
			in_claim_messageId = messageIds

		url_path = "/service/confirmItems"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"messageIds": in_claim_messageId
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def writePurchaseLog(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/writePurchaseLog
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/writePurchaseLog"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"grade": 100,
			"currency": "USD",
			"price": 12.23, 
			"os": "android",
			"market": "googlePlay",
			"marketOrderId": "123098120938.123123123",
			"marketProductId": "API Test Item 0003",
			"marketPurchaseTime": self.ngle.get_current_timestemp()
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def writeResourceLog(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/writeResourceLog
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/writeResourceLog"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"grade":"1",
			"rCurrency" : "al",
			"delta" : 120000,
			"amount" : 56000000,
			"modType" : "add",
			"modTime" : self.ngle.get_current_timestemp(),
			"reason" : "일반알농장",
			"subReason" : "free"
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def writeActionLog(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/writeActionLog
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/writeActionLog"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"grade": 11,
			"category": "tutorial",
			"action": "skip",
			"modTm": self.ngle.get_current_timestemp()
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def writeRoundLog(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/writeRoundLog
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/writeRoundLog"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"gameMode": "월드투어",
			"gameModeDtl": "북미오픈 1차전",
			"resultTp": "win",
			"energyAmt": 41234,
			"roundExp": 321,
			"startTime": 1444748400000,
			"endTime": 1444748430000,
			"character1Id": "레이첼",
			"character2Id": "제이슨",
			"character3Id": "세레나",
			"character1Lv": 13,
			"character2Lv": 1,
			"character3Lv": 23
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def writeItemLog(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/writeItemLog
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/writeItemLog"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"appId": self.scenario['appId'],
			"playerId": inPlayerId,
			"itemType": "grip",
			"itemId": "superultragrip",
			"itemAttr1": "lv4",
			"itemAttr2": "*",
			"quantity": 1,
			"rCurrency": "gold",
			"cost": 1,
			"reason": "buy",
			"subReason": "*"
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def sendPush(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/sendPush
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/sendPush"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"titleMap":{"en":"oepnAPI Test Title"},
			"bodyMap":{"en":"oepnAPI Test Body"},
			"ticker":"openAPI",
			"playerIds":self.scenario['push_receiver_Ids']
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def sendOnlinePush(self):
		'''
		http://wiki.nzincorp.com/display/ZP/sendOnlinePush
		'''

		url_path = "/service/sendOnlinePush"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'])
		params = {
			"playerIds":self.scenario['push_receiver_Ids'],
			"body" : {
				"uri":"achievement://v1/achievement/getRewards",                  
				"rewardsMap": {
					"CWC_ACHV01":[
						{
							"masteryGrade": 1,
							"regTime": 1421893909000
						},
						{
							"masteryGrade": 2,
							"regTime": 1421893912000
						}
					]
				}
			}
		}

		# None Response Content 
		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def sendAllOnlinePush(self):
		'''
		http://wiki.nzincorp.com/display/ZP/sendAllOnlinePush
		'''

		url_path = "/service/sendAllOnlinePush"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'])
		params = {
			"body" : {
				"notice": "5분 후에 서버 점검이 시작됩니다."
				}
			}

		# None Response Content 
		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def sendConditionalPush(self):
		'''
		http://wiki.nzincorp.com/display/ZP/sendConditionalPush
		'''

		url_path = "/service/sendConditionalPush"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'])
		params = {
			"playerIds": self.scenario['push_receiver_Ids'],
			"onlineMessage": {
				"body": {
					"data": "1234"
				}
			},
			"offlineMessage": {
				"titleMap": {
					"en": "openAPI offline title",
					"ko": "openAPI offline title"
					},
				"bodyMap": {
					"en": "openAPI offline body",
					"ko": "openAPI offline body"
					}
				}
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)





	def eventLevelUp(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/eventLevelUp
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/eventLevelUp"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"deviceId": self.scenario['deviceId'],
			"level": 3
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def eventStageClear(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/eventLevelUp
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/eventStageClear"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"deviceId": self.scenario['deviceId'],
			"level": 3
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def eventPurchase(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/eventLevelUp
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/eventPurchase"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"deviceId": self.scenario['deviceId'],
			"itemCode": "gem100",
			"price": 3000
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def eventAppDefined(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/eventAppDefined
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/eventAppDefined"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"deviceId": self.scenario['deviceId'],
			"type":"invite",
			"value":"10"
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def checkReservation(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/checkReservation
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/checkReservation"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {
			"userKey": self.scenario['deviceId']
			}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	def setReferrer(self, inPlayerId=None):
		'''
		http://wiki.nzincorp.com/display/ZP/setReferrer
		'''

		if inPlayerId == None:
			inPlayerId = self.playerId

		url_path = "/service/checkReservation"
		headers = self.ngle.get_headers(
			appId = self.scenario['appId'],
			appSecret = self.scenario['appSecret'],
			playerId = inPlayerId)
		params = {}

		status_code, data = self.ngle.https_post_getData(url_path, params, headers)
		
		return (status_code, data)

	


