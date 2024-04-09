import requests

def number_of_subscribers(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json().get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
