#!/usr/bin/python3
"""Query GitHub API for commits
"""
import requests
import sys


def get_commits():
    """Query GitHub API for commits
    """
    repo, owner = sys.argv[1:]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10W"
    res = requests.get(url)
    body = res.json()
    for res in body:
        print(f"{res['sha']}: {res['commit']['author']['name']}")


if __name__ == "__main__":
    get_commits()
