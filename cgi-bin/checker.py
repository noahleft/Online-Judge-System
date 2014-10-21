#!/usr/local/bin/python3

from re import search

def Checker(filepath):
  banList=['system']
  with open(filepath,'r') as infile:
    strlines=infile.readlines()
  if any(list(filter(lambda x: any(list(map(lambda y:search(y,x),banList))) ,strlines))):
    print('forbidden word used')
    return False
  else:
    return True

