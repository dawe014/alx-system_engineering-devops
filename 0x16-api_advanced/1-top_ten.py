import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, print None.
    """
    user_agent = {'User-Agent': 'Lizzie'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    elif response.status_code == 404:
        print("None")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
