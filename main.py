#!/usr/bin/python3

import praw

reddit = praw.Reddit('CommentCloud')

print(reddit.read_only)
