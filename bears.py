from random import choice

USER_SETTINGS = get_addon_settings("bears")

jokes = ["How much does a polar bear weigh? Enough to break the ice.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why don't polar bears get married? They all have cold feet.",
    "What do you call bears with no ears? Bees!"]


def run(command, args, voice_instance):
    if "bear joke" in command:
        voice_instance.say(random.choice(jokes))
    else:
        voice_instance.say(f"Bears.")
