#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return None

    if response.status_code != 200:
        return hot_list

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist", 0)

    for child in results.get("children", []):
        hot_list.append(child.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list
