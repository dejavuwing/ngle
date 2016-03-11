# -*- coding: utf-8 -*-
import unittest
from mock import Mock
from openAPI import APITest

class Test_oepnAPI(unittest.TestCase):

	api = APITest()
	mock = Mock()

	def setUp(self):
		testName = self.shortDescription()

		if testName in ('t2', 't3'):
			ee, data = self.api.loginTestPlayer()
			self.zat = data['zat']
			self.playerId = data['player']['playerId']
		elif testName in ('t4', 't5'):
			self.playerId = "8523698741.td.1"

	def tearDown(slef):
		pass

	def test_1_loginTestPlayer(self):
		'''t1'''

		status, data = self.api.loginTestPlayer()
		self.mock.zat.return_value = data['zat']
		self.mock.playerId.return_value = data['player']['playerId']
	
		self.assertEqual(200, status)
		self.assertIsInstance(self.mock.playerId(), unicode)
		self.assertIsInstance(self.mock.zat(), unicode)

	def test_2_validateZinnyAccessToken(self):
		'''t2'''

		status, data = self.api.validateZinnyAccessToken(self.mock.playerId(), self.mock.zat())
		self.assertEqual(200, status)

	def test_3_refreshZinnyAccessToken(self):
		'''t3'''

		status, data = self.api.refreshZinnyAccessToken(self.mock.playerId(), self.mock.zat())
		self.mock.zat.return_value = zat = data['zat']

		self.assertEqual(200, status)
		self.assertIsInstance(self.mock.zat(), unicode)

	def test_4_sendMessage(self):
		'''t4'''

		status, data = self.api.sendMessage(self.mock.playerId())
		messageId = data['messageId']

		self.assertEqual(200, status)
		self.assertIsInstance(messageId, unicode)

	def test_5_getReceivedMessages(self):
		'''t5'''

		status, data = self.api.getReceivedMessages(self.mock.playerId())
		item_totalCount = data['totalCount']

		self.assertEqual(200, status)
		self.assertGreaterEqual(item_totalCount, 0)


if __name__ == '__main__':
	unittest.main()

	#fooRunner = unittest.TextTestRunner()
	#fooRunner.run(fooSuite)



