#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


url = raw_input("Enter URL ")   
path = raw_input("Enter path of the wordlist: ")

with open(path, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> http://" + test_url)
