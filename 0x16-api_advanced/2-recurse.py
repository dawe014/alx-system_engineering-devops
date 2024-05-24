import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively return a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list.extend([child["data"]["title"] for child in children])
        after = data.get("after")
        
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    
    return None if response.status_code == 404 else hot_list

# Example usage:
# print(recurse('python'))  # Should return a list of titles of hot articles in r/python
# print(recurse('thissubredditdoesnotexist'))  # Should return None
