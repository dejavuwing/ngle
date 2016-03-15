# -*- coding: utf-8 -*-
import socket
import time
import signal
import csv
import os
import json

from nGle_util import nGle_util


class set_file_members:
	def __init__(self):
		self.ngle = nGle_util()

	def set_file(self, address='localhost', datas=list()):
		file_name = "nGle_sys_{}_{}".format(address, self.ngle.get_date())

		top_title = [
			"time",
			"cpu_times.user",
			"cpu_times.system",
			"cpu_times.idle",
			"cpu_percent(%)",
			"cpu_percent_per_cpu",
			"mem_virtual.total(Mbyte)",
			"mem_virtual.available(Mbyte)",
			"mem_virtual.used(Mbyte)",
			"mem_virtual.free(Mbyte)",
			"mem_virtual.percent(%)",
			"mem_swap.total(Mbyte)",
			"mem_swap.used(Mbyte)",
			"mem_swap.free(Mbyte)",
			"mem_swap.percent(%)",
			"disk_io.read_count",
			"disk_io.write_count",
			"disk_io.read(Mbyte)",
			"disk_io.write(Mbyte)",
			"net_io.sent(Mbyte)",
			"net_io.recv(Mbyte)",
			"net_io.packets_sent",
			"net_io_counters.packets_recv",
			"net_port_counter(80 443 8080)"
			]

		if os.path.exists(file_name):
			with open(file_name, "a+") as f:
				writer = csv.writer(f, delimiter='\t', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
				writer.writerow(datas)
		else:
			with open(file_name, "a+") as f:
				writer = csv.writer(f, delimiter='\t', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
				writer.writerow(top_title)
	

class call_resource:
	def __init__(self):
		self.ngle = nGle_util()
		pass

	def get_resource_data(self):
		HOST, PORT = "localhost", 9999
		data = "hi server"

		# Create a socket (SOCK_STREAM means a TCP socket)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			# Connect to server and send data
			sock.connect((HOST, PORT))
			sock.sendall(data)

			# Receive data from the server and shut down
			received = sock.recv(1024)
			recv_data = json.loads(received)

		finally:
			sock.close()

		sfm = set_file_members()
		datas = self.pars_recv_data(recv_data)
		sfm.set_file(HOST, datas)
		#print type(datas)
		

	def pars_recv_data(self, datas):

		items = list()

		items = [
			datas["datetime"],
			datas["cpu_user"],
			datas["cpu_system"],
			datas["cpu_idle"],
			datas["cpu_perc"],
			datas["cpu_per_perc"],
			self.ngle.change_B_to_M(datas["mem_total"]),
			self.ngle.change_B_to_M(datas["mem_available"]),
			self.ngle.change_B_to_M(datas["mem_used"]),
			self.ngle.change_B_to_M(datas["mem_free"]),
			datas["mem_perc"],
			self.ngle.change_B_to_M(datas["swap_totla"]),
			self.ngle.change_B_to_M(datas["swap_used"]),
			self.ngle.change_B_to_M(datas["swap_free"]),
			datas["swap_perc"],
			datas["disk_read_count"],
			datas["disk_write_count"],
			self.ngle.change_B_to_M(datas["disk_read_bytes"]),
			self.ngle.change_B_to_M(datas["disk_write_bytes"]),
			self.ngle.change_B_to_M(datas["net_sent_bytes"]),
			self.ngle.change_B_to_M(datas["net_recv_bytes"]),
			datas["net_sent_packets"],
			datas["net_recv_packets"],
			datas["net_port_count"]
			]

		return items


if __name__ == "__main__":
	ngle = nGle_util()
	signal.signal(signal.SIGINT, ngle.signal_handler)

	while True:
		call_resource().get_resource_data()
		time.sleep(5)

