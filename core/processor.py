import socket
import threading
import configparser
import sys
import os
import queue

sys.path.append(os.path.abspath('..'))
from usr_func import *


class DataProcessor:
    def __init__(self, host, port, process_func):
        self.host = host
        self.port = port
        self.process_func = process_func
        self.queue = queue.Queue()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((self.host, self.port))
        print('Listening on {}:{}'.format(self.host, self.port))
        t = threading.Thread(target=self.process, args=(server_socket,))
        t.start()

    def process(self, server_socket):
        while True:
            data, addr = server_socket.recvfrom(1024)
            processed_data = self.process_func(data)
            self.queue.put(processed_data)

    def get_processed_data(self):
        return self.queue.get()


if __name__ == '__main__':
    # read configuration from file
    config = configparser.ConfigParser()
    config.read('../config.ini')

    # create data processors for each data source
    processors = []
    for section in config.sections():
        host = config.get(section, 'host')
        port = config.getint(section, 'port')
        process_func = globals()[config.get(section, 'process_func')]
        processor = DataProcessor(host, port, process_func)
        processors.append(processor)

    # start data processors
    for processor in processors:
        processor.start()
