# -*- coding: utf-8 -*-
from openAPI import APITest

if __name__=='__main__':
	api = APITest()
	
	status_code, data = api.loginTestPlayer()
	print '-' * 80
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.validateZinnyAccessToken()
	# print status_code, '\n', data, '\n', ('-' * 80)

	# status_code, data = api.refreshZinnyAccessToken()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.sendMessage()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.getReceivedMessages()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.claimAttachedItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.confirmAttachedItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.claimItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.confirmItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.finishMessages()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.writePurchaseLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.writeResourceLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.writeActionLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.writeRoundLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.writeItemLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	# status_code, data = api.sendPush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.sendOnlinePush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.sendAllOnlinePush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = api.sendConditionalPush()
	print status_code, '\n', data, '\n', ('-' * 80)

	

	


	

	

	

	

