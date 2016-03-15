# -*- coding: utf-8 -*-
import SocketServer
import json
import psutil
import datetime, time

class get_psutil_members:
    '''
    https://pythonhosted.org/psutil/
    '''

    def __init__(self):
        pass

    def get_net_port_counter(self, *args):
        port_counter = 0
        for c in psutil.net_connections(kind='inet'):
            if c.status == "ESTABLISHED":
                if c.laddr[1] in args:
                    port_counter += 1

        return port_counter

    def get_psutil(self):
        
        cpu_times = psutil.cpu_times()
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        disk_io_counters = psutil.disk_io_counters()
        net_io_counters = psutil.net_io_counters()
        
        dt_now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        items = {}

        items = {
            "datetime": dt_now,
            "cpu_user": cpu_times.user,
            "cpu_system": cpu_times.system,
            "cpu_idle": cpu_times.idle,
            "cpu_perc": psutil.cpu_percent(interval=1),
            "cpu_per_perc": psutil.cpu_percent(percpu=True),
            "mem_total": virtual_memory.total,
            "mem_available": virtual_memory.available,
            "mem_used": virtual_memory.used,
            "mem_free": virtual_memory.free,
            "mem_perc": virtual_memory.percent,
            "swap_totla": swap_memory.total,
            "swap_used": swap_memory.used,
            "swap_free": swap_memory.free,
            "swap_perc": swap_memory.percent,
            "disk_read_count": disk_io_counters.read_count,
            "disk_write_count": disk_io_counters.write_count,
            "disk_read_bytes": disk_io_counters.read_bytes,
            "disk_write_bytes": disk_io_counters.write_bytes,
            "net_sent_bytes": net_io_counters.bytes_sent,
            "net_recv_bytes": net_io_counters.bytes_recv,
            "net_sent_packets": net_io_counters.packets_sent,
            "net_recv_packets": net_io_counters.packets_recv,
            "net_port_count": self.get_net_port_counter(80,443, 8080)
            }

        return items


class NGLE_TCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        gpm = get_psutil_members()
        data_string = json.dumps(gpm.get_psutil())

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        self.request.sendall(data_string)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), NGLE_TCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()