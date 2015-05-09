# Copyright (c) 2014 Aluminium Computing, Inc., under APL

# the program class

import string

lictimes = 0

def find(num_list, num, start, end):
  # Report the index in num_list that contains num or -1 if not found.
  # ASSUMPTION: num_list is sorted
  if start == end:
    if num_list[start] == num:
      return start
    else:
      return -1
  mid = (start + end)/2
  if num_list[mid] == num:
    return mid
  elif num_list[mid] < num:
    return find(num_list, num, mid + 1, end)
  else: # num_list[mid] > num
    return find(num_list, num, start, mid-1)
  return -1


class Program(object):
  Keywords = [ "REM",
               "GOTO",
               "PRINT",
             ]
  def __init__(self):
    self.lines = {}


  def hh_print(self, string):
    unlicenced = False
    if unlicenced and (lictimes % 10 == 0):
      print("Your copy of HHBasic(TM) is unlicenced!\nPlease obtain a licence from Aluminium Computing, Inc.")
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
      elif statement[0] == "GOTO":
        try:
          line_num = int(statement[1])
          go_num = find(line_order, line_num, 0, len(line_order) -1)
          if go_num >= 0: 
            self.pc = go_num - 1
          else: # WE NEVER GET HERE!!!!!
            print "SYNTAX ERROR IN LINE %d: NO SUCH LINE %d." % \
              (line_order[self.pc], line_num)
        except:
          print "SYNTAX ERROR: Invalid line number '%s' in\n   %d %s" % \
            (statement[1], line_order[self.pc], self.lines[line_order[self.pc]]
      self.pc += 1
