#!/usr/bin/python3
"""Script to parse json response
from a server
"""
import requests
import sys


def post_email():
    """Send email to the given url
    using python requests package
    """
    try:
        url = "http://0.0.0.0:5000/search_user"
        q = ""
        if len(sys.argv) > 1:
            q = sys.argv[1]

        res = requests.post(url, {"q": q})
        body = res.json()

        if len(body) == 0:
            print("No result")
        else:
            print(f"[{body.get('id')}] {body.get('name')}")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    post_email()
