#!/usr/bin/python3
"""a module tha includes a function that queries the Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    res = requests.get(f"https://www.reddit.com/r/{sys.argv[1]}/about.json")
    dic = res.json()
    subs = dic.get('data').get('subscribers')
    return 0 if (subs is None) else subs
