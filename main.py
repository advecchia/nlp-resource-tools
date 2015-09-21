#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#http://pythonhosted.org//python-weka-wrapper/install.html
#from modules import *
import logging as log
import argparse
from modules.parser.data_processor import RawDataProcessor
from modules.data.persistency import DataPersistency

def main(args):
    """
    """
    method_name = "Mestrado.main"
    log.info('{}: Data file manipulation.'.format(method_name))
    raw_data_file = args.filename
    log.info('{}'.format(raw_data_file))
    rdp = RawDataProcessor(raw_data_file)
    a = rdp.tokenize()
    print('{}'.format(a))
    dp = DataPersistency()
    filename = 'data/temp/dump.txt'
    dp.save_dump_to_file(a, filename)
    dump = dp.read_dump_from_file(filename)
    print('{}'.format(dump))
    

if __name__ == "__main__":
    log.basicConfig(filename='output.log', level=log.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
    log.info('Mestrado program initialization.')
    parser = argparse.ArgumentParser(description='This program is a workflow for the automatic construction of Natural Language Resources.')
    parser.add_argument('--filename', metavar='file', help='Input text file for processing')
    args = parser.parse_args()
    main(args)