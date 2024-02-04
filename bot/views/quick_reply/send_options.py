from .data import existing_options
from instance import chat


def send_options(sender_id, options, title="Que voulez-vous faire ensuite ?"):
    selected_options = []
    if not options or len(options) < 1:
        return None
    for option in options:
        print(existing_options.get(option))
        selected_options.append(existing_options.get(option))
    chat.send_quick_reply(sender_id, selected_options, title)