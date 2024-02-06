from .data import existing_options
from instance import chat


def send_options(sender_id, options, title="Comment puis-je vous aider ?"):
    selected_options = []
    if not options or len(options) < 1:
        return None
    for option in options:
        selected_options.append(existing_options.get(option))
    chat.send_quick_reply(sender_id, selected_options, title) 