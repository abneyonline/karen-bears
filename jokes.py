from utils.settings import get_addon_settings


import praw
import json
from utils.setup import load_config
from random import choice

USER_SETTINGS = get_addon_settings("jokes")


def run(command, args, voice_instance):
    creds = load_config("addons/joker/creds.json")

    reddit = praw.Reddit(
        client_id=USER_SETTINGS["client_id"],
        client_secret=USER_SETTINGS["client_secret"],
        password=USER_SETTINGS["password"],
        user_agent="karen_jokes",
        username=USER_SETTINGS["username"],
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
