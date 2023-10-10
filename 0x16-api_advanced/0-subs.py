#!/usr/bin/python3
"""a module tha includes a function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0'})
    dic = res.json()
    if dic is None:
        return 0
    subs = dic.get('data')
    subs = subs.get('subscribers')
    return 0 if (subs is None) else subs
