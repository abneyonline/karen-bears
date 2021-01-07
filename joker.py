import praw
import json
from utils.setup import load_config
from random import choice


def run(command, args, voice_instance):
    creds = load_config("addons/joker/creds.json")

    reddit = praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        password=creds["password"],
        user_agent=creds["user_agent"],
        username=creds["username"],
    )

    if "dad joke" in command:
        subreddit = reddit.subreddit("dadjokes")
    else:
        subreddit = reddit.subreddit("jokes")

    joke = choice(
        [
            (joke.title, joke.selftext)
            for joke in subreddit.hot(limit=10)
            if not joke.stickied
        ]
    )

    title, text = joke

    voice_instance.say(f"{title}, {text}")
