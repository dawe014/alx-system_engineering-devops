#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""
    # Base URL for the Reddit API
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set the custom User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Set parameters for pagination
    params = {
        "after": after,
        "limit": 100
    }
    
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # If the subreddit is invalid, return None
    if response.status_code == 404:
        return None

    # If the response is not OK, return the current hot_list
    if response.status_code != 200:
        return hot_list
    
    # Parse the JSON response
    results = response.json().get("data")
    after = results.get("after")
    children = results.get("children")
    
    # Add titles of the current batch of hot posts to the hot_list
    for child in children:
        hot_list.append(child.get("data").get("title"))

    # If there is a next page, continue recursion
    if after:
        return recurse(subreddit, hot_list, after)
    
    # Return the complete list of titles
    return hot_list
