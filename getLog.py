# -*- coding: utf-8 -*-
import pymysql.cursors
import json
import logging.handlers
import logging
import datetime, time
import os, sys

##############日志模块#############
class FinalLogger: 
   logger = None
   levels = {"n" : logging.NOTSET,
    "d" : logging.DEBUG,
    "i" : logging.INFO,
    "w" : logging.WARN,
    "e" : logging.ERROR,
    "c" : logging.CRITICAL}
   today=datetime.date.today()
   log_level = "d"
   log_file = "../log/"+"final_logger"+str(today)+".log"
   log_max_byte = 10 * 1024 * 1024;
   log_backup_count = 5
   @staticmethod

   def getLogger():

     FinalLogger.logger = logging.Logger("oggingtwt.FinalLogger")
     log_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file,\
     maxBytes = FinalLogger.log_max_byte,\
     backupCount = FinalLogger.log_backup_count)
     log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
     log_handler.setFormatter(log_fmt)
     FinalLogger.logger.addHandler(log_handler)
     FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
     return FinalLogger.logger


