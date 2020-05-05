#!/usr/bin/python3
# -*- coding: utf-8 -*-

# For any sugestion contact to @kosmokato

"""
Get system time
"""

# HOW LONG DOES IT TAKES?
# -----------------------
from datetime import datetime

# at the top
start_time = datetime.now()
# [...]  # rest of the code
# at the bot
end_time = datetime.now()
print('[i] Execution time: {}'.format(end_time - start_time))  #hh:mm:ss.ms