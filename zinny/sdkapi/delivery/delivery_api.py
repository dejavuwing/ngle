# -*- coding: utf-8 -*-
import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from nGle_util import nGle_util


class delivery_api():

	def __init__(self):
		self.ngle = nGle_util()

		with open('scenario.json') as data_file:
			self.scenario = json.load(data_file)

	