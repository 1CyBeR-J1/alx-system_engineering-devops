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

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = get(url, headers=user_agent)

    if (r.status_code is 302):
        return 0
    if (r.status_code is 404):
        return 0

    return r.json()['data'].get('subscribers', 0)
