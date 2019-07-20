#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:02:16 2019

@author: fractaluser
"""

'''
Created on 20-Jul-2019

@author: fractaluser
'''
import logging
import datetime
import os
from configparser import ConfigParser

class loggerfunc(object):

     def __init__(self,level):
                self.level=level

                print(self.level)

     def setlogginglevel(self):

           logginglevel=str.upper(self.level)
           LEVELS = {'DEBUG':logging.DEBUG,
                     'INFO': logging.INFO,
                     'WARNING': logging.WARNING,
                     'ERROR': logging.ERROR,
                     'CRITICAL': logging.CRITICAL}
           self.loglevel=LEVELS[logginglevel]

     def logger(self):

        self.setlogginglevel()

        logger_test=logging.getLogger(__name__)
        current_date=datetime.date.today().isoformat()
        logger_test.setLevel(self.loglevel)
        p=os.getcwd()
        os.system("mkdir -p %s/logs"%p)
        ch = logging.FileHandler('%s/logs/datadownload_%s.log'%(p,current_date),mode='a')
        ch.setLevel(self.loglevel)
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger_test.addHandler(ch)
        return(logger_test)
    
if __name__=="__main__":
       level="info"
       t1=loggerfunc(level)
       t2=t1.logger()
       print(t2)
