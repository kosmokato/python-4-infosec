#!/usr/bin/python3
# -*- coding: utf-8 -*-

# For any sugestion contact to @kosmokato

"""
System commands from python3
"""

import subprocess


comando = "whoami"

out = subprocess.Popen(str(comando), 
  stdout=subprocess.PIPE, 
  stderr=subprocess.STDOUT, shell=True)
stdout,stderr = out.communicate()
output = stdout.decode().split('\n')  # list() with the output on the screen.
output = list(filter(None, output))

print("\n".join(output))  # print every line on the screen.