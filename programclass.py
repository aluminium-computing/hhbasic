# Copyright (c) 2014 Aluminium Computing, Inc., under APL

# the program class

class Program(object):
  def __init__(self):
    self.lines = {}


  def addLine(self, line):
    tokenized = line.split(" ")
    key = int(tokenized[0])
    statement = line[len(str(key))+1:]
    self.lines[key] = statement
