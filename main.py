#!/usr/bin/python3

import praw

#Read only mode
reddit = praw.Reddit('CommentCloud')

print(reddit.read_only)

user = reddit.redditor("reddit_username_here")
for comment in user.comments.new(limit=None):
    print(comment.body)
