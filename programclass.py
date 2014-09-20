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
      print "Run not implemented. Line %d : %s" % \
          (line_order[self.pc], self.lines[line_order[self.pc]])
      self.pc += 1
