import datetime, time
import sys


class nGle_util:
	def __init__(self):
		pass

	def signal_handler(self, signal, frame):
		print 'lose nGle Sys Mon'
		sys.exit(0)

	def change_B_to_K(self, ebyte):
		return int(ebyte/1024)

	def change_B_to_M(self, ebyte):
		return int((ebyte/1024)/1024)

	def change_color(self, comm):
		if 80.0 <= comm <= 100.0:
			strComm = bcolors.FAIL + str(comm) + "%" + bcolors.ENDC
		elif 70.0 <= comm <= 79.9:
			strComm = bcolors.WARNING + str(comm) + "%" + bcolors.ENDC
		else:
			strComm = str(comm) + "%"

		return strComm

	def get_date(self, date_when='today'):
		today = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')

		if date_when == "today":
			date = today
		else:
			date = today

		return date

	def get_time(self):
		return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
