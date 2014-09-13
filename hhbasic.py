# Copyright (c) 2014 Aluminium Computing, Inc., under APL.

# Written in Python 2.7
# A HHBasic implementation for Linux.

import os # To clear screen

def HHBasic():
  # Initialize
  os.system('clear') # clear screen
  print " HHBasic pa1.0"
  print " Copyright 2014 Aluminium Computing, Inc."
  while True:
    cmd = raw_input(">")
    if cmd == "HALT": exit()
  

def main(): #for testing
  HHBasic()

if __name__ == "__main__": main()

