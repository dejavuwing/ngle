# -*- coding: utf-8 -*-
from nGle_util import nGle_util
from api_papabravo import papabravo


if __name__=='__main__':
	p = papabravo()
	
	status_code, data = p.login_LoginToLoginServer()
	print '-' * 80
	print status_code, '\n', data, '\n', ('-' * 80)