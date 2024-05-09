#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests
from sys import argv

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    """
    user_agent = {'User-Agent': 'Lizzie'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <subreddit>")
    else:
        top_ten(argv[1])
