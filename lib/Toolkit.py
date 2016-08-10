#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Toolkit script for all types of functions, needed throughout the project
#
# Copyright (c) 2015	NorthernSec
# Copyright (c)	2015	Pieter-Jan Moreels
# This software is licensed under the Original BSD License

# Imports
import os
import re
import json
from dateutil import tz
import dateutil.parser
from datetime import datetime

# string to dict
def make_dict(s):
  # break into list of keys and values
  chunks = re.split('\s*(\w+\:)\s*',s)
  res={}
  # work backwards in value, key pairs
  args=[reversed(chunks)]*2
  for value,key in zip(*args):
    key=key.rstrip(':')
    if value:
      #add to current result-dict
      res[key]=value
    else:
      #start a higher-level result-dict
      res={key:res}
  return res

def writeJson(file, data):
  if os.path.exists(file):
    os.remove(file)
  with open(file, 'w') as dump:
    json.dump(data, dump, indent=2)

def toLocalTime(utc):
  timezone = tz.tzlocal()
  utc = dateutil.parser.parse(utc)
  output = utc.astimezone(timezone)
  output = output.strftime('%d-%m-%Y - %H:%M')
  return output

def fromEpoch(epoch):
  return datetime.fromtimestamp(epoch).strftime('%a %d %h %Y at %H:%M:%S')

def toHuman(cpe):
  cpe = cpe[7:]
  result = cpe.split(':')[0] + " - "
  for c in cpe.split(':')[1:]:
    c = c.replace(':', ' ')
    c = c.replace('_', ' ')
    result += (" %s" %(c))
  result = result.title()
  return result

def splitByLength(string, size=50):
  return [string[i:i+size] for i in range(0,len(string),size)]
