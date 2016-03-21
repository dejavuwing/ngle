# -*- coding: utf-8 -*-
import unittest
from mock import Mock

from nGle_util import nGle_util
from openapi.open_api import openapi_temp


class Test_oepnAPI(unittest.TestCase):

	api = openapi_temp()
	ngle = nGle_util()
	mock = Mock()

	def setUp(self):
		testName = self.shortDescription()
		pass

	def tearDown(slef):
		pass

	def test_1_loginTestPlayer(self):
		'''test_1_loginTestPlayer'''

		status, data = self.api.loginTestPlayer()
		self.mock.zat.return_value = data['zat']
		self.mock.playerId.return_value = data['player']['playerId']
	
		self.assertEqual(200, status)
		self.assertIsInstance(self.mock.playerId(), unicode)
		self.assertIsInstance(self.mock.zat(), unicode)

	def test_2_validateZinnyAccessToken(self):
		'''test_2_validateZinnyAccessToken'''

		status, data = self.api.validateZinnyAccessToken(self.mock.playerId(), self.mock.zat())
		self.assertEqual(200, status)

	def test_3_refreshZinnyAccessToken(self):
		'''test_3_refreshZinnyAccessToken'''

		status, data = self.api.refreshZinnyAccessToken(self.mock.playerId(), self.mock.zat())
		self.mock.zat.return_value = data['zat']

		expiryTime = self.ngle.get_timestamp_to_datetime(data['zatExpiryTime'])
		currentTime = self.ngle.get_time()

		self.assertEqual(200, status)
		self.assertIsInstance(self.mock.zat(), unicode)
		self.assertGreaterEqual(expiryTime, currentTime)

	def test_4_sendMessage(self):
		'''test_4_sendMessage'''

		status, data = self.api.sendMessage(self.mock.playerId())
		messageId = data['messageId']

		self.assertEqual(200, status)
		self.assertIsInstance(messageId, unicode)

	def test_5_getReceivedMessages(self):
		'''test_5_getReceivedMessages'''

		status, data = self.api.getReceivedMessages(self.mock.playerId())
		item_totalCount = data['totalCount']

		if item_totalCount > 0:
			claim_itemId = []
			claim_messageId = []
			claim_itemId.append(str(data['messages'][0]['items'][0]['itemId']))
			claim_messageId.append(str(data['messages'][0]['message']['messageId']))
			self.mock.claim_itemId.return_value = claim_itemId
			self.mock.claim_messageId.return_value = claim_messageId

		self.assertEqual(200, status)
		self.assertGreaterEqual(item_totalCount, 0)

	def test_6_claimAttachedItems(self):
		'''test_6_claimAttachedItems'''

		status, data = self.api.claimAttachedItems(self.mock.playerId(), self.mock.claim_itemId())

		self.assertEqual(200, status)
		if status == 200:
			claim_itemId = []
			claim_itemId.append(data['items'][0]['itemId'])

			print type(claim_itemId)
			self.assertListEqual(self.mock.claim_itemId(), claim_itemId)

	def test_7_confirmAttachedItems(self):
		'''test_7_confirmAttachedItems'''

		status, data = self.api.confirmAttachedItems(self.mock.playerId(), self.mock.claim_itemId())

		self.assertEqual(200, status)

	def test_8_claimItems(self):
		'''test_8_claimItems'''

		status, data = self.api.claimItems(self.mock.playerId(), self.mock.claim_messageId())

		self.assertEqual(200, status)
		if status == 200:
			claim_messageId = []
			claim_messageId.append(data['results'][0]['messageId'])
			self.assertListEqual(self.mock.claim_messageId(), claim_messageId)

	def test_9_confirmItems(self):
		'''test_9_confirmItems'''

		status, data = self.api.confirmItems(self.mock.playerId(), self.mock.claim_messageId())

		self.assertEqual(200, status)


if __name__ == '__main__':
	unittest.main()

	#fooRunner = unittest.TextTestRunner()
	#fooRunner.run(fooSuite)




