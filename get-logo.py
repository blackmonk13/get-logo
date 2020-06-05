#!/usr/bin/env python
# Copyright 2020 Blackmonk13. All rights reserved.
#
# This software is provided under under the 
# GNU GPL V3 License. See the accompanying LICENSE file
# for more information.
#
# Author:
#  blackmonk (@protonmail.com)
#
import requests
from bs4 import BeautifulSoup
import argparse

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }

if __name__ == "__main__":
  print("get-logo")