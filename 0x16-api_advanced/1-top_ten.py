#!/usr/bin/python3
"""
fetching the first 10 hot posts listed of a given subreddit
"""
import json
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit"""
    headers = {'User-Agent': 'ApiTestALX'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        print("None")
    if resp.status_code == 200:
        hot = resp.json()
        titles = []
        for post in hot['data']['children'][:10]:
            titles.append(post['data']['title'])
        for title in titles:
            print(title)