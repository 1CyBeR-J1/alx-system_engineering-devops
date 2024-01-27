#!/usr/bin/python3
"""
Module contains a function that prints from reddit API
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
    """

    url_base = 'http://www.reddit.com/r/'
    url_query = '{:s}/hot.json?limit={:d}'.format(subreddit, 10)
    headers = {'user-agent': 'Botquest'}
    r = requests.get(url_base + url_query, headers=headers)

    if (r.status_code is 302):
        print("None")
        return
    if (r.status_code is 404):
        print("None")
        return
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
