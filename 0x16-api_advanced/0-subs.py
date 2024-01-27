#!/usr/bin/python3
"""
module contains reddit api request
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the
    number of subscribers (not active users, total subscribers)
    for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'MyBot/0.0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
