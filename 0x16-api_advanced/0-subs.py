#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        results = response.json().get("data")
        if results and "subscribers" in results:
            return results.get("subscribers")
    
    # Return 0 if the subreddit does not exist or other issues
    return 0
