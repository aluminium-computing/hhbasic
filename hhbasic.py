# Copyright (c) 2014 Aluminium Computing, Inc., under APL.

# Written in Python 2.7
# A HHBasic implementation for Linux.

import os # To clear screen

def HHBasic():
  # Initialize
  os.system('clear') # clear screen
  print " HHBasic pa1.0"
  print " Copyright 2014 Aluminium Computing, Inc."
  interpreter_commands = [
    "HALT",   # exit
    "LIST",   # list program in memory
    "LOAD",   # load a program from disk
    "NEW",    # clear memory
    "RUN",    # execute the program in memory
    "SAVE",   # save program in memory to disk 
  ]
  while True:
    inline = raw_input(">")
    cmd = inline.split(" ")
    is_statement = False
    if cmd[0] == "HALT": exit()
    try:
      is_statement = int(cmd[0])
    except ValueError:
      if cmd[0] not in interpreter_commands:
        print("I don't understand what you're trying to do. That's not a command or a program line.")
        continue
    # At this point we either have a statement with a valid line number or a command to process


def main():
  # TODO: Trap for KeyboardInterrupt exception to handle Ctrl-C
  HHBasic()

if __name__ == "__main__": main()

