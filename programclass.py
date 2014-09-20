# Copyright (c) 2014 Aluminium Computing, Inc., under APL

# the program class

import string

class Program(object):
  Keywords = [ "REM",
               "GOTO",
               "PRINT",
             ]
  def __init__(self):
    self.lines = {}


  def hh_print(self, string):
    unlicensed = False
    if unlicensed:
      print("UNLICENSED HHBASIC 1.0")
    print(string) 


  def addLine(self, line):
    tokenized = line.split(" ")
    key = int(tokenized[0])
    statement = line[len(str(key))+1:]
    self.lines[key] = statement


  def list(self):
    for i in sorted(self.lines.keys()):
      if self.lines[i]:
        print "%d %s" % (i, self.lines[i])
  
  
  def new(self):
    self.lines = {}
  

  def run(self):
    """ Run: execute the program from the beginning. """
    self.pc = 0
    self.variables = {}
    line_order = sorted(self.lines.keys())
    while self.pc < len(line_order):
      # run the statement at self.lines[line_order[self.pc]]
      # ASSUMPTION: every statement starts with a keyword:
      statement = self.lines[line_order[self.pc]].split(" ")
      if statement[0] not in self.Keywords:
        print "SYNTAX ERROR: Unknown keyword '%s'in\n   %d %s" % \
          (statement[0], line_order[self.pc], self.lines[line_order[self.pc]])
      elif statement[0] == "PRINT":
        stp = (string.join(statement[1:], " ")).strip('"')
        self.hh_print(stp)
      elif statement[0] == "REM":
        pass
      else:  
        print "Run not implemented. Line %d : %s" % \
            (line_order[self.pc], self.lines[line_order[self.pc]])
      self.pc += 1
