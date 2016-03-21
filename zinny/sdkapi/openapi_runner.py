# -*- coding: utf-8 -*-
from nGle_util import nGle_util

from openapi.open_api import openapi_temp
# from delivery.message_api import message_api
# from delivery.delivery_api import delivery_api



if __name__=='__main__':
	openapi = openapi_temp()
	# message = message_api()
	# delivery = delivery_api()
	
	status_code, data = openapi.loginTestPlayer()
	print '-' * 80
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.validateZinnyAccessToken()
	# print status_code, '\n', data, '\n', ('-' * 80)

	# status_code, data = openapi.refreshZinnyAccessToken()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.sendMessage()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.getReceivedMessages()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.claimAttachedItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.confirmAttachedItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.claimItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.confirmItems()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.finishMessages()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.writePurchaseLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.writeResourceLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.writeActionLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.writeRoundLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.writeItemLog()
	# print status_code, '\n', data, '\n', ('-' * 80)

	# status_code, data = openapi.sendPush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.sendOnlinePush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.sendAllOnlinePush()
	# print status_code, '\n', data, '\n', ('-' * 80)

	status_code, data = openapi.sendConditionalPush()
	print status_code, '\n', data, '\n', ('-' * 80)



	
