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

api_url = "http://artii.herokuapp.com/make?text="


def getlogo(logostr):
    req = requests.get(api_url + logostr, headers=headers, timeout=10)

    if req.status_code == requests.codes.ok:
        ascii_content = req.text
        ascii_soup = BeautifulSoup(ascii_content, features="html5lib")
        logo_soup = ascii_soup.find('body').text
        print(logo_soup)


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('logo', action='store', type=str)
    options = parser.parse_args()
    return options


if __name__ == "__main__":
    options = get_options()
    lg = options.logo
    getlogo(lg)
