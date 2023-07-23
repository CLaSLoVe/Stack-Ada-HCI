import configparser
from core.processor import DataProcessor
from core.stack import Stack
from usr_func import *

if __name__ == '__main__':
    # read configuration from file
    config = configparser.ConfigParser()
    config.read('config/port.ini')

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

    stack = Stack(par_namelist)

    # main loop to process data
    while True:
        for processor in processors:
            data = processor.get_data()
            if data is not None:
                stack.get(data)
                print(stack.get_bias())