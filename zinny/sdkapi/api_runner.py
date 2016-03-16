# -*- coding: utf-8 -*-
from nGle_util import nGle_util
from auth.auth_api import api_login


if __name__=='__main__':
	login = api_login()
	
	status_code, data = login.loginTestPlayer()
	print '-' * 80
	print status_code, '\n', data, '\n', ('-' * 80)

	
