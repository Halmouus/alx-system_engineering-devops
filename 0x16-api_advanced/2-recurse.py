#!/usr/bin/python3
"""
fetching the titles of all hot articles for a given subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[], page=""):
    """recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit"""
    headers = {'User-Agent': 'ApiTestALX'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json{page}'
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        return None
    if resp.status_code == 200:
        hot = resp.json()
        for post in hot['data']['children']:
            hot_list.append(post['data']['title'])
        if 'after' in hot['data'] and hot['data']['after'] is not None:
            next = hot['data']['after']
            recurse(subreddit, hot_list, f"?after={next}")
        return hot_list
