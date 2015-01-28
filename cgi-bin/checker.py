#!/usr/local/bin/python3

from re import search
from codecs import open

def removeCommit(strline):
  if '//' in strline:
    strline=strline[:strline.index('//')]
  return strline

def Checker(filepath):
  banList=['system','sort']
  with open(filepath,'r',"unicode_escape") as infile:
    strlines=infile.readlines()
  strlines=list(map(lambda x: removeCommit(x) ,strlines))
  if any(list(filter(lambda x: any(list(map(lambda y:search(y,x),banList))) ,strlines))):
    print('forbidden word used\n')
    print(list(filter(lambda x: any(list(map(lambda y:search(y,x),banList))) ,strlines)))
    return False
  else:
    return True

