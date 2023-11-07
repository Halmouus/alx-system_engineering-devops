#!/usr/bin/python3
"""
fetch the number of subscribers of a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number
    of subscribers for a given subreddit"""
    headers = {'User-Agent': 'ApiTestALX'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        return 0
    if resp.status_code == 200:
        about = resp.json()
        subcount = about['data']['subscribers']
        return subcount
